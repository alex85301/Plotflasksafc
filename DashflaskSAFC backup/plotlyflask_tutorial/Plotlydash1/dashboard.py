
"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
#from .data import create_dataframe
from .layout import html_layout
import plotly.graph_objs as go


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp1/',
        external_stylesheets=[
            '/static/dist/css/styles.css',
            'https://fonts.googleapis.com/css?family=Lato'
        ]
    )

    # Load DataFrame
    df = pd.read_csv('/Users/alexbaverstock/DashflaskSAFC/data/safc1920.csv')               
    PlayerRatings = df[['rating','player_name']]
    PlayerRatings.fillna('0', inplace=True)
    PlayerRatings['rating'] = df['rating'].astype(float)
    PlayerRatings['player_name'] = df['player_name'].astype(str)
    df  = pd.pivot_table(PlayerRatings,values='rating',index='player_name',aggfunc='mean')
    df1 = df.reset_index()
    df2 = df1

    #df = df.unstack()

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div([
    dcc.Graph(
        id='scatter3',
        figure={
            'data': [
                go.Scatter(
                    x = df.index,
                    y = df['rating'],
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                        }
                )],
            'layout': go.Layout(
                title = 'Player Ratings SAFC',
                xaxis = {'title': 'Player Names'},
                yaxis = {'title': 'Average Rating'},
                hovermode='closest'
            )
        }
    ),
    create_data_table(df2)
    ],
    id='dash-container')
    return dash_app.server

def create_data_table(df2):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in df2.columns],
        data=df2.to_dict('records'),
        sort_action="native",
        sort_mode='native',
        page_size=300
    )
    return table