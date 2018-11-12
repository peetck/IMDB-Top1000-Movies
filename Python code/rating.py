import pygal
import pandas as pd
data = pd.read_csv("../IMDB-Movie-Data.csv")

def rating(data):
    rating = data["Rating"].tolist()
    dic = {"0-2":0, "2-4":0, "4-6":0, "6-8":0, "8-10":0}
    for i in rating:
        if i >= 0 and i < 2:
            dic["0-2"] += 1
        elif i >= 2 and i < 4:
            dic["2-4"] += 1
        elif i >= 4 and i < 6:
            dic["4-6"] += 1
        elif i >= 6 and i < 8:
            dic["6-8"] += 1
        elif i >= 8 and i < 10:
            dic["8-10"] += 1
    graph = pygal.Bar()
    graph.title = "rating"
    graph.x_labels = ["0-2", "2-4", "4-6", "6-8", "8-10"]
    graph.add("", [dic["0-2"], dic["2-4"], dic["4-6"], dic["6-8"], dic["8-10"]])
    graph.render_to_file("../Graph/rating.svg")
rating(data)