from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("Pink_Morsel_Sales_Data.csv")

df["date"] =  pd.to_datetime(df["date"])
df = df.sort_values(by="date", ascending=True)

regions = df["region"].unique()

app.layout = dbc.Container(fluid=True, className="p-4 bg-light min-vh-100", children=[
    
    dbc.Card(className="mb-4 shadow-sm border-0 bg-dark text-white", children=[
        dbc.CardBody(className="text-center py-4", children=[
            html.H1("Pink Morsel Sales Dashboard", className="display-5 font-weight-bold mb-2"),
            html.P("Visual chart of Pink Morsel Sales across regionas", className="lead text-muted")
        ])
    ]),
    
    dbc.Row([
        
        dbc.Col(md=3, children=[
            dbc.Card(className="shadow-sm border-0 mb-4 p-3", children=[
                html.H5("Filter Settings", className="text-secondary border-bottom pb-2 mb-3"),
                html.Label("Select Target Region:", className="font-weight-bold mb-2 text-dark"),
                
                dbc.RadioItems(
                    id='region-filter',
                    options=[{'label': r, 'value': r} for r in regions],
                    value=regions[0],
                    inline=False,
                    className="btn-group-vertical w-100",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-primary text-start mb-2 w-100 rounded"
                )
            ])
        ]),
        
        dbc.Col(md=9, children=[
            dbc.Card(className="shadow-sm border-0 p-3", children=[
                html.H5(id='chart-title', className="text-primary mb-3"),
                
                dcc.Loading(
                    type="circle", 
                    color="#1a1a1a",
                    children=dcc.Graph(id='interactive-line-chart', config={'displayModeBar': False})
                )
            ])
        ])
    ])
])

@app.callback(
    [Output('interactive-line-chart', 'figure'),
     Output('chart-title', 'children')],
    [Input('region-filter', 'value')]
)
def update_dashboard(selected_region):
    filtered_df = df[df['region'] == selected_region]
    
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        markers=True,
        template="plotly_white"
    )
    
    fig.update_traces(line_color='#2c3e50', line_width=3, marker=dict(size=8, color='#e74c3c'))
    fig.update_layout(
        margin=dict(l=40, r=40, t=20, b=40),
        xaxis=dict(showgrid=True, gridcolor='#f0f0f0', type='date'),
        yaxis=dict(showgrid=True, gridcolor='#f0f0f0'),
        font_family="Arial"
    )
    
    dynamic_title = f"Trend Highlights: {selected_region} Region"
    
    return fig, dynamic_title

if __name__ == '__main__':
    app.run(debug=True)