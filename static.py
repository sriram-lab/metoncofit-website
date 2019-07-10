"""
MetOncoFit Interactive explorer static
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


def header():
    """
    """
    body = dbc.Container(
        dbc.Row(
            [
                dbc.Col([
                    html.Div([
                        html.H1("MetOncoFit")
                        ], style={'marginTop': 30, 'marginBottom': 30}),
                    html.Div([
                        html.P(
                            """
                        MetOncoFit is a machine learning approach that uses biochemical and metabolic attributes to predict tumor differential expression, copy number variation, and patient survival.
                        """
                            )
                        ], style={'marginTop': 30, 'marginBottom': 30}),
                    html.Div([
                        html.H2("Introduction"),
                        html.P(
                            """
                        Tumors reprogram normal cellular metabolism to support uncontrolled proliferation. While some of these metabolic reprogramming strategies are common across most tumors, such as the Warburg effect, there must be diverse metabolic objectives that contribute to tumor heterogeneity.

                        We hypothesized that cancer cells have few key changes in the metabolic network, and examined frequently dysregulated metabolic genes using a multi-scale systems biology approach to determine commone features that contribute to metabolic dysregulation in tumors.

                        """
                            )
                        ], style={'marginTop': 30, 'marginBottom': 30}),
                    html.Div([
                        html.H4("Installing and Using the MetOncoFit approach"),
                        html.P(
                            """
                        The MetOncoFit interactive explorer shows the top 10 features predicted by MetOncoFit and the feature values with respect to each gene. All 10 cancer models and their predictions for differential expression, copy number variation, and patient survival are in this explorer.
                        """),
                        html.P(
                            """
                        """
                            ),
                        html.P(
                            """
                        To download the source code, please visit out GitHub respository: https://github.com/sriram-lab/MetOncoFit.To support the MetOncoFit project, you can cite our publication:
                        """
                            ),
                        html.P(
                            """
                        """
                            ),
                        html.P(
                            """
                        Oruganty, K., Campit, S.E., Mamde, S., & Chandrasekaran, S. Common biochemical and topological attributes of metabolic genes recurrently dysregulated in tumors.
                        """
                            )
                        ], style={'marginTop': 30, 'marginBottom': 30}),
                    html.Div([
                        html.H4("MetOncoFit interactive explorer"),
                        ])
                    ])
                ]
            )
        )
    return body
