import json
from datetime import datetime

def generate_report(df):
    """
    Generates a JSON report summarizing the incident detection results.
    """
    total_events = len(df)
    total_anomalies = len(df[df['anomaly'] == -1])
    anomaly_details = df[df['anomaly'] == -1].to_dict(orient="records")
    
    report = {
        "report_generated": datetime.now().isoformat(),
        "total_events": total_events,
        "total_anomalies": total_anomalies,
        "anomaly_details": anomaly_details
    }
    return json.dumps(report, indent=4)

if __name__ == '__main__':
    from log_parser import parse_logs
    from anomaly_detector import detect_anomalies
    logs = parse_logs("data/synthetic_logs.csv")
    _, df_with_anomaly = detect_anomalies(logs)
    report = generate_report(df_with_anomaly)
    print(report)
