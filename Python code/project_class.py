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
            graph.title = "ประเภทของหนัง ของปี %d [%d เรื่อง]" %(ye,count)
            for i in sorted(dic, key = lambda x: dic[x], reverse=True):
                graph.add(i, dic[i])
            graph.render_to_file("../Graph/%d.svg" %ye)
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
        graph.title = "ประเภทของหนัง ตั้งแต่ปี 2006 - 2016"
        value = []
        for i in sorted(dic.values())[::-1]:
            graph.add(dic2[i], i)
        graph.render_to_file("../Graph/genre_graph.svg")
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
        dic_2006, dic_2007, dic_2008, dic_2009, dic_2010\
        , dic_2011, dic_2012, dic_2013, dic_2014, dic_2015\
        , dic_2016 = {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}, \
        {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}, \
        {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}, \
        {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}, \
        {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}, \
        {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}, \
        {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}\
        , {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}, \
        {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}, \
        {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}, \
        {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0, "Animation":0, "Biography":0}
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
        graph = pygal.Line()
        graph.title = "รายได้จากการขายหนังแต่ละประเภท (US-Dollars)"
        graph.x_labels = map(str, range(2006, 2017))
        graph.add("Action", [dic_2006["Action"], dic_2007["Action"], dic_2008["Action"], dic_2009["Action"], dic_2010["Action"], dic_2011["Action"], dic_2012["Action"]\
            , dic_2013["Action"], dic_2014["Action"], dic_2015["Action"], dic_2016["Action"]])
        graph.add("Adventure", [dic_2006["Adventure"], dic_2007["Adventure"], dic_2008["Adventure"], dic_2009["Adventure"], dic_2010["Adventure"], dic_2011["Adventure"], dic_2012["Adventure"]\
            , dic_2013["Adventure"], dic_2014["Adventure"], dic_2015["Adventure"], dic_2016["Adventure"]])
        graph.add("Horror", [dic_2006["Horror"], dic_2007["Horror"], dic_2008["Horror"], dic_2009["Horror"], dic_2010["Horror"], dic_2011["Horror"], dic_2012["Horror"]\
            , dic_2013["Horror"], dic_2014["Horror"], dic_2015["Horror"], dic_2016["Horror"]])
        graph.add("Animation", [dic_2006["Animation"], dic_2007["Animation"], dic_2008["Animation"], dic_2009["Animation"], dic_2010["Animation"], dic_2011["Animation"], dic_2012["Animation"]\
            , dic_2013["Animation"], dic_2014["Animation"], dic_2015["Animation"], dic_2016["Animation"]])
        graph.add("Comedy", [dic_2006["Comedy"], dic_2007["Comedy"], dic_2008["Comedy"], dic_2009["Comedy"], dic_2010["Comedy"], dic_2011["Comedy"], dic_2012["Comedy"]\
            , dic_2013["Comedy"], dic_2014["Comedy"], dic_2015["Comedy"], dic_2016["Comedy"]])
        graph.add("Biography", [dic_2006["Biography"], dic_2007["Biography"], dic_2008["Biography"], dic_2009["Biography"], dic_2010["Biography"], dic_2011["Biography"], dic_2012["Biography"]\
            , dic_2013["Biography"], dic_2014["Biography"], dic_2015["Biography"], dic_2016["Biography"]])
        graph.add("Drama", [dic_2006["Drama"], dic_2007["Drama"], dic_2008["Drama"], dic_2009["Drama"], dic_2010["Drama"], dic_2011["Drama"], dic_2012["Drama"]\
            , dic_2013["Drama"], dic_2014["Drama"], dic_2015["Drama"], dic_2016["Drama"]])
        graph.add("Crime", [dic_2006["Crime"], dic_2007["Crime"], dic_2008["Crime"], dic_2009["Crime"], dic_2010["Crime"], dic_2011["Crime"], dic_2012["Crime"]\
            , dic_2013["Crime"], dic_2014["Crime"], dic_2015["Crime"], dic_2016["Crime"]])
        graph.add("Romance", [dic_2006["Romance"], dic_2007["Romance"], dic_2008["Romance"], dic_2009["Romance"], dic_2010["Romance"], dic_2011["Romance"], dic_2012["Romance"]\
            , dic_2013["Romance"], dic_2014["Romance"], dic_2015["Romance"], dic_2016["Romance"]])
        graph.add("Mystery", [dic_2006["Mystery"], dic_2007["Mystery"], dic_2008["Mystery"], dic_2009["Mystery"], dic_2010["Mystery"], dic_2011["Mystery"], dic_2012["Mystery"]\
            , dic_2013["Mystery"], dic_2014["Mystery"], dic_2015["Mystery"], dic_2016["Mystery"]])
        graph.add("Thriller", [dic_2006["Thriller"], dic_2007["Thriller"], dic_2008["Thriller"], dic_2009["Thriller"], dic_2010["Thriller"], dic_2011["Thriller"], dic_2012["Thriller"]\
            , dic_2013["Thriller"], dic_2014["Thriller"], dic_2015["Thriller"], dic_2016["Thriller"]])
        graph.add("Sci-Fi", [dic_2006["Sci-Fi"], dic_2007["Sci-Fi"], dic_2008["Sci-Fi"], dic_2009["Sci-Fi"], dic_2010["Sci-Fi"], dic_2011["Sci-Fi"], dic_2012["Sci-Fi"]\
            , dic_2013["Sci-Fi"], dic_2014["Sci-Fi"], dic_2015["Sci-Fi"], dic_2016["Sci-Fi"]])
        graph.add("Fantasy", [dic_2006["Fantasy"], dic_2007["Fantasy"], dic_2008["Fantasy"], dic_2009["Fantasy"], dic_2010["Fantasy"], dic_2011["Fantasy"], dic_2012["Fantasy"]\
            , dic_2013["Fantasy"], dic_2014["Fantasy"], dic_2015["Fantasy"], dic_2016["Fantasy"]])
        graph.render_to_file("../Graph/genre_price_each_years.svg")
    def runtime(data):
        runtime = data["Runtime (Minutes)"].tolist()
        genre = data["Genre"].tolist()
        dic = {}
        for i in range(len(runtime)):
            for j in genre[i].split(","):
                if j not in dic:
                    dic[j] = runtime[i]
                else:
                    if runtime[i] > dic[j]:
                        dic[j] = runtime[i]
        graph = pygal.Bar()
        graph.title = "Runtime [IMDB Top 1000 Movies (2006 - 2016)]"
        for i in sorted(dic, key = lambda x: dic[x], reverse=True):
            graph.add(i, dic[i])
        graph.render_to_file("../Graph/runtime.svg")
    def vote(data):
        vote = data["Votes"].tolist()
        genre = data["Genre"].tolist()
        dic = {}
        for i in range(len(vote)):
            for j in genre[i].split(","):
                if j not in dic:
                    dic[j] = vote[i]
                else:
                    dic[j] += vote[i]
        graph = pygal.Bar()
        graph.title = "Vote [IMDB Top 1000 Movies (2006 - 2016)]"

        for i in sorted(dic, key = lambda x: dic[x], reverse=True):
            graph.add(i, dic[i])
        graph.render_to_file("../Graph/vote.svg")
    def rating(data):
        rating = data["Rating"].tolist()
        genre = data["Genre"].tolist()
        dic = {}
        for i in range(len(rating)):
            for j in genre[i].split(","):
                if j not in dic:
                    dic[j] = rating[i]
                else:
                    dic[j] += rating[i]
        graph = pygal.Bar()
        graph.title = "Rating [IMDB Top 1000 Movies (2006 - 2016)]"

        for i in sorted(dic, key = lambda x: dic[x], reverse=True):
            graph.add(i, dic[i])
        graph.render_to_file("../Graph/rating.svg")

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

        popcorn = np.array(Image.open(path.join("../Picture/popcorn.png")))
        wordcloud = WordCloud(max_font_size=60, mask=popcorn,background_color="white").generate(text_less50)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        wordcloud.to_file("../Wordcloud/less50.png")
