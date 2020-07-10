import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Import and clean data (importing csv into pandas)
#df = pd.read_csv("WPP2019_TotalPopulationBySex.csv")
df = pd.read_csv("x.csv")
# App layout
app.layout = html.Div([

    html.H1("Web Application with world population", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2001", "value": 2001},
                     {"label": "2002", "value": 2002},
                     {"label": "2003", "value": 2003},
                     {"label": "2004", "value": 2004},
                     {"label": "2005", "value": 2005},
                     {"label": "2006", "value": 2006},
                     {"label": "2007", "value": 2007},
                     {"label": "2008", "value": 2008},
                     {"label": "2009", "value": 2009},
                     {"label": "2010", "value": 2010},
                     {"label": "2011", "value": 2011},
                     {"label": "2012", "value": 2012},
                     {"label": "2013", "value": 2013},
                     {"label": "2014", "value": 2014},
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018},
                     {"label": "2019", "value": 2019}],
                 multi=False,
                 value=2019,
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
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    #container = "The year chosen by user was: {}".format(option_slctd)

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
    #hover_data=df['Location','PopTotal']
    marker_line_width=0.5,
    colorbar_title = 'Population',
    )]
    )
    container = "The year chosen by user was: {}".format(option_slctd)
    return container, fig
     
if __name__ == '__main__':
    app.run_server(debug=True)
