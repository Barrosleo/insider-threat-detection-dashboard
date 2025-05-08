# insider threat detection and anomaly dashboard

this project simulates the aggregation of synthetic siem and user activity logs to detect abnormal behavior that might indicate an insider threat. the solution applies anomaly detection, visualizes events with an interactive dashboard, and generates an incident report summarizing suspicious activity.

## key features
- data aggregation from simulated sources (file access, system logins, email logs)
- anomaly detection using machine learning (IsolationForest)
- interactive dashboard for timeline and alert visualization (built with dash and plotly)
- automated report generation for incident response

## usage
1. use github codespaces or the web editor to edit and run the project.
2. install dependencies from `requirements.txt`.
3. run the application with:
python src/main.py

## repository structure
insider-threat-detection-dashboard/
├── README.md
├── requirements.txt
├── docs/
│   └── incident_report.json
├── data/
│   └── synthetic_logs.csv
└── src/
    ├── main.py
    ├── log_generator.py
    ├── log_parser.py
    ├── anomaly_detector.py
    ├── dashboard.py
    └── report_generator.py


