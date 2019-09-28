import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

from src.dash_header import tab as tabs_header
from src.dash_page import page

external_stylesheets = ['./static/css/main.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    tabs_header,
    html.Div(id='page-monitoring')
])

@app.callback(
    Output(component_id='page-monitoring', component_property='children'),
    [Input(component_id='tab-1', component_property='n_clicks'),
    Input(component_id='tab-2', component_property='n_clicks'),
    Input(component_id='tab-3', component_property='n_clicks')],
)
def display(btn_1, btn_2, btn_3):
    if btn_1 != None:
        return page
    elif btn_2 != None:
        return html.Div([html.P("Hello btn")])
    elif btn_3 != None:
        return html.Div([html.P("Hello")])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)

