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
import plotly.express as px

def init_dashboard(server):
   
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
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
    fig = px.scatter(x=df.index,
        y=df['rating'])

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[dcc.Graph(
            #id='scatter3',
            figure= fig              
            ),
            create_data_table(df)
        ],
        id='dash-container'
    )
    return dash_app.server


def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    df = pd.read_csv('/Users/alexbaverstock/DashflaskSAFC/data/safc1920.csv')               
    PlayerRatings = df[['rating','player_name']]
    table = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in PlayerRatings],
        #columns=df[['rating','player_name']]
        data=df.to_dict('records'),
        sort_action="native",
        sort_mode='native',
        page_size=300
    )
    return table

