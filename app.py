from dash import Dash, dcc, html, Input, Output
import altair as alt
from vega_datasets import data

# Load Iris Dataset
iris = data.iris()

# Set up app and layout/frontend
app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
    html.Div('Dashboard to explore Iris Plants', style={'color': 'black', 'fontSize': 44}),
    html.Iframe(
        id='scatter',
        style = {'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='ycol-widget', 
        value='petalWidth',
        options=[{'label': i, 'value':i} for i in iris.columns]),
    dcc.Slider(id = 'xslider', min=0, max=2.6)
], style={'marginTop': 50})

# Set up callback / backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('ycol-widget', 'value'),
    Input('xslider', 'value'))
def plot_altair(ycol, xmax):
    chart = alt.Chart(iris[iris['petalWidth'] < xmax]).mark_point().encode(
        x='petalWidth',
        y=ycol,
        color = 'species',
        tooltip= 'petalWidth').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)
