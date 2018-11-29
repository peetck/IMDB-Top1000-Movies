import pygal
import numpy as np
import pandas as pd
data = pd.read_csv("../IMDB-Movie-Data.csv")
def genre_06(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic_06 = {}
    for i in range(len(genre)):
        if years[i] == 2006:
            value = genre[i].split(",")
            for j in value:
                if j in dic_06:
                    dic_06[j] += 1
                else:
                    dic_06[j] = 1
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2006 [44 เรื่อง]"
    for i in dic_06:
        graph.add(i, dic_06[i])
    graph.render_to_file("../Graph/2006.svg")
genre_06(data)
def genre_07(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic_07 = {}
    for i in range(len(genre)):
        if years[i] == 2007:
            value = genre[i].split(",")
            for j in value:
                if j in dic_07:
                    dic_07[j] += 1
                else:
                    dic_07[j] = 1
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2007 [53 เรื่อง]"
    for i in dic_07:
        graph.add(i, dic_07[i])
    graph.render_to_file("../Graph/2007.svg")
genre_07(data)
def genre_08(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic_08 = {}
    for i in range(len(genre)):
        if years[i] == 2008:
            value = genre[i].split(",")
            for j in value:
                if j in dic_08:
                    dic_08[j] += 1
                else:
                    dic_08[j] = 1
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2008 [52 เรื่อง]"
    for i in dic_08:
        graph.add(i, dic_08[i])
    graph.render_to_file("../Graph/2008.svg")
genre_08(data)
def genre_09(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic_09 = {}
    for i in range(len(genre)):
        if years[i] == 2009:
            value = genre[i].split(",")
            for j in value:
                if j in dic_09:
                    dic_09[j] += 1
                else:
                    dic_09[j] = 1
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2009 [51 เรื่อง]"
    for i in dic_09:
        graph.add(i, dic_09[i])
    graph.render_to_file("../Graph/2009.svg")
genre_09(data)
def genre_10(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic_10 = {}
    for i in range(len(genre)):
        if years[i] == 2010:
            value = genre[i].split(",")
            for j in value:
                if j in dic_10:
                    dic_10[j] += 1
                else:
                    dic_10[j] = 1
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2010 [60 เรื่อง]"
    for i in dic_10:
        graph.add(i, dic_10[i])
    graph.render_to_file("../Graph/2010.svg")
genre_10(data)
def genre_11(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic_11 = {}
    for i in range(len(genre)):
        if years[i] == 2011:
            value = genre[i].split(",")
            for j in value:
                if j in dic_11:
                    dic_11[j] += 1
                else:
                    dic_11[j] = 1
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2011 [63 เรื่อง]"
    for i in dic_11:
        graph.add(i, dic_11[i])
    graph.render_to_file("../Graph/2011.svg")
genre_11(data)
def genre_12(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic_12 = {}
    for i in range(len(genre)):
        if years[i] == 2012:
            value = genre[i].split(",")
            for j in value:
                if j in dic_12:
                    dic_12[j] += 1
                else:
                    dic_12[j] = 1
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2012 [64 เรื่อง]"
    for i in dic_12:
        graph.add(i, dic_12[i])
    graph.render_to_file("../Graph/2012.svg")
genre_12(data)
def genre_13(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic_13 = {}
    for i in range(len(genre)):
        if years[i] == 2013:
            value = genre[i].split(",")
            for j in value:
                if j in dic_13:
                    dic_13[j] += 1
                else:
                    dic_13[j] = 1
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2013 [91 เรื่อง]"
    for i in dic_13:
        graph.add(i, dic_13[i])
    graph.render_to_file("../Graph/2013.svg")
genre_13(data)
def genre_14(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic_14 = {}
    for i in range(len(genre)):
        if years[i] == 2014:
            value = genre[i].split(",")
            for j in value:
                if j in dic_14:
                    dic_14[j] += 1
                else:
                    dic_14[j] = 1
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2014 [98 เรื่อง]"
    for i in dic_14:
        graph.add(i, dic_14[i])
    graph.render_to_file("../Graph/2014.svg")
genre_14(data)
def genre_15(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic_15 = {}
    for i in range(len(genre)):
        if years[i] == 2015:
            value = genre[i].split(",")
            for j in value:
                if j in dic_15:
                    dic_15[j] += 1
                else:
                    dic_15[j] = 1
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2015 [127 เรื่อง]"
    for i in dic_15:
        graph.add(i, dic_15[i])
    graph.render_to_file("../Graph/2015.svg")
genre_15(data)
def genre_16(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic_16 = {}
    for i in range(len(genre)):
        if years[i] == 2016:
            value = genre[i].split(",")
            for j in value:
                if j in dic_16:
                    dic_16[j] += 1
                else:
                    dic_16[j] = 1
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2016 [297 เรื่อง]"
    for i in dic_16:
        graph.add(i, dic_16[i])
    graph.render_to_file("../Graph/2016.svg")
genre_16(data)
