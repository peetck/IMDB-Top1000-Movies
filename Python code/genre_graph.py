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
    for i in genre_2:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    create_graph(dic)
def create_graph(dic):
    graph = pygal.Pie()
    graph.title = "ประเภทของหนังที่ได้รับความนิยม ตั้งแต่ปี 2006 - 2016 (1000 เรื่อง)"
    for i in dic:
        graph.add(i, dic[i])
    graph.render_to_file("../Graph/genre_graph.svg")
genre_graph(data)
