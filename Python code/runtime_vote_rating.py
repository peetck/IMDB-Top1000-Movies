import pygal
import pandas as pd
import numpy as np
data = pd.read_csv("../IMDB-Movie-Data.csv")
def runtime(data):
    runtime = data["Runtime (Minutes)"].tolist()
    runtime = [int(i) for i in runtime]
    runtime_mean = np.average(runtime)
    runtime_sd = np.std(runtime)
    runtime_highest = np.max(runtime)
    graph = pygal.Bar()
    graph.title = "Runtime [IMDB Top 1000 Movies (2006 - 2016)]"
    graph.x_labels = ["Highest", "Median", "Standard Division"]
    graph.add("Runtime", [runtime_highest, runtime_mean, runtime_sd])
    graph.render_to_file("../Graph/runtime.svg")
def vote(data):
    vote = data["Votes"].tolist()
    vote = [int(i) for i in vote]
    vote_mean = np.average(vote)
    vote_sd = np.std(vote)
    vote_highest = np.max(vote)
    graph = pygal.Bar()
    graph.title = "Vote [IMDB Top 1000 Movies (2006 - 2016)]"
    graph.x_labels = ["Highest", "Median", "Standard Division"]
    graph.add("", [vote_highest, vote_mean, vote_sd])
    graph.render_to_file("../Graph/vote.svg")
def rating(data):
    rating = data["Rating"].tolist()
    rating = [int(i) for i in rating]
    rating_mean = np.average(rating)
    rating_sd = np.std(rating)
    rating_highest = np.max(rating)
    graph = pygal.Bar()
    graph.title = "Rating [IMDB Top 1000 Movies (2006 - 2016)]"
    graph.x_labels = ["Highest", "Median", "Standard Division"]
    graph.add("", [rating_highest, rating_mean, rating_sd])
    graph.render_to_file("../Graph/rating.svg")
runtime(data)
rating(data)
vote(data)
