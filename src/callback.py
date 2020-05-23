"""
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


def updateGenes(df, slider_choice):
    """
    """
    geneList = df['Gene'].unique().tolist()
    updatedGeneList = geneList[0:slider_choice]

    return updatedGeneList


def update_df(df, cancer_choice, prediction_choice, slider_choice):
    """
    update_df returns an updated dataframe that will be rendered.
    """
    updatedTargetDF = df[df['Target'] == prediction_choice]
    updatedCancerDF = updatedTargetDF[updatedTargetDF['Cancer']
                                      == cancer_choice]
    updatedGeneList = updateGenes(updatedCancerDF, slider_choice)
    updatedDF = updatedCancerDF.loc[updatedCancerDF['Gene'].isin(
        updatedGeneList)]
    finalDF = updatedDF.sort_values(['Gini', 'Value'], ascending=False)
    return finalDF


def make_customHoverbar(df):
    custom_hover = list()
    for _, row in df.iterrows():
        hover = \
            'Gene: '+'{}'.format(row['Gene']) + \
            '<br>'+'Feature: '+'{}'.format(row['Feature']) + \
            '<br>'+'Value: ' + '{0:.2f}'.format(row['Value']) + \
            '<br>'+'R: '+'{0:.2f}'.format(row['R'])
        custom_hover.append(hover)
    return custom_hover
