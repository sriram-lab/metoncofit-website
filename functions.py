"""
MetOncoFit Interactive explorer
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

df = pd.DataFrame()
colormap = []


def widget(data=df):
    """
    """
    # get values that will be used
    num_uniq_genes = data["Gene"].nunique()
    cancer_type = data["Cancer"].unique()
    prediction_type = data["Target"].unique()

    widgets = dbc.Container(
        [
            # Text that updates with slider values
            dbc.Row(
                html.Div(id='updatemode-output-container',
                         style={
                             'margin-top': 20,
                             'padding': '0px 20px 20px 20px'
                             }
                         )
                ),

            # Slider
            dbc.Row(
                [
                    html.Div(
                        dcc.Slider(
                            id='gene-slider',
                            min=1,
                            max=num_uniq_genes,
                            step=1,
                            value=25,
                            marks={
                                0: {'label': '0'},
                                100: {'label': '100'},
                                250: {'label': '250'},
                                500: {'label': '500'},
                                750: {'label': '750'},
                                num_uniq_genes: {'label': str(num_uniq_genes)}
                                },
                            updatemode='drag'
                            ),
                        style={'width': '50%', 'padding': '0px 20px 20px 20px'},
                        ),

                    # Dropdown menus
                    dbc.Col(
                        html.Div(
                            dcc.Dropdown(
                                id='cancer-type',
                                options=[{'label': i, 'value': i}
                                         for i in cancer_type],
                                value='Pan Cancer'
                                )
                            ),
                        width={"size": 3.0},

                        ),
                    dbc.Col(
                        html.Div(
                            dcc.Dropdown(
                                id='prediction-type',
                                options=[{'label': i, 'value': i}
                                         for i in prediction_type],
                                value='Differential Expression'
                                )
                            ),
                        width={"size": 3.0,
                               "offset": 0.3}
                        )
                    ]
                )
            ]
        )
    return widgets


def make_struct(hm_id='type-heatmap', data=df, nam='type', cmap=colormap):
    """
    """
    container = html.Div(
        dcc.Graph(
            id=hm_id,
            figure={
                'data': [(
                    go.Heatmap(
                        x=data['Gene'],
                        y=data['Feature'],
                        z=data['Value'],
                        name=nam,
                        colorscale=cmap)
                    )],
                'layout': go.Layout(
                    title=go.layout.Title(
                        text=('<b>Target label: '
                              + data['Type'].iloc[0]+'</b>'),
                        xanchor='right',
                        yanchor='bottom',
                        x=0,
                        font=dict(
                            family='Arial',
                            size=16,
                            color='black'
                            )
                        ),
                    autosize=False,
                    #width=1000,
                    yaxis=dict(
                        automargin=True,
                        tickfont=dict(
                            family='Arial, sans-serif',
                            size=14,
                            color='black'
                            )
                        )
                    )
                },
            config={
                'displayModeBar': False
                }
            )
        )
    return container
