"""
code to generate interctive web-based heatmaps from pandas dataframe
@author: Scott Campit
"""

html.Div(
    dcc.Graph(
        id='up-heatmap',
        figure={
            'data': [(
                go.Heatmap(
                    x=up['Gene'],
                    y=up['Feature'],
                    z=up['Value'],
                    name='up',
                    colorscale='RdBu')
                    )],
            'layout':go.Layout(
                title=go.layout.Title(
                    text=('<b>Target label: '+up['Type'].iloc[0]+'</b>'),
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
),
