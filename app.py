import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import datetime

# Load the processed data
df = pd.read_csv('data/output.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Aggregate sales by date and region
df_grouped = df.groupby(['date', 'region'], as_index=False)['sales'].sum()

# Create the line chart
fig = px.line(
    df_grouped,
    x='date',
    y='sales',
    color='region',
    title='Pink Morsel Sales Over Time',
    labels={'date': 'Date', 'sales': 'Sales ($)', 'region': 'Region'}
)

# Add a vertical line for the price increase on Jan 15, 2021
fig.add_vline(
    x=datetime.datetime(2021, 1, 15).timestamp() * 1000,
    line_dash='dash',
    line_color='red',
    annotation_text='Price Increase',
    annotation_position='top left'
)

# Build the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Pink Morsel Sales Visualiser', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)