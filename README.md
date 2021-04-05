# Energy Data Visualization Dashboard 
> Here goes your awesome project description!

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
This projects was created to show the growth trends in Nameplate Capcity categorized each prime mover. 

## Screenshots
![Example screenshot](./img/screenshot.png)

## Technologies
* Dash - dash_core_components - dash_html_components - dash_bootstrap_components
* Plotly - plotly.express - plotly.io
* Pandas
* OS
* Path

## Setup
1. Clone this repo to your desktop.
2. Install Dependencies 
    * import dash
    * import dash_core_components as dcc
    * import dash_html_components as html
    * from dash.dependencies import Output, Input
    * import plotly.express as px
    * import dash_bootstrap_components as dbc
    * import pandas as pd
    * import plotly.graph_objects as go
    * import os
    * from pathlib import Path
    * import plotly.io as pio
3. Run 'dash_app.py' 
4. View the local server at http://127.0.0.1:8050/

## Features
List of features ready and TODOs for future development
* Scatter Geo Map 
* Line Chart
* Bar Chart 
* Dropdowns and radio buttons to include or excude data by Prime Mover
* Graphs automatically orient to fit window size 

To-do list:
* Make color scheme so that every graph has consistent color markers for prime movers 
* Change from using local xlsx files to pulling data from the EIA API 

## Status
Project is: _in progress_

## Contact
Created by [@HenryQuillin](henryquillin@gmail.com) - feel free to contact me!
