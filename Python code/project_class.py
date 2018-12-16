from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from wordcloud import WordCloud
import pygal
#
class project:
    """ project class """
    def genre_2006_2016(data):
        genre = data["Genre"].tolist()
        years = data["Year"].tolist()
        for ye in range(2006, 2017):
            dic = {}
            count = 0
            for i in range(len(genre)):
                if years[i] == ye:
                    value = genre[i].split(",")
                    for j in value:
                        if j in dic:
                            dic[j] += 1
                        else:
                            dic[j] = 1
                    count += 1
            graph = pygal.Bar()
            graph.title = "ประเภทของภาพยนตร์ปี %d [%d เรื่อง]" %(ye,count)
            for i in sorted(dic, key = lambda x: dic[x], reverse=True):
                graph.add(i, dic[i])
            graph.render_to_file("../Graph/%d.svg" %ye)
            graph.render_to_file("../docs/assets/images/%d.svg" %ye)
###############################################################################################################################
    def genre_graph(data):
        genre = data["Genre"].tolist()
        genre_2 = []
        dic = {}
        for i in genre:
            check = i.split(",")
            for i in check:
                genre_2.append(i)
        dic2 = {}
        for i in genre_2:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in dic:
            dic2[dic[i]] = i
        graph = pygal.Bar()
        graph.title = "ประเภทของภาพยนตร์ ตั้งแต่ปี 2006 - 2016"
        value = []
        for i in sorted(dic.values())[::-1]:
            graph.add(dic2[i], i)
        graph.render_to_file("../Graph/genre_graph.svg")
        graph.render_to_file("../docs/assets/images/genre_graph.svg")
###############################################################################################################################
    def genre_price(data):
        genre = data["Genre"].tolist()
        revenue = data["Revenue (Millions)"].tolist()
        year = data["Year"].tolist()
        genre_reduce = []
        for i in genre:
            check = i.split(",")
            for i in check:
                genre_reduce.append(i)
                year.append(year[genre_reduce.index(i)])
                revenue.append(revenue[genre_reduce.index(i)])
        dic_2006 = {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}
        dic_2007,dic_2008,dic_2009,dic_2010,dic_2011,dic_2012,dic_2013,dic_2014,dic_2015,dic_2016 = \
        dic_2006.copy(),dic_2006.copy(),dic_2006.copy(),dic_2006.copy(),dic_2006.copy(),dic_2006.copy(),dic_2006.copy(),dic_2006.copy()\
        ,dic_2006.copy(),dic_2006.copy()
        count = 0
        for i in genre_reduce:
            if year[count] == 2006:
                state = dic_2006
            if year[count] == 2007:
                state = dic_2007
            if year[count] == 2008:
                state = dic_2008
            if year[count] == 2009:
                state = dic_2009
            if year[count] == 2010:
                state = dic_2010
            if year[count] == 2011:
                state = dic_2011
            if year[count] == 2012:
                state = dic_2012
            if year[count] == 2013:
                state = dic_2013
            if year[count] == 2014:
                state = dic_2014
            if year[count] == 2015:
                state = dic_2015
            if year[count] == 2016:
                state = dic_2016
            if i not in state:
                state[i] = revenue[count]
            else:
                state[i] += revenue[count]
            count += 1
        graph = pygal.Bar()
        graph.title = "รายได้ของภาพยนตร์แต่ละประเภท [รวมทุกปี] (US-Dollars Millions)"
        listed_genre = ["Action", "Adventure","Horror","Animation","Comedy","Biography","Drama","Crime","Romance","Mystery","Thriller","Sci-Fi","Fantasy"]
        listed_each = [dic_2006, dic_2007, dic_2008, dic_2009, dic_2010 , dic_2011, dic_2012, dic_2013, dic_2014, dic_2015, dic_2016]
        all_dic = {}
        for dic in listed_each:
            for j in dic:
                if j in all_dic:
                    all_dic[j] += dic[j]
                else:
                    all_dic[j] = dic[j]
        for i in sorted(all_dic, reverse=True, key= lambda x: all_dic[x]):
            graph.add(i, all_dic[i])
        graph.render_to_file("../Graph/genre_price_all.svg")
        graph.render_to_file("../docs/assets/images/genre_price_all.svg")
        graph = pygal.Line()
        graph.title = "รายได้จากการขายภาพยนตร์แต่ละประเภทในแต่ละปี (US-Dollars Millions)"
        graph.x_labels = map(str, range(2006, 2017))
        listed_genre = ["Action", "Adventure","Horror","Animation","Comedy","Biography","Drama","Crime","Romance","Mystery","Thriller","Sci-Fi","Fantasy"]
        for i in listed_genre:
            graph.add("%s" %i, [dic_2006["%s" %i], dic_2007["%s" %i], dic_2008["%s" %i], dic_2009["%s" %i], dic_2010["%s" %i], dic_2011["%s" %i], dic_2012["%s" %i]\
            , dic_2013["%s" %i], dic_2014["%s" %i], dic_2015["%s" %i], dic_2016["%s" %i]])
        graph.render_to_file("../Graph/genre_price_each_years.svg")
        graph.render_to_file("../docs/assets/images/genre_price_each_years.svg")
        listed_each = [dic_2006, dic_2007, dic_2008, dic_2009, dic_2010 , dic_2011, dic_2012, dic_2013, dic_2014, dic_2015, dic_2016]
        count = 0
        for i in range(2006, 2017):
            graph = pygal.Bar()
            graph.title = "รายได้รวมของภาพยนตร์ปี %d (US-Dollars Millions)" %i
            for j in sorted(listed_each[count], key= lambda x: listed_each[count][x], reverse=True):
                graph.add(j, listed_each[count][j])
                graph.render_to_file("../Graph/price%d.svg" %i)
                graph.render_to_file("../docs/assets/images/price%d.svg" %i)
            count += 1
