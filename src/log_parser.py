import pandas as pd

def parse_logs(filepath="data/synthetic_logs.csv"):
    try:
        df = pd.read_csv(filepath)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return pd.DataFrame()

if __name__ == '__main__':
    logs = parse_logs()
    print(logs.head())
