import dash
from dash import dcc, html, dash_table
import plotly.express as px

def create_dashboard(df):
    app = dash.Dash(__name__)
    # Create a scatter plot timeline: x = timestamp, y = activity_score, color indicates anomaly status
    fig = px.scatter(df, x='timestamp', y='activity_score', color=df['anomaly'].apply(lambda x: 'anomaly' if x==-1 else 'normal'),
                     symbol='system', title='Event Timeline with Anomaly Detection')
    
    app.layout = html.Div(children=[
        html.H1("Insider Threat Detection Dashboard"),
        dash_table.DataTable(
            id='log-table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            page_size=10,
        ),
        dcc.Graph(figure=fig)
    ])
    return app

if __name__ == '__main__':
    from log_parser import parse_logs
    from anomaly_detector import detect_anomalies
    logs = parse_logs("data/synthetic_logs.csv")
    _, df_with_anomaly = detect_anomalies(logs)
    app = create_dashboard(df_with_anomaly)
    app.run_server(debug=True)
