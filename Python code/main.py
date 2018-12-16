from project_class import project
import pandas as pd
import time
start = time.time()
def main():
    """ create graph function """
    data = pd.read_csv("../IMDB-Movie-Data.csv") # read data
    print("Loading ......")
    project.genre_2006_2016(data) # create graph each years [2006-2016]
    project.genre_graph(data) # create graph all years [2006-2016]
    project.genre_price(data) # create graph price each + all years[2006-2016]
    project.runtime(data) # create average runtime graph all years [2006-2016]
    project.rating(data) # create average rating graph all years [2006-2016]
    project.vote(data) # create vote graph
    project.word(data) # generate wordcloud
    project.director(data) # create director graph
main()
print("Success!!  use: %s sec" %(time.time() - start))
