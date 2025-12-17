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

    html.Button("Load Data", id="load-btn", style={"marginLeft": "20px"}, n_clicks=0),

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
    if n == 0:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update
    raw_data = wu.get_weather(city)
    df = wu.convert_to_df(raw_data)

    # Create indivual charts
    temp_fig = px.line(
        df, x="datetime", y="temp",
        title=f"{city} - Temperature",
        labels={"datetime": "Date/Time", "temp": "Temperature (°C)"}
    )

    humidity_fig = px.line(
        df, x="datetime", y="humidity",
        title=f"{city} - Humidity",
        labels={"datetime": "Date/Time", "humidity": "Humidity (%)"}
    )

    wind_fig = px.line(
        df, x="datetime", y="wind",
        title=f"{city} - Wind Speed",
        labels={"datetime": "Date/Time", "wind": "Wind Speed (m/s)"}
    )

    # Compute stats 
    stats_txt=""
    for label,metric in METRIC.items():
        stats = wu.compute_stats(df, metric)
        stats_txt += (
            f"{label}\n" 
            f"Max: {stats["max"]} at {stats["max_time"]}\n"
            f"Min: {stats["min"]} at {stats["min_time"]}\n"
            f"Avg: {stats["mean"]}\n"
            f"Perentage Change: {stats["percent_change"]}%\n\n"
        )

    return temp_fig, wind_fig, humidity_fig, stats_txt

### App Execution ###
if __name__ == "__main__":
    app.run(debug=True)