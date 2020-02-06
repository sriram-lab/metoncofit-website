"""
MetOncoFit Interactive explorer

This application was built with a Flask framework using Dash and Plotly. The explorer shows three heatmaps that shows the top 10 features predicted by MetOncoFit on the y-axis, the genes corresponding to the feature predictions on the x-axis, and each cell is the corresponding gene-feature value.

@author: Scott Campit
"""
import pandas as pd
import numpy as np
import json, os

from plotly import tools
import chart_studio.plotly as py
import plotly.graph_objs as go

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import flask

import metoncofit.static
import metoncofit.functions
#import callbacks
import metoncofit.col

# Intialize the Flask/Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'MetOncoFit'

# Read in data
base = os.path.dirname(os.path.abspath(__file__))
df = pd.read_json(base+'/data/db.json')

# Create dataframes to parse data into three heat maps
up = df.loc[(df["Type"] == "UPREGULATED") | (df["Type"] == "GAIN")]
up = up.sort_values(by="Gini", ascending=False)

neut = df.loc[(df["Type"] == "NEUTRAL") | (df["Type"] == "NEUT")]
neut = neut.sort_values(by="Gini", ascending=False)

down = df.loc[(df["Type"] == "DOWNREGULATED") | (df["Type"] == "LOSS")]
down = down.sort_values(by="Gini", ascending=False)

colormap = metoncofit.col.Choose_Gradient('red')

# Text describing MetOncoFit
_body = metoncofit.static.header()

# Create dynamic parts that will allow client to interact with data
_widgets = metoncofit.functions.widget(data=df)

up_heatmap = metoncofit.functions.make_struct(
    hm_id='up-heatmap', data=up, nam='up', cmap=colormap)
neut_heatmap = metoncofit.functions.make_struct(
    hm_id='neut-heatmap', data=neut, nam='neut', cmap=colormap)
