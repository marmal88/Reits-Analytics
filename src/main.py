import numpy as np
import plotly.express as px
from dotenv import load_dotenv
import os
import plotly.graph_objects as go

import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.app_func.pdf import Pdf_Scraper


PDF = "/home/oem/Documents/coding/personal/Reits-Analytics/data/Ascendas-Reit-Annual-Report-2021.pdf"

scraper = Pdf_Scraper()

bizpark_table = scraper.get_table(PDF, 72)
buildings_df = scraper.get_bizpark_df(bizpark_table)

# print(buildings_df["gross_revenue_(SGD:Mil)"])

load_dotenv()
api_key = os.getenv("MAPBOX_KEY")

fig = px.scatter_mapbox(
    buildings_df,
    title="Business and Science Parks",
    lon="longitude",
    lat="lattitude",
    color="property",
    size="gross_revenue_(SGD:Mil)",
    zoom=10,
    height=700,
    width=1500,
)

fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_accesstoken=api_key,
)
fig.update_layout(autosize=True, margin={"r": 10, "t": 50, "l": 10, "b": 10})

app = dash.Dash()
app.layout = html.Div([dcc.Graph(figure=fig)])


if __name__ == "__main__":
    app.run_server(debug=True)
