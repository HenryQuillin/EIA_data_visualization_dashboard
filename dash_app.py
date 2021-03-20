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

data = str(Path(os.getcwd()+'/data'))

final_df = pd.DataFrame()
years = range(2019,2020)
for year in years:
    #create plant dataframe 
    plant_df = pd.read_excel(data + f'/2___Plant_Y{year}.xlsx', skiprows=1, nrows=25)
    plant_df = plant_df[['Utility ID','Plant Code', 'Plant Name', 'Latitude', 'Longitude']]

    #create generator dataframe
    gen_df = pd.read_excel(data + f'/3_1_Generator_Y{year}.xlsx', skiprows=1, nrows=25)
    gen_df = gen_df[['Utility ID','Plant Code', 'Plant Name','Generator ID', 'Technology', 'Prime Mover', 'Operating Year','Nameplate Capacity (MW)']]

    #merge both dataframes on 'plant code' 
    merged_df = pd.merge(gen_df, plant_df)
    print('-------MERGED DF--------')

    merged_df = merged_df.assign(year=year)
    final_df = pd.concat([final_df, merged_df], ignore_index=True)
    print('---------------All years------------------')
print('----------LOADED DATAFRAMES----------------')

# Add total capacity of prime movers 
total_capacity_df = final_df[['year','Prime Mover','Nameplate Capacity (MW)']].groupby('Prime Mover', as_index=False)['Nameplate Capacity (MW)'].sum()
for year in years:
    total_capacity_df = total_capacity_df.assign(year=year)
    total_capacity_df.rename(columns = {'Nameplate Capacity (MW)':'Total Nameplate Capacity'}, inplace = True) 
print(total_capacity_df)

exit()
print(final_df.head(3))
# Create df with total_capacity 
total_capacity_df = final_df[['year','Prime Mover','Nameplate Capacity (MW)']]
for x in total_capacity_df['Prime Mover'].unique():
    print(x)
    total = total_capacity_df.loc[total_capacity_df['Prime Mover'] == x, 'Nameplate Capacity (MW)'].sum()
    total_capacity_df = total_capacity_df.assign(TotalCapacity=total)
#total_capacity_df.loc[total_capacity_df['Prime Mover'] == x, 'Total Capacity'] = total
#print(total_capacity_df.head(15))



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
        dbc.Col([
            html.H3("Total Nameplate Capacity by Prime Mover", className='text-center text-primary mb-4'),
            dcc.Dropdown(id='dpdn1', multi=True, value=['WT','IC'], options=[{'label':x, 'value':x}
                                    for x in final_df['Prime Mover'].unique()],
                         ),
            dcc.Graph(id='line-fig', figure={})
        ], #width={'size':5, 'offset':0},
        xs=12, sm=12, md=12, lg=5, xl=5),
        dbc.Col([
            html.H3("Total Nameplate Capacity by Technology", className='text-center text-primary mb-4'),
            dcc.Dropdown(id='dpdn2', multi=True, value='Petroleum Liquids', options=[{'label':x, 'value':x}
                                  for x in sorted(final_df['Technology'].unique())],
                         ),
            dcc.Graph(id='line-fig2', figure={})
        ], #width={'size':5, 'offset':0} 
        xs=12, sm=12, md=12, lg=5, xl=5),
    ],justify='around'),

    dbc.Row([
        dbc.Col([
            html.H3('Bubble Map', style={'textDecoration': 'underline'}, className='text-center'), 
            dcc.Checklist(id='bubble_map_checklist', value=['IC', 'WT', 'HY'], options=[{'label':x,'value':x} for x in sorted(final_df['Prime Mover'].unique())],labelClassName='mr-3'),
            dcc.Graph(id='bubble_chart', figure={})
        ], #width={'size':5, 'offset':0})
        xs=12, sm=12, md=12, lg=10, xl=10),
    ], justify='around')
],fluid=True)

print('---------------CREATED LAYOUT-------------------')
# Updating Line Fig 1 
@app.callback(
    [Output('line-fig','figure')],
    [Input('dpdn1','value')]
)
def update_fig1(dpdn_val):
    dff = final_df[final_df['Prime Mover'].isin(dpdn_val)]
    line_fig = px.line(dff, x='year', y='Nameplate Capacity (MW)')
    return [line_fig]




print('---------------RAN SERVER-------------------')

app.run_server(debug=True)
'''



# fig = go.Figure(data=go.Scattergeo(
#     lon=merged_df['Longitude'],
#     lat=merged_df['Latitude'],
#     text=merged_df['Plant Name'],
#     mode='markers',
# ))
# fig.update_layout(height=400,width=600,margin={"r":0,"t":0,"l":0,"b":0})

# fig.show()














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