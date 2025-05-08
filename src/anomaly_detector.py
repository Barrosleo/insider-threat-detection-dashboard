from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df):
    """
    Uses IsolationForest to detect anomalous events.
    Adds a new column 'anomaly' where -1 indicates an anomaly and 1 means a normal event.
    Returns a tuple of (anomalies, full dataframe with anomaly info).
    """
    # Use only the numeric feature for anomaly detection
    X = df[['activity_score']]
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)
    
    # Predict anomalies: -1 = anomaly, 1 = normal
    df['anomaly'] = model.predict(X)
    anomalies = df[df['anomaly'] == -1]
    return anomalies, df

if __name__ == '__main__':
    import pandas as pd
    from log_parser import parse_logs
    logs = parse_logs("data/synthetic_logs.csv")
    anomalies, df_with_anomaly = detect_anomalies(logs)
    print("Anomalies detected:")
    print(anomalies)
