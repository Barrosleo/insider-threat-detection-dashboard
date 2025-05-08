from log_generator import generate_logs
from log_parser import parse_logs
from anomaly_detector import detect_anomalies
from dashboard import create_dashboard
from report_generator import generate_report
import os

def main():
    # ensure necessary directories exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    
    # generate synthetic logs (if you want to refresh the data)
    df_generated = generate_logs(200)
    df_generated.to_csv("data/synthetic_logs.csv", index=False)
    print("Synthetic logs generated.")
    
    # parse logs from csv
    logs = parse_logs("data/synthetic_logs.csv")
    print("Parsed logs:", len(logs), "records.")
    
    # apply anomaly detection
    anomalies, logs_with_anomaly_info = detect_anomalies(logs)
    print("Anomaly detection complete. Found", len(anomalies), "anomalies.")
    
    # generate report and save to docs
    report = generate_report(logs_with_anomaly_info)
    with open("docs/incident_report.json", "w") as f:
        f.write(report)
    print("Incident report saved to docs/incident_report.json")
    
    # launch the interactive dashboard
    app = create_dashboard(logs_with_anomaly_info)
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
