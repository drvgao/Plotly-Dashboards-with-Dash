from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Analysis of the restaurant sales'),
    dcc.Graph(id="pie-charts-x-graph"),
    html.P("Names:"),
    dcc.Dropdown(id='pie-charts-x-names',
        options=['Total Scenarios', 'Total TCs'],
        value='Total Scenarios', clearable=False
    ),
    html.P("Values:"),
    dcc.Dropdown(id='pie-charts-x-values',
        options=['Total Scenarios', 'Total Scenarios'],
        value='Total TCs', clearable=False
    ),
])


@app.callback(
    Output("pie-charts-x-graph", "figure"), 
    Input("pie-charts-x-names", "value"), 
    Input("pie-charts-x-values", "value"))
def generate_chart(names, values):
    df = pd.read_excel('../Data/TestCoverage.xlsx') #, index_col=[0]
    print(df.sample(2))
    fig = px.pie(df, values=values, names='Feature', hole=.3)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
