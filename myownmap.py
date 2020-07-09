import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Import and clean data (importing csv into pandas)
df = pd.read_csv("WPP2019_TotalPopulationBySex.csv")

# App layout
app.layout = html.Div([

    html.H1("Web Application with world population", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2001", "Time": 2001},
                     {"label": "2002", "Time": 2002},
                     {"label": "2003", "Time": 2003},
                     {"label": "2004", "Time": 2004},
                     {"label": "2005", "Time": 2005},
                     {"label": "2006", "Time": 2006},
                     {"label": "2007", "Time": 2007},
                     {"label": "2008", "Time": 2008},
                     {"label": "2009", "Time": 2009},
                     {"label": "2010", "Time": 2010},
                     {"label": "2011", "Time": 2011},
                     {"label": "2012", "Time": 2012},
                     {"label": "2013", "Time": 2013},
                     {"label": "2014", "Time": 2014},
                     {"label": "2015", "Time": 2015},
                     {"label": "2016", "Time": 2016},
                     {"label": "2017", "Time": 2017},
                     {"label": "2018", "Time": 2018},
                     {"label": "2019", "Time": 2019}],
                 multi=False,
                 Time=2019,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_world_map', figure={})

])

# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_world_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='Time')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Time"] == option_slctd]
    
    fig = go.Figure(data=[go.Choropleth(
    locations = df['iso_alpha'],
    z = df['PopTotal'],
    text = df['Location'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    hover_data=df['Location','PopTotal']
    marker_line_width=0.5,
    colorbar_title = 'Population',
    ])
    )
    return container, fig
     
if __name__ == '__main__':
    app.run_server(debug=True)
