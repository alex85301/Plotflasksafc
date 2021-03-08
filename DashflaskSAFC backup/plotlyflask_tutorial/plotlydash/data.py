"""Prepare data for Plotly Dash."""
#import pandas as pd
#import numpy as np


#def create_dataframe():"""Create Pandas DataFrame from local CSV."""
#    df = pd.read_csv('data/safc1920.csv', parse_dates=['created'])
#    df['created'] = df['created'].dt.date
#    df.drop(columns=['incident_zip'], inplace=True)
#    num_complaints = df['complaint_type'].value_counts()
#    to_remove = num_complaints[num_complaints <= 30].index
#    df.replace(to_remove, np.nan, inplace=True)
#    return df


#import pandas as pd
#import numpy as np

#def create_dataframe():
#     df = pd.read_csv('/Users/alexbaverstock/DashflaskSAFC/data/safc1920.csv')               
#     PlayerRatings = df[['rating','player_name']]
#     PlayerRatings.fillna('0', inplace=True)
#     PlayerRatings['rating'] = df['rating'].astype(float)
#     PlayerRatings['player_name'] = df['player_name'].astype(str)
#     df  = pd.pivot_table(PlayerRatings,values='rating',index='player_name',aggfunc='mean')
 #    return df
