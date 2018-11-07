import pygal
import pandas as pd
import math
def main():
    """ Main Function Use to create all of graph """
    data = pd.read_csv("IMDB-Movie-Data.csv") # read data of movies with pandas
    graph1(data)
def graph1(data):
    """ Total Movie Sales in each years (2006 - 2016) """
    year = data["Year"].tolist() # get year
    revenue = data["Revenue (Millions)"].tolist() # get revenue
    dic_of_totalmoviesales = {} # create dic
    count = 0
    listed2 = []
    for i in year:
        if i not in dic_of_totalmoviesales and not math.isnan(revenue[count]):
            dic_of_totalmoviesales[i] = revenue[count]
        elif i in dic_of_totalmoviesales and not math.isnan(revenue[count]):
            dic_of_totalmoviesales[i] += revenue[count]
        count += 1
        listed2.append(i)
    listed = []
    for i in sorted(dic_of_totalmoviesales):
        listed.append(dic_of_totalmoviesales[i])

    graph = pygal.Line()
    graph.title = "กราฟรายได้ที่ได้จากการขายภาพยนต์ ของหนัง1000เรื่อง (Million US dollars)"
    graph.x_labels = map(str, range(2006, 2017))
    graph.add("", listed)
    graph.render_to_file("Graph of total revenue of movies sales in each year.svg")
    movies_of_each_years = {}
    for i in listed2:
        if i not in movies_of_each_years:
            movies_of_each_years[i] = 1
        else:
            movies_of_each_years[i] = movies_of_each_years[i] + 1
    listed3 = []
    for i in range(2006, 2017):
        listed3.append(listed2.count(i))
    graph2 = pygal.Bar()
    graph2.title = "กราฟอัตราการผลิตภาพยนต์จากทั้งหมด 1000 เรื่อง"
    graph2.x_labels = map(str, range(2006, 2017))
    graph2.add("", listed3)
    graph2.render_to_file("Graph of total movies pro in each year.svg")
main()