down_heatmap = metoncofit.functions.make_struct(
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


@app.callback(
    dash.dependencies.Output('up-heatmap', 'figure'),
    [dash.dependencies.Input('cancer-type', 'value'),
     dash.dependencies.Input('prediction-type', 'value'),
     dash.dependencies.Input('gene-slider', 'value')])
def update_up(cancer_choice, prediction_choice, slider_choice):
    up_df = up[up['Target'] == prediction_choice]
    up_df = up_df[up_df['Cancer'] == cancer_choice]
    up_tmp = up_df['Gene'].unique().tolist()
    up_tmp = up_tmp[0:slider_choice]
    up_df = up_df.loc[up_df['Gene'].isin(up_tmp)]
    up_df = up_df.sort_values(['Gini', 'Value'], ascending=False)

    custom_hover = []
    for _, i in up_df.iterrows():
        dat = 'Gene: '+'{}'.format(i['Gene'])+'<br>'+'Feature: '+'{}'.format(i['Feature']) + \
                                   '<br>'+'Value: ' + \
                                       '{0:.2f}'.format(
                                           i['Value'])+'<br>'+'R: '+'{0:.2f}'.format(i['R'])
        custom_hover.append(dat)

    return {
        'data': [(
            go.Heatmap(
                x=up_df['Gene'],
                y=up_df['Feature'],
                z=up_df['Value'],
                name='up-heatmap',
                colorscale=colormap,
                text=custom_hover,
                hoverinfo='text')
                )],
        'layout': go.Layout(
            title=go.layout.Title(
                text=('<b>Target label: '+up_df['Type'].iloc[0]+'</b>'),
                xanchor='left',
                yanchor='bottom',
                x=0.47,
                font=dict(
                    family='Arial',
                    size=16,
                    color='black'
                    )
                ),
            autosize=False,
            yaxis=dict(
                automargin=True,
                autorange='reversed',
                tickfont=dict(
                    family='Arial, sans-serif',
                    size=14,
                    color='black',
                    )
                )
            )
        }


@app.callback(
    dash.dependencies.Output('neut-heatmap', 'figure'),
    [dash.dependencies.Input('cancer-type', 'value'),
     dash.dependencies.Input('prediction-type', 'value'),
     dash.dependencies.Input('gene-slider', 'value')])
def update_neut(cancer_choice, prediction_choice, slider_choice):
    neut_df = neut[neut['Target'] == prediction_choice]
    neut_df = neut_df[neut_df['Cancer'] == cancer_choice]
    neut_tmp = neut_df['Gene'].unique().tolist()
    neut_tmp = neut_tmp[0:slider_choice]
    neut_df = neut_df.loc[neut_df['Gene'].isin(neut_tmp)]
    neut_df = neut_df.sort_values(['Gini', 'Value'], ascending=False)

    custom_hover = []
    for _, i in neut_df.iterrows():
        dat = 'Gene: '+'{}'.format(i['Gene'])+'<br>'+'Feature: '+'{}'.format(i['Feature']) + \
                                   '<br>'+'Value: ' + \
                                       '{0:.2f}'.format(
                                           i['Value'])+'<br>'+'R: '+'{0:.2f}'.format(i['R'])
        custom_hover.append(dat)

    return {
        'data': [(
            go.Heatmap(
                x=neut_df['Gene'],
                y=neut_df['Feature'],
                z=neut_df['Value'],
                name='neut-heatmap',
                colorscale=colormap,
                text=custom_hover,
                hoverinfo='text')
                )],
        'layout': go.Layout(
            title=go.layout.Title(
                text=('<b>Target label: '+neut_df['Type'].iloc[0]+'</b>'),
                xanchor='left',
                yanchor='bottom',
                x=0.47,
                font=dict(
                    family='Arial',
                    size=16,
                    color='black'
                    )
                ),
            autosize=False,
            yaxis=dict(
                automargin=True,
                autorange='reversed',
                tickfont=dict(
                    family='Arial, sans-serif',
                    size=14,
                    color='black',
                    )
                )
            )
        }


@app.callback(
    dash.dependencies.Output('down-heatmap', 'figure'),
    [dash.dependencies.Input('cancer-type', 'value'),
     dash.dependencies.Input('prediction-type', 'value'),
     dash.dependencies.Input('gene-slider', 'value')])
def update_down(cancer_choice, prediction_choice, slider_choice):
    down_df = down[down['Target'] == prediction_choice]
    down_df = down_df[down_df['Cancer'] == cancer_choice]
    down_tmp = down_df['Gene'].unique().tolist()
    down_tmp = down_tmp[0:slider_choice]
    down_df = down_df.loc[down_df['Gene'].isin(down_tmp)]
    down_df = down_df.sort_values(['Gini', 'Value'], ascending=False)

    custom_hover = []
    for _, i in down_df.iterrows():
        dat = 'Gene: '+'{}'.format(i['Gene'])+'<br>'+'Feature: '+'{}'.format(i['Feature']) + \
                                   '<br>'+'Value: ' + \
                                       '{0:.2f}'.format(
                                           i['Value'])+'<br>'+'R: '+'{0:.2f}'.format(i['R'])
        custom_hover.append(dat)

    return {
        'data': [(
            go.Heatmap(
                x=down_df['Gene'],
                y=down_df['Feature'],
                z=down_df['Value'],
                name='down-heatmap',
                colorscale=colormap,
                text=custom_hover,
                hoverinfo='text')
                )],
        'layout': go.Layout(
            title=go.layout.Title(
                text=('<b>Target label: '+down_df['Type'].iloc[0]+'</b>'),
                xanchor='left',
                yanchor='bottom',
                x=0.47,
                font=dict(
                    family='Arial',
                    size=16,
                    color='black'
                    )
                ),
            autosize=False,
            yaxis=dict(
                automargin=True,
                autorange='reversed',
                tickfont=dict(
                    family='Arial, sans-serif',
                    size=14,
                    color='black',
                    )
                )
            )
        }

    # Callback for the slider
    @app.callback(Output('updatemode-output-container', 'children'),
                  [dash.dependencies.Input('gene-slider', 'value')])
    def display_value(value):
            return 'Number of genes displayed: {}'.format(value, value)

# For server
#server = app.server


if __name__ == '__main__':
    app.run_server(debug=True)