###############################################################################################################################
    def runtime(data):
        runtime = data["Runtime (Minutes)"].tolist()
        genre = data["Genre"].tolist()
        dic = {}
        for i in range(len(runtime)):
            for j in genre[i].split(","):
                if j not in dic:
                    dic[j] = [runtime[i]]
                else:
                    dic[j] += [runtime[i]]
        graph_dic = {}
        for i in dic:
            graph_dic[i] = np.mean(dic[i])
        graph = pygal.Bar()
        graph.title = "ความยาวเฉลี่ยของภาพยนตร์ในแต่ละประเภท (2006-2016)"
        for i in sorted(graph_dic, key = lambda x: graph_dic[x], reverse=True):
            graph.add(i, graph_dic[i])
        graph.render_to_file("../Graph/runtime.svg")
        graph.render_to_file("../docs/assets/images/runtime.svg")
###############################################################################################################################
    def vote(data):
        vote = data["Votes"].tolist()
        genre = data["Genre"].tolist()
        year = data["Year"].tolist()
        dic = {}
        for i in range(len(vote)):
            for j in genre[i].split(","):
                if j not in dic:
                    dic[j] = vote[i]
                else:
                    dic[j] += vote[i]
        graph = pygal.Bar()
        graph.title = "ผล Vote รวมของภาพยนตร์แต่ละประเภท (2006-2016)"

        for i in sorted(dic, key = lambda x: dic[x], reverse=True):
            graph.add(i, dic[i])
        graph.render_to_file("../Graph/vote.svg")
        graph.render_to_file("../docs/assets/images/vote.svg")
        for i in range(2006, 2017):
            dic = {}
            for j in range(len(genre)):
                if year[j] == i:
                    for gen in genre[j].split(","):
                        if gen not in dic:
                            dic[gen] = vote[j]
                        else:
                            dic[gen] += vote[j]
            graph = pygal.Bar()
            graph.title = "ผลโหวตของภาพยนตร์ปี %d" %i
            for item in sorted(dic, key=lambda x:dic[x], reverse=True):
                graph.add(item, dic[item])
            graph.render_to_file("../Graph/vote%d.svg" %i)
            graph.render_to_file("../docs/assets/images/vote%d.svg" %i)
###############################################################################################################################
    def rating(data):
        rating = data["Rating"].tolist()
        genre = data["Genre"].tolist()
        dic = {}
        for i in range(len(rating)):
            for j in genre[i].split(","):
                if j not in dic:
                    dic[j] = [rating[i]]
                else:
                    dic[j] += [rating[i]]
        graph = pygal.Bar()
        graph.title = "Rating เฉลี่ยของภาพยนตร์แต่ละประเภทรวมทุกปี (2006-2016)"
        graph_dic = {}
        for i in dic:
            graph_dic[i] = np.mean(dic[i])
        for i in sorted(graph_dic, key = lambda x: graph_dic[x], reverse=True):
            graph.add(i, graph_dic[i])
        graph.render_to_file("../Graph/rating.svg")
        graph.render_to_file("../docs/assets/images/rating.svg")
###############################################################################################################################
    def word(data):
        description = data["Description"].tolist()
        text = ""
        for i in description:
            text += i
        popcorn = np.array(Image.open(path.join("../Picture/popcorn.png")))
        wordcloud = WordCloud(max_font_size=60, mask=popcorn,background_color="white").generate(text)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        wordcloud.to_file("../Wordcloud/all.png")
        wordcloud.to_file("../docs/assets/images/all.png")
        price = data["Revenue (Millions)"].tolist()
        text_more50 = ""
        text_less50 = ""
        for i in range(len(price)):
            if price[i] >= 50:
                text_more50 += description[i]
            else:
                text_less50 += description[i]
        popcorn = np.array(Image.open(path.join("../Picture/popcorn.png")))
        wordcloud = WordCloud(max_font_size=60, mask=popcorn,background_color="white").generate(text_more50)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        wordcloud.to_file("../Wordcloud/more50.png")
        wordcloud.to_file("../docs/assets/images/more50.png")
        popcorn = np.array(Image.open(path.join("../Picture/popcorn.png")))
        wordcloud = WordCloud(max_font_size=60, mask=popcorn,background_color="white").generate(text_less50)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        wordcloud.to_file("../Wordcloud/less50.png")
        wordcloud.to_file("../docs/assets/images/less50.png")
###############################################################################################################################
    def director(data):
        dic = {}
        direct = data["Director"].tolist()
        for i in direct:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        graph = pygal.Bar()
        graph.title = "ผู้กํากับที่กํากับภาพยนตร์ยอดนิยมทั้งหมดตั้งแต่ปี 2006 - 2016"
        count = 0
        for i in sorted(dic, key = lambda x: dic[x], reverse=True):
            graph.add(i, dic[i])
            count += 1
            if count == 11:
                break
        graph.render_to_file("../Graph/Director.svg")
        graph.render_to_file("../docs/assets/images/Director.svg")
####################################################################
