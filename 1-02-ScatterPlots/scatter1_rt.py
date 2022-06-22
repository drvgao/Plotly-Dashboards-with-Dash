#######
# This plots 100 random data points (set the seed to 42 to
# obtain the same points we do!) between 1 and 100 in both
# vertical and horizontal directions.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import os, re

os.chdir("C:\\Temp\\jm\\digicon_results")
elapsed_list = []
# pyo.plot(data, filename='scatter_ds.html')
def remove_suite_name(tc_name="default-tc"):
    # print('tc_name_with_no: before', tc_name)
    pattern = r'\[TG\]-.*\[TC\]-'  # remove prefix from test case name
    try:
        if tc_name.find('[TG]') != -1:
            tc_name = re.sub(pattern, '', tc_name)
            tc_name_with_no = str(tc_name)[:2]
            print('tc_name_with_no', tc_name)
            elapsed_list.append(tc_name)
    except ValueError:
        pass

df = pd.read_csv("result.jtl")
label_ed = pd.Series(df.label)
label_ed = label_ed.apply(remove_suite_name)

np.random.seed(42)
random_x = label_ed
random_y = df.elapsed

data = [go.Scatter(
    x = elapsed_list,
    y = random_y,
    mode = 'lines+markers',
    name = 'lines+markers'
)]
layout = go.Layout(
    title = 'Line chart showing three different modes'
)
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='line1.html')
