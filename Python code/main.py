from project_class import project
import pandas as pd
import time
start = time.time()
def main():
    data = pd.read_csv("../IMDB-Movie-Data.csv")

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
print("Success!!  use: %s sec" %(time.time() - start))