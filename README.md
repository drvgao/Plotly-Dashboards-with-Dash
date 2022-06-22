# Plotly-Dashboards-with-Dash

## Welcome to the course repo!

Do you want to learn how to create amazing dashboards with Python, Plotly, and
Dash?

# Dash Notes

Dash has three major components 1. Dash components 2. html components 3. dcc core components

## Dash flow

    1. create the flask app  ```app = dash.Dash()```
    2. create dash layout
        1. Layout contains html and dash core components.
        2. dcc.Graph is one for plotly graphs
            1. dcc.Graph(id, figure={data, layout})
