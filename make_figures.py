import pandas as pd
import numpy as np
import json
import os

from _plotly_future_ import v4_subplots
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import chart_studio.plotly as py

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import flask

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'MetOncoFit'

base = os.path.dirname(os.path.abspath(__file__))
df = pd.read_json(base+'/data/db.json')

up = df.loc[(df["Type"] == "UPREGULATED") | (df["Type"] == "GAIN")
            ].sort_values(by="Gini", ascending=False)
neut = df.loc[(df["Type"] == "NEUTRAL") | (df["Type"] == "NEUT")
              ].sort_values(by="Gini", ascending=False)
down = df.loc[(df["Type"] == "DOWNREGULATED") | (
    df["Type"] == "LOSS")].sort_values(by="Gini", ascending=False)

dotplot = go.Scatter(
    x=up['Value'].values,
    y=up['Feature'],
    marker=dict(color="crimson", size=6),
    mode="markers",
)

barplot = go.Bar(
    x=up['Gini'].values,
    y=up["Feature"],
    orientation='h'
)

annotations = []


confusion_matr = go.Heatmap(
    x=None,
    y=None,
    z=None,
)

#fig = go.Figure()
#fig.add_trace(barplot)
fig = make_subplots(rows=1, cols=2,
                    shared_xaxes=False, shared_yaxes=True,
                    vertical_spacing=0.001
                    )
fig.add_trace(dotplot, row=1, col=1)
fig.add_trace(barplot, row=1, col=2)

app.layout = html.Div(
    dcc.Graph(
        figure=fig,
        config={
            'displayModeBar': False
            }
        )
    )

if __name__ == '__main__':
    app.run_server(debug=True)
