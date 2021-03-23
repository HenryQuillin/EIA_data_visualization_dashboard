from logging import lastResort
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime
import plotly.graph_objects as go
import os
from pathlib import Path
import plotly.io as pio


data = str(Path(os.getcwd()+'/data'))
pio.templates.default = "plotly_white"

master_df = pd.DataFrame()
tc_by_pm_df = pd.DataFrame()
#template = 'plotly_dark'
years = range(2018,2020)
for year in years:
    #create plant dataframe 
    plant_df = pd.read_excel(data + f'/2___Plant_Y{year}.xlsx', skiprows=1)
    plant_df = plant_df[['Utility ID','Plant Code', 'Plant Name', 'Latitude', 'Longitude']]

    #create generator dataframe
    gen_df = pd.read_excel(data + f'/3_1_Generator_Y{year}.xlsx', skiprows=1)
    gen_df = gen_df[['Utility ID','Plant Code', 'Plant Name','Generator ID', 'Prime Mover', 'Technology', 'Operating Year','Nameplate Capacity (MW)']]

    #merge both dataframes on 'plant code' 
    merged_df = pd.merge(gen_df, plant_df)
    print('-------MERGED DF--------')
    merged_df = merged_df.assign(year=year)
    # Create Total capcity grouped by Prime Mover Dataframe 
    dff = merged_df[['year','Prime Mover','Nameplate Capacity (MW)']].groupby('Prime Mover', as_index=False)['Nameplate Capacity (MW)'].sum()
    dff = dff.assign(year=year)
    tc_by_pm_df = pd.concat([tc_by_pm_df, dff], ignore_index=True)

    master_df = pd.concat([master_df, merged_df], ignore_index=True)

tc_by_pm_df.rename(columns = {'Nameplate Capacity (MW)':'Total Nameplate Capacity'}, inplace = True) 

print('----------LOADED DATAFRAMES----------------')

print(dff.shape)
print(tc_by_pm_df)
print(tc_by_pm_df.shape)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
print('---------------CREATING LAYOUT-------------------')
# ------------APP LAYOUT------------------------------
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Energy Data Dashboard",
                        className='text-center text-primary mb-4'),
                )
    ]),
        dbc.Row([
        dbc.Col(html.P("Created by Henry Quillin",
                        className='text-center pt-1'),
                )
    ]),
    dbc.Row([
        dbc.Col([
            html.H3('Map of generation units in the United States', style={'textDecoration': 'underline'}, className='text-center'), 
            dcc.Checklist(id='bubble_map_checklist', value=['BA','BT','CE','CS','FW','HY','OT','PS','WT'], options=[{'label':x,'value':x} for x in sorted(master_df['Prime Mover'].unique())],className='text-center',labelClassName='mr-3 '),
            dcc.Graph(id='bubble_chart', figure={})
        ], #width={'size':5, 'offset':0})
        xs=12, sm=12, md=12, lg=10, xl=10),
    ], justify='around'),
    dbc.Row([
        dbc.Col([
            html.H4("Total Nameplate Capacity by Prime Mover (Line Chart)", className='text-center text-primary mb-4'),
            dcc.Dropdown(id='dpdn1', multi=True, value=['WT','CT','CA','HY'], options=[{'label':x, 'value':x} for x in master_df['Prime Mover'].unique()],
                         ),
            dcc.Graph(id='line-fig', figure={})
        ], #width={'size':5, 'offset':0},
        xs=12, sm=12, md=12, lg=5, xl=5),
        dbc.Col([
            html.H4("Total Nameplate Capacity by Prime Mover (Bar Chart)", className='text-center text-primary mb-4'),
            dcc.Dropdown(id='dpdn2', multi=True, value=['BA','BT','CE','CS','FW','HY','OT','PS','WT'], options=[{'label':x, 'value':x} for x in sorted(master_df['Prime Mover'].unique())],
                         ),
            dcc.Graph(id='bar-chart', figure={})
        ], #width={'size':5, 'offset':0} 
        xs=12, sm=12, md=12, lg=5, xl=5),
    ],justify='around')
],fluid=True)

print('---------------CREATED LAYOUT-------------------')
# Updating Line Fig 1 
@app.callback(
    [Output('line-fig','figure')],
    [Input('dpdn1','value')]
)
def update_fig1(dpdn_val):
    dff = tc_by_pm_df[tc_by_pm_df['Prime Mover'].isin(dpdn_val)]
    fig = px.line(dff, x='year', y='Total Nameplate Capacity', color='Prime Mover')
    return [fig]
@app.callback(
    [Output('bar-chart','figure')],
    [Input('dpdn2','value')]
)
def update_bar_chart(dpdn_val):
    dff = tc_by_pm_df[tc_by_pm_df['Prime Mover'].isin(dpdn_val)]
    line_fig = px.bar(dff, x='year', y='Total Nameplate Capacity', color='Prime Mover')
    return [line_fig]

# Updating Map 
@app.callback(
    [Output('bubble_chart','figure')],
    [Input('bubble_map_checklist','value')]
)
def update_map(dpdn_val):
    dff = master_df[master_df['Prime Mover'].isin(dpdn_val)]
    fig1 = px.scatter_geo(dff,
                     lat='Latitude',
                     lon='Longitude',
                     color='Prime Mover',
                     scope='usa',
                     size='Nameplate Capacity (MW)',
                     width=1200,
                     height=600
                      # size of markers, "pop" is one of the columns of gapminder
                     )
    # fig = go.Figure(data=go.Scattergeo(
    # locationmode = 'USA-states',
    # lon=dff['Longitude'],
    # lat=dff['Latitude'],
    # text=dff['Plant Name'],
    # mode='markers',
    # marker = dict(
    #     size = 8,
    #     opacity = 0.8,
    #     reversescale = True,
    #     autocolorscale = False,
    #     symbol = 'square',
    #     line = dict(
    #         width=1,
    #         color='rgba(102, 102, 102)'
    #     ),
    #     colorscale = 'Blues',
    #     cmin = 0
    # )))


    return[fig1]


'''
@app.callback(
    [Output('bar-chart','figure')],
    [Input('dpdn2','value')]
)
def update_fig2(dpdn_val):
    t_by_pm_df = pd.DataFrame()
    dff = master_df[['year','Prime Mover','Technology']].groupby('Technology', as_index=False)['Nameplate Capacity (MW)'].sum()
    for year in years:
        dff = dff.assign(year=year)
        t_by_pm_df = pd.concat([t_by_pm_df, dff], ignore_index=True)
    t_by_pm_df.rename(columns = {'Nameplate Capacity (MW)':'Total Nameplate Capacity'}, inplace = True) 
    dff2 = t_by_pm_df[t_by_pm_df['Technology'].isin(dpdn_val)]
    line_fig = px.line(dff2, x='year', y='Total Nameplate Capacity', color='Technology')
    return [line_fig]
'''
# def update_fig2(dpdn_val):
#     dff = tc_by_pm_df[tc_by_pm_df['Prime Mover'].isin(dpdn_val)]
#     line_fig = px.line(dff, x='year', y='Total Nameplate Capacity', color='Prime Mover')
#     return [line_fig]



print('---------------RAN SERVER-------------------')
if __name__ == '__main__':
    app.run_server(debug=True)
#exit()
'''
t_by_pm_df = pd.DataFrame()
dff = master_df[['year','Prime Mover','Technology']].groupby('Technology', as_index=False)['Nameplate Capacity (MW)'].sum()
for year in years:
    dff = dff.assign(year=year)
    t_by_pm_df = pd.concat([t_by_pm_df, dff], ignore_index=True)




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