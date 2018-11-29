import pygal
import numpy as np
import pandas as pd
data = pd.read_csv("../IMDB-Movie-Data.csv")
def genre_graph(data):
    genre = data["Genre"].tolist()
    years = data["Year"].tolist()
    dic = {}
    for i in range(len(genre)):
        if years[i] == 2006:
            value = genre[i].split(",")
            for j in value:
                if j in dic:
                    dic[j] += 1
                else:
                    dic[j] = 1
    create_graph(dic)
def create_graph(dic):
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ของปี 2006 [44 เรื่อง]"
    for i in dic:
        graph.add(i, dic[i])
    graph.render_to_file("../Graph/2006.svg")
genre_graph(data)
