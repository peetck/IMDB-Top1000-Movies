import pygal
import pandas as pd
data = pd.read_csv("../IMDB-Movie-Data.csv")

def runtime(data):
    runtime = data["Runtime (Minutes)"].tolist()
    dic = {"60-80":0, "80-100":0, "100-120":0, "120-140":0, "140-160":0, "160-180":0, "180+":0}
    for i in runtime:
        if i >= 60 and i < 80:
            dic["60-80"] += 1
        elif i >= 80 and i < 100:
            dic["80-100"] += 1
        elif i >= 100 and i < 120:
            dic["100-120"] += 1
        elif i >= 120 and i < 140:
            dic["120-140"] += 1
        elif i >= 140 and i < 160:
            dic["140-160"] += 1
        elif i >= 160 and i < 180:
            dic["160-180"] += 1
        elif i >= 180:
            dic["180+"] += 1
    graph = pygal.Bar()
    graph.title = "Runtime"
    graph.x_labels = ["60-80", "81-100", "101-120", "121-140", "141-160", "161-180", "180+"]
    graph.add("", [dic["60-80"], dic["80-100"], dic["100-120"], dic["120-140"], dic["140-160"], dic["160-180"], dic["180+"]])
    graph.render_to_file("../Graph/runtime.svg")
runtime(data)