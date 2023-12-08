import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Загрузка данных из файла
df = pd.read_csv('BIBA.txt', parse_dates=['Дата'])

# Создание приложения Dash
app = dash.Dash(__name__)

# Определение макета дашборда
app.layout = html.Div(children=[
    html.H1(children='Анализ солнечной радиации и погоды'),

    dcc.Graph(
        id='radiation-graph',
        figure={
            'data': [
                {'x': df['Дата'], 'y': df['Солнечная радиация'], 'type': 'line', 'name': 'Солнечная радиация'},
            ],
            'layout': {
                'title': 'График солнечной радиации',
                'xaxis': {'title': 'Дата'},
                'yaxis': {'title': 'Солнечная радиация'},
            }
        }
    ),

    dcc.Graph(
        id='temperature-graph',
        figure={
            'data': [
                {'x': df['Дата'], 'y': df['Температура'], 'type': 'line', 'name': 'Температура'},
            ],
            'layout': {
                'title': 'График температуры',
                'xaxis': {'title': 'Дата'},
                'yaxis': {'title': 'Температура'},
            }
        }
    ),

    dcc.Graph(
        id='cloudiness-graph',
        figure=px.bar(df, x='Дата', y='Облачность', title='График облачности')
    ),

    dcc.Graph(
        id='wind-graph',
        figure={
            'data': [
                {'x': df['Облачность'], 'y': df['Температура'], 'type': 'line', 'name': 'Скорость ветра'},
            ],
            'layout': {
                'title': 'График Облачность-Температура',
                'xaxis': {'title': 'Облачность'},
                'yaxis': {'title': 'Температура'},
            }
        }
    ),

    dcc.Graph(
        id='precipitation-graph',
        figure=px.bar(df, x='Солнечная радиация', y='Температура', title='График Солнечная радиация-Температура')
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True)
