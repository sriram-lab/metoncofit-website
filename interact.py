"""
interact.py
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def interact(df):
    """
    """
    # get values that will be used
    num_uniq_genes = df["Gene"].nunique()
    cancer_type = df["Cancer"].unique()
    prediction_type = df["Target"].unique()

    _widgets = dbc.Container(
        [
            # Text that updates with slider values
            dbc.Row(
                html.Div(id='updatemode-output-container',
                style={
                    'margin-top':20,
                    'padding':'0px 20px 20px 20px'
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
                                0: {'label':'0'},
                                100: {'label':'100'},
                                250: {'label':'250'},
                                500: {'label':'500'},
                                750: {'label':'750'},
                                num_uniq_genes: {'label':str(num_uniq_genes)}
                            },
                            updatemode='drag'
                        ),
                    style={'width':'50%', 'padding':'0px 20px 20px 20px'},
                    ),

                    # Dropdown menus
                    dbc.Col(
                        html.Div(
                            dcc.Dropdown(
                                id='cancer-type',
                                options=[{'label':i, 'value':i} for i in cancer_type],
                                value='Pan Cancer'
                            )
                        ),
                        width={"size":3.0},

                    ),
                    dbc.Col(
                        html.Div(
                            dcc.Dropdown(
                                id='prediction-type',
                                options=[{'label':i,'value':i} for i in prediction_type],
                                value='Differential Expression'
                            )
                        ),
                        width={"size":3.0,
                            "offset":0.3}
                    )
                ]
            )
        ]
    )
