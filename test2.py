import callbacks
"""
MetOncoFit Interactive explorer

This application was built with a Flask framework using Dash and Plotly. The explorer shows three heatmaps that shows the top 10 features predicted by MetOncoFit on the y-axis, the genes corresponding to the feature predictions on the x-axis, and each cell is the corresponding gene-feature value.

@author: Scott Campit
"""
import pandas as pd
import numpy as np
import json

from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import flask

import static
import functions
import callbacks
import col

# Intialize the Flask/Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'MetOncoFit'

# Read in data
df = pd.read_json('db.json')

# Create dataframes to parse data into three heat maps
up = df.loc[(df["Type"] == "UPREGULATED") | (df["Type"] == "GAIN")]
up = up.sort_values(by="Gini", ascending=False)
neut = df.loc[(df["Type"] == "NEUTRAL") | (df["Type"] == "NEUT")]
neut = neut.sort_values(by="Gini", ascending=False)
down = df.loc[(df["Type"] == "DOWNREGULATED") | (df["Type"] == "LOSS")]
down = down.sort_values(by="Gini", ascending=False)

colormap = col.Choose_Gradient('blue')

# Will be rendered as HTML. Description of the algorithm.
_body = static.header()

# Create dynamic parts that will allow client to interact with data
_widgets = functions.widget(data=df)

up_heatmap = functions.make_struct(
    hm_id='up-heatmap', data=up, nam='up', cmap=colormap)
neut_heatmap = functions.make_struct(
    hm_id='neut-heatmap', data=neut, nam='neut', cmap=colormap)
down_heatmap = functions.make_struct(
    hm_id='down-heatmap', data=down, nam='down', cmap=colormap)

# Initialize the application
app.layout = html.Div(
                      [_body,
                       _widgets,
                       up_heatmap,
                       neut_heatmap,
                       down_heatmap
                       ]
                      )

# For server
#server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
