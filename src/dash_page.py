import dash
import dash_core_components as dcc
import dash_html_components as html

import dash_daq as daq

markdown_text = '''
---
### MONITORING 1:

'''

page = html.Div(children=[
    dcc.Markdown(children=markdown_text)
])