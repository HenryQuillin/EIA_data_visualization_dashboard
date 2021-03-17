import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from dash_html_components.Figure import Figure
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime
import plotly.express
import plotly.graph_objects as go

data = 'C:\\Users\\henry\\Desktop\\Projects\\internship_repo\\data'

all_years = pd.DataFrame()
years = range(2019,2020)
for year in years:
    #create plant dataframe 
    plant_df = pd.read_excel(data + f'\\2___Plant_Y{year}.xlsx', skiprows=1, nrows=25)
    plant_df = plant_df[['Utility ID','Plant Code', 'Plant Name', 'Latitude', 'Longitude', 'Transmission or Distribution System Owner']]

    #create generator dataframe
    gen_df = pd.read_excel(data + f'\\3_1_Generator_Y{year}.xlsx', skiprows=1, nrows=25)
    gen_df = gen_df[['Utility ID','Plant Code', 'Plant Name','Generator ID', 'Technology', 'Prime Mover', 'Operating Year','Nameplate Capacity (MW)']]

    #merge both dataframes on 'plant code' 
    merged_df = pd.merge(gen_df, plant_df)
    print('-------MERGED DF--------')
    print(merged_df.head(2))

    merged_df = merged_df.assign(year=year)
    all_years = pd.concat([all_years, merged_df], ignore_index=True)
    print('All years------------------')
    print(all_years.head(3))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])



# ------------APP LAYOUT------------------------------
app.layout = dbc.Container([

    dbc.Row([
        dbc.Col(html.H1("Energy Data Dashboard",
                        className='text-center text-primary mb-4'),
                width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='dpdn1', multi=False, value='Wind', 
                                    options=[{'label':x, 'value':x}
                                    for x in gen_df['Technology'].unique()],
                         ),
            dcc.Graph(id='line-fig', figure={})
        ]),
        dbc.Col([
            dcc.Dropdown(id='my-dpdn2', multi=True, value=['PFE','BNTX'],
                         options=[{'label':x, 'value':x}
                                  for x in sorted(df['Symbols'].unique())],
                         ),
            dcc.Graph(id='line-fig2', figure={})
        ])
    ]),

    dbc.Row([
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)



# fig = go.Figure(data=go.Scattergeo(
#     lon=merged_df['Longitude'],
#     lat=merged_df['Latitude'],
#     text=merged_df['Plant Name'],
#     mode='markers',
# ))
# fig.update_layout(height=400,width=600,margin={"r":0,"t":0,"l":0,"b":0})

# fig.show()













'''
app = dash.Dash(__name__, external_stylesheets=dbc.themes.DARKLY,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

#Layout Section
#-------------------------------------

app.layout = dbc.Container([ 
    dbc.Row({
        dbc.Col(html.H1("Energy Data Dashboard----",
                        className='text-center bg-white, mb-4'
        ))
    })
])



if __name__ == '__main__':
    app.run_server(debug=True)



colors = {
    'background': '#111111',
    'text': '#7FDBFF'

fig = go.Figure(data=go.Scattergeo(
    lon=merged_df['Longitude'],
    lat=merged_df['Latitude'],
    text=merged_df['Plant Name'],
    mode='markers',
))
fig.update_layout(height=400,width=600)


app.layout = html.Div([
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=True,
                 value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br()

    #dcc.Graph(id='EIA_data', figure=fig)

])


fig.show()

# ------------------------------------------------------------------------------

'''