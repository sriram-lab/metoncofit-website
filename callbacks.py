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

from run_app import app, up, neut, down

# Create callbacks - unfortunately Dash only supports one output per callback, so I made three callbacks - same structure different heatmap.
