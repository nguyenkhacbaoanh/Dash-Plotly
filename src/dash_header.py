import dash
import dash_core_components as dcc
import dash_html_components as html

import dash_daq as daq

tab = html.Div(className='Header', id='tabs', children=[
    html.Button(className='tab', id='tab-1', children=[
        html.Div(className='indicators', id='indicator-1', children=[
            daq.Indicator(className='indicator', label='A', value=True, color='#00cc96'),
            daq.Indicator(className='indicator', label='B', value=True, color='#22dd96'),
            daq.Indicator(className='indicator', label='C', value=True, color='#55ee96'),
        ]),
    ]),
    html.Button(className='tab', id='tab-2', children=[
        html.Div(className='indicators', id='indicator-2', children=[
            daq.Indicator(className='indicator', label='A', value=True, color='#00cc96'),
            daq.Indicator(className='indicator', label='B', value=True, color='#22dd96'),
            daq.Indicator(className='indicator', label='C', value=True, color='#55ee96'),
        ]),
    ]),
    html.Button(className='tab', id='tab-3', children=[
        html.Div(className='indicators', id='indicator-3', children=[
            daq.Indicator(className='indicator', label='A', value=True, color='#00cc96'),
            daq.Indicator(className='indicator', label='B', value=True, color='#22dd96'),
            daq.Indicator(className='indicator', label='C', value=True, color='#55ee96'),
        ])
    ]),
])