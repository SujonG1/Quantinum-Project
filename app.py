from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("Pink_Morsel_Sales_Data.csv")

df["date"] =  pd.to_datetime(df["date"])
df = df.sort_values(by="date", ascending=True)

fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Chart",
    template="plotly_white",
    markers=True
)

fig.update_xaxes(type='date')

app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'padding': '20px'}, children=[
    html.H1(
        children='Pink Morsel Analysis Dashboard',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),
    
    html.P(
        children='Visualizing sales trend of Pink Morsel with respect to time.',
        style={'textAlign': 'center', 'color': '#7f8c8d'}
    ),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)