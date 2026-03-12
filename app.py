import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import datetime

# Load the processed data
df = pd.read_csv('data/output.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

app = dash.Dash(__name__)

app.layout = html.Div(style={
    'fontFamily': 'Arial, sans-serif',
    'backgroundColor': '#f4f4f4',
    'padding': '20px'
}, children=[

    html.H1('Pink Morsel Sales Visualiser', style={
        'textAlign': 'center',
        'color': '#ff69b4',
        'fontSize': '36px',
        'marginBottom': '10px'
    }),

    html.P('Filter by region:', style={
        'textAlign': 'center',
        'color': '#555',
        'fontSize': '16px'
    }),

    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'},
        ],
        value='all',
        inline=True,
        style={
            'textAlign': 'center',
            'fontSize': '16px',
            'marginBottom': '20px',
            'color': '#333'
        }
    ),

    dcc.Graph(id='sales-chart')
])

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered = df.groupby(['date', 'region'], as_index=False)['sales'].sum()
        fig = px.line(filtered, x='date', y='sales', color='region',
                      labels={'date': 'Date', 'sales': 'Sales ($)', 'region': 'Region'})
    else:
        filtered = df[df['region'] == selected_region].groupby('date', as_index=False)['sales'].sum()
        fig = px.line(filtered, x='date', y='sales',
                      labels={'date': 'Date', 'sales': 'Sales ($)'})

    fig.add_vline(
        x=datetime.datetime(2021, 1, 15).timestamp() * 1000,
        line_dash='dash',
        line_color='red',
        annotation_text='Price Increase',
        annotation_position='top left'
    )

    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='#f4f4f4',
        title='Pink Morsel Sales Over Time',
        title_x=0.5
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)