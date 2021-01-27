import pandas as pd
import plotly.express
import plotly.graph_objects as go
import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pathlib import Path

app = dash.Dash(__name__)


df = pd.read_csv(Path(os.getcwd()) / 'data' / "df_2018.csv")

df.reset_index(inplace=True)
print(df[:5])


# App layout
fig = go.Figure(data=go.Scattergeo(
    lon=df['Longitude'],
    lat=df['Latitude'],
    text=df['Plant Name'],
    mode='markers',
))
fig.update_layout(height=800,width=1300,margin={"r":0,"t":0,"l":0,"b":0})
app.layout = html.Div([

    html.H1("EIA Energy Data", style={'text-align': 'center'}),

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
    html.Br(),

    dcc.Graph(id='EIA_data', figure=fig)

])


#fig.show()

# ------------------------------------------------------------------------------

'''
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    #dff = dff[dff["Year"] == option_slctd]
    #dff = dff[dff["Affected by"] == "Varroa_mites"]

# Plotly Express
    
    fig = px.choropleth(
        data_frame=df,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )
    
    fig = px.scatter_geo(df, locations="iso_alpha",
                         color="continent",  # which column to use to set the color of markers
                         hover_name="country",  # column added to hover information
                         size="pop",  # size of markers
                         projection="natural earth")

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )


'''

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)