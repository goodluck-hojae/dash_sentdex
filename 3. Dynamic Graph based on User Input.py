import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()

stock = 'TSLA'
df = web.DataReader(stock, 'google', start, end)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        symbol to graph:
    '''),

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')

])

@app.callback(
    Output(component_id='output-graph',component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_graph(input_data):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'google', start, end)

    return dcc.Graph(
        id='example_graph',
        figure={
            'data': [
                {'x': df.index, 'y':df.Close, 'type':'line','name':input_data},
            ],
            'layout':{
                'title': input_data
            }
        }
    )
if __name__ == '__main__':
    app.run_server(debug=True)