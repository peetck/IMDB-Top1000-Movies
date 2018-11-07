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
    for i in year:
        if i not in dic_of_totalmoviesales and not math.isnan(revenue[count]):
            dic_of_totalmoviesales[i] = revenue[count]
        elif i in dic_of_totalmoviesales and not math.isnan(revenue[count]):
            dic_of_totalmoviesales[i] += revenue[count]
        count += 1
    listed = []
    for i in sorted(dic_of_totalmoviesales):
        listed.append(dic_of_totalmoviesales[i])
    graph = pygal.Line()
    graph.title = "Graph of Movie revenue in each years (million) (US dollars)"
    graph.x_labels = map(str, range(2006, 2017))
    graph.add("Revenue", listed)
    graph.render_to_file("Graph of total movies sales in each year.svg")
main()
