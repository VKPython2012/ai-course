import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import weather_utils as wu

### Data ###
CITIES = [
    "Ho Chi Minh City", "Hanoi", "Paris", 
    "London", "Shanghai", "Seoul", "Las Vegas"
]

METRIC = {
    "Temperature (°C)" : "temp",
    "Humidity (%)" : "humidity",
    "Wind Speed (m/s)" : "wind"
}

### Application ###
app = dash.Dash(__name__) # Application Object 

app.layout = html.Div([
    html.H1("Weather Trend Explorer!"),

    html.Div([
        html.Label("Select City"),
        dcc.Dropdown(
            id="city-dropdown",
            options=[{
                "label": c, "value": c
            } for c in CITIES],
            value="Ho Chi Minh City",
            clearable=False
        )
    ], style={
        "width":"30%",
        "display":"inline-block"
    }),

    html.Button("Load Data", id="lead-btn", style={"marginLeft": "20px"}, n_clicks=0),

    html.Hr(),

    dcc.Graph(id="temp-chart"),
    dcc.Graph(id="humidity-chart"),
    dcc.Graph(id="wind-chart"),

    html.Div([
        html.H3("Quick Stats"),
        html.Div(id="stats-box", style={"WhiteSpace":"pre-line  "})
    ], style={
        "border": "1px solid #ccc",
        "padding": "15px",
        "borderRadius": "8px",
        "marginTop": "20px",
        "width":"45%",
        "display": "inline-block",
        "verticalAlign":"top"
    })
])


@app.callback(
    Output("temp-chart", "figure"),
    Output("humidity-chart", "figure"),
    Output("wind-chart", "figure"),
    Output("stats-box", "children"),
    Input("load-btn", "n_clicks"),
    State("city-dropdown", "value")
)
def update_weather(n, city):
    pass



### App Execution ###
if __name__ == "__main__":
    app.run(debug=True)