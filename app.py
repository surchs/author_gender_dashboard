import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import html, dcc

external_stylesheets = [dbc.themes.FLATLY, "assets/styles.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Author gender distribution"
server = app.server


# Getting the data
gender_ratio_year_table = pd.read_csv('assets/gender_ratio_table.csv')

fig = px.choropleth(gender_ratio_year_table, locations="iso",
                    color="ratio", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma,
                    animation_frame="year",
                    range_color=(0, 5),
                    height=800
                   )

figure_box = dcc.Graph(
    id="worldmap",
    figure=fig,
)

figure_card = dbc.Card(
    [
        dbc.CardHeader(html.H3("Gender ratio of first authors")),
        dbc.CardBody(
            [
                dbc.Row(dbc.Col(figure_box)),
            ]
        ),
    ]
)


app.layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(figure_card),
                    ]
                ),
            ],
            fluid=True,
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8060)