from project_class import project
import pandas as pd
def main():
    data = pd.read_csv("../IMDB-Movie-Data.csv")
    print("***************************************")
    print("Listed of graph")
    print("1.genre 2010 - 2016 [each years]")
    print("2.genre 2010 - 2016 [all]")
    print("3.revenue [all]")
    print("4.Rating, runtime, vote, director")
    print("5.Wordcloud")
    print("6.All")
    inp = int(input("Choose What graph you want to create: "))
    if inp == 1:
        print("Loading ......")
        project.genre_2006_2016(data)
    elif inp == 2:
        print("Loading ......")
        project.genre_graph(data)

    elif inp == 3:
        print("Loading ......")
        project.genre_price(data)

    elif inp == 4:
        print("Loading ......")
        project.runtime(data)
        project.rating(data)
        project.vote(data)
        project.director(data)
    elif inp == 5:
        print("Loading ......")
        project.word(data)

    elif inp == 6:
        print("Loading ......")
        project.genre_2006_2016(data)
        project.genre_graph(data)
        project.genre_price(data)
        project.runtime(data)
        project.rating(data)
        project.vote(data)
        project.word(data)
        project.director(data)
main()
print("Success!!")