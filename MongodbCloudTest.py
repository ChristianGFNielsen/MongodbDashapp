import pymongo
import pandas as pd
import dash
from dash import html
from dash import dcc 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

myclient = pymongo.MongoClient("mongodb+srv://chri733q:password@cluster0.wejpo.mongodb.net/test")


mydb = myclient["mydatabase"]
mycol = mydb["virksomhedsomsætninger"]

#mylist = [
#    {"Firma": "Colgate", "omsætning": 10000, "år": 2021},
#    {"Firma": "Apple", "omsætning": 15000, "år": 2021},
#    {"Firma": "Tesla", "omsætning": 20000, "år": 2021}
#]
#x = mycol.insert_many(mylist)

data = pd.DataFrame(list(mycol.find()))

print(data)

fig_omsætning = px.histogram(data, 
    x='Firma', y='omsætning', title='Omsætning pr Firma',
    hover_data=[],
    labels={'omsætning':'Omsætning', 'Firma':'firma'})
fig_omsætning.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)

dash_app = dash.Dash(__name__)
app = dash_app.server

dash_app.layout = html.Div(children=[

    html.Div(children=[
            dcc.Graph(id="Firmaomsætninger", figure=fig_omsætning)
        ]),
])


if __name__ == '__main__':
    dash_app.run_server(debug=True)
