import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
#for sensor
import Adafruit_DHT
import time

#grab sensor data
sensor=11
pin=4

#setting lengths for plot
X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(75)

# temp reading iteration counter
i=0
     
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1 * 1000
        ),
    ]
)
print('testing')

@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter():
    #print('Results: '+str(i))
    humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
    tfahr = temperature*9/5 +32
    print(tfahr)
    X.append(X[-1] + 1)
    Y.append(tfahr)

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)],
                                                title='Time Elapsed (seconds)'),
                                                yaxis=dict(range=[min(Y), max(Y)],
                                                title='Temperature (°F)'),
                                                )}
#title='Temperature (°F)'),

if __name__ == '__main__':
    app.run_server(debug=True)

