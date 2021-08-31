import pandas as pd
import plotly.express as plex

reading = pd.read_csv('covidData.csv')
graph = plex.scatter(reading, x = "date", y = "cases", color = "country")

graph.show()