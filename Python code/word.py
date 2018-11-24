#!/usr/bin/env python
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from wordcloud import WordCloud
data = pd.read_csv("../IMDB-Movie-Data.csv")
def word(data):
    description = data["Description"].tolist()
    text = ""
    for i in description:
        text += i
    wine = np.array(Image.open(path.join("../Picture/wine.png")))
    wordcloud = WordCloud(max_font_size=60, mask=wine,background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    wordcloud.to_file("../Wordcloud/all.png")

    price = data["Revenue (Millions)"].tolist()
    text_more50 = ""
    text_less50 = ""
    for i in range(len(price)):
        if price[i] >= 50:
            text_more50 += description[i]
        else:
            text_less50 += description[i]

    wine = np.array(Image.open(path.join("../Picture/wine.png")))
    wordcloud = WordCloud(max_font_size=60, mask=wine,background_color="white").generate(text_more50)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    wordcloud.to_file("../Wordcloud/more50.png")

    wine = np.array(Image.open(path.join("../Picture/wine.png")))
    wordcloud = WordCloud(max_font_size=60, mask=wine,background_color="white").generate(text_less50)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    wordcloud.to_file("../Wordcloud/less50.png")

word(data)
