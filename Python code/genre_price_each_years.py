import pygal
import pandas as pd
data = pd.read_csv("../IMDB-Movie-Data.csv")
def genre_price(data):
    genre = data["Genre"].tolist()
    revenue = data["Revenue (Millions)"].tolist()
    year = data["Year"].tolist()
    genre_reduce = []
    for i in genre:
        check = i.split(",")
        genre_reduce.append(check[0])
    dic_2006, dic_2007, dic_2008, dic_2009, dic_2010\
    , dic_2011, dic_2012, dic_2013, dic_2014, dic_2015\
    , dic_2016 = {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0}, \
    {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0}, \
    {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0}, \
    {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0}, \
    {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0}, \
    {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0}, \
    {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0}\
    , {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0}, \
    {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0}, \
    {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0}, \
    {"Romance":0, "Mystery":0, "Thriller":0, "Sci-Fi":0, "Fantasy":0}
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
    create_graph(dic_2006, dic_2007, dic_2008, dic_2009, dic_2010\
    , dic_2011, dic_2012, dic_2013, dic_2014, dic_2015\
    , dic_2016)
def create_graph(dic_2006, dic_2007, dic_2008, dic_2009, dic_2010\
    , dic_2011, dic_2012, dic_2013, dic_2014, dic_2015\
    , dic_2016):
    graph = pygal.StackedBar()
    graph.title = "รายได้จากการขายหนังแต่ละประเภทในแต่ละปี (2006 - 2016) #US-Dollars"
    graph.x_labels = map(str, range(2006, 2017))
    graph.add("Animation", [dic_2006["Action"], dic_2007["Action"], dic_2008["Action"], dic_2009["Action"], dic_2010["Action"], dic_2011["Action"], dic_2012["Action"]\
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
genre_price(data)