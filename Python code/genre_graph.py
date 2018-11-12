import pygal
import pandas as pd
data = pd.read_csv("../IMDB-Movie-Data.csv")
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
    create_graph(dic, dic2)
def create_graph(dic, dic2):
    graph = pygal.Bar()
    graph.title = "ประเภทของหนัง ตั้งแต่ปี 2006 - 2016"
    value = []
    for i in sorted(dic.values())[::-1]:
        graph.add(dic2[i], i)
    graph.render_to_file("../Graph/genre_graph.svg")
genre_graph(data)
