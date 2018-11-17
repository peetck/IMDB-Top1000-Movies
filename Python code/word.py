from os import path
from PIL import Image
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("../IMDB-Movie-Data.csv")
def word(data):
    data = data["Description"].tolist()
    text = ""
    for i in data:
        text += i
    wine = np.array(Image.open(path.join("../Picture/wine.png")))
    wordcloud = WordCloud(max_font_size=40, mask=wine,background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    wordcloud.to_file("../Wordcloud/all.png")
word(data)
