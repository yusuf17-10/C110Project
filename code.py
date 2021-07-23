import csv
import pandas as pd
import plotly.express as px
import math
import plotly.figure_factory as ff
import random
import statistics

df = pd.read_csv("medium.csv")
data = df ["reading_time"].tolist()
fig =ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()

population_mean = statistics.mean(data)
print("Mean = ",population_mean)
population_standarddeveation = statistics.stdev(data)
print("Standard Deveation = ",population_standarddeveation)



datalsit = []
for i in range(0,1000):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean  =statistics.mean(dataset)
print(" Mean of 1000 values",mean)
print("standard deveation of 1000 values",standarddeveation)