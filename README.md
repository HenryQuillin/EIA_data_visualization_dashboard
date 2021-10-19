# Energy Data Visualization Dashboard 


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
Interactive data visualization app for energy/power trading. Displays wind, solar, and other energy data. Created to show the growth trends categorized each prime mover.

## Screenshots
![Screen Shot 2021-04-05 at 1 06 53 PM](https://user-images.githubusercontent.com/46876350/113608401-2a677b00-9610-11eb-9f6c-dc788f3a45a8.png)
![Screen Shot 2021-04-05 at 1 09 59 PM](https://user-images.githubusercontent.com/46876350/113608467-3ce1b480-9610-11eb-8982-d2f1abc42ddc.png)
![Screen Shot 2021-04-05 at 1 10 15 PM](https://user-images.githubusercontent.com/46876350/113608496-4703b300-9610-11eb-8030-83c65453a226.png)

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
Project is: _finished_

## Contact
Created by [@HenryQuillin](henryquillin@gmail.com) - feel free to contact me!
