import plotly.express as px
import plotly.offline as pyo
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

ndf = pd.DataFrame(random_x, random_y, columns=['TC_NAME', 'Response_Time'])

fig = px.scatter(ndf, x="TC_NAME", y="Response_Time",
                title="Respose Times")
fig.update_layout(
    font_family="Courier New",
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green"
)

fig.update_xaxes(title_font_family="Arial")
# fig.show()

pyo.plot(fig, filename='line1.html')