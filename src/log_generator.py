import pandas as pd
import random
import datetime

def generate_logs(num_records=100):
    systems = ['file', 'login', 'email']
    users = ['alice', 'bob', 'charlie', 'dave']
    activities = {
        'file': ['file_read', 'file_write'],
        'login': ['login-success', 'login-failure'],
        'email': ['normal-email', 'phishing-email']
    }
    
    logs = []
    for _ in range(num_records):
        system = random.choice(systems)
        user = random.choice(users)
        activity = random.choice(activities[system])
        # simulate a numeric score; higher values indicate suspicious activity
        base_score = random.randint(10, 50)
        # add extra weight if the activity is particularly suspicious
        if activity in ["login-failure", "phishing-email"]:
            base_score += random.randint(30, 50)
        log = {
            "timestamp": datetime.datetime.now().isoformat(),
            "system": system,
            "user": user,
            "activity": activity,
            "activity_score": base_score
        }
        logs.append(log)
    return pd.DataFrame(logs)

if __name__ == '__main__':
    df = generate_logs(10)
    print(df.head())
