#######
# This plots 100 random data points (set the seed to 42 to
# obtain the same points we do!) between 1 and 100 in both
# vertical and horizontal directions.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import os

os.chdir("C:\\Temp\\jm\\digicon_results")
df = pd.read_csv("result.jtl")

np.random.seed(42)
random_x = df.label
random_y = df.success

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
)]

pyo.plot(data, filename='scatter_ds.html')
