import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# ----------------------------
# Parameters
# ----------------------------
num_users = 500
min_sessions = 1
max_sessions = 5
start_date = datetime(2026, 3, 1, 8, 0)
end_date = datetime(2026, 3, 10, 22, 0)

devices = ['mobile', 'desktop', None]  # introduce missing
countries = ['IT', 'ES', 'FR', 'DE', None]  # introduce missing
user_types = ['new', 'returning']
categories = ['Clothing', 'Electronics', 'Accessories', 'Home', 'Sports',
              'clothing', 'ACCESSORIES', None]  # inconsistencies + missing

event_probabilities = {
    'page_view': 1.0,
    'product_view': 0.7,
    'add_to_cart': 0.25,
    'checkout': 0.2,
    'purchase': 0.15
}

# ----------------------------
# Helper functions
# ----------------------------
def random_timestamp(start, end):
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

def generate_session_events(user_id, session_id, start_time):
    events = []
    current_time = start_time

    if random.random() <= event_probabilities['page_view']:
        events.append(['page_view', 'homepage', random.choice([None, "homepage"]), current_time])

        if random.random() <= event_probabilities['product_view']:
            category = random.choice(categories)
            current_time += timedelta(seconds=random.randint(10,90))
            events.append(['product_view', 'product_page', category, current_time])

            if random.random() <= event_probabilities['add_to_cart']:
                current_time += timedelta(seconds=random.randint(10,90))
                events.append(['add_to_cart', 'product_page', category, current_time])

                if random.random() <= event_probabilities['checkout']:
                    current_time += timedelta(seconds=random.randint(10,90))
                    events.append(['checkout', 'checkout', None, current_time])

                    if random.random() <= event_probabilities['purchase']:
                        current_time += timedelta(seconds=random.randint(10,90))
                        events.append(['purchase', 'confirmation', category, current_time])
    return events

# ----------------------------
# Generate dataset
# ----------------------------
data = []

for user_id in range(1, num_users+1):
    user_type = np.random.choice(user_types, p=[0.7, 0.3])
    device = np.random.choice(devices, p=[0.55, 0.35, 0.1])
    country = np.random.choice(countries, p=[0.45,0.2,0.15,0.15,0.05])
    
    num_user_sessions = random.randint(min_sessions, max_sessions)
    for s in range(1, num_user_sessions+1):
        session_id = f"s{user_id:03d}_{s}"
        session_start = random_timestamp(start_date, end_date)
        session_events = generate_session_events(user_id, session_id, session_start)
        for evt in session_events:
            data.append([
                str(user_id),
                str(session_id),
                evt[0],  # event
                evt[1],  # page
                evt[2],  # category (may be None)
                evt[3],  # timestamp
                device,
                country,
                user_type
            ])

# ----------------------------
# Create DataFrame
# ----------------------------
df = pd.DataFrame(data, columns=[
    'user_id', 'session_id', 'event', 'page', 'category', 'timestamp',
    'device', 'country', 'user_type'
])

# ----------------------------
# Introduce duplicates ~2%
# ----------------------------
duplicates = df.sample(frac=0.02, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

# Shuffle rows to desordenar timestamps
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# ----------------------------
# Save CSV in data/raw/
# ----------------------------
output_dir = os.path.join(os.path.dirname(__file__), "../data/raw")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "ecommerce_dataset_raw_realistic.csv")
df.to_csv(output_path, index=False)

print("Realistic raw dataset generated!")
print("Total events (including duplicates):", len(df))
print("CSV saved at:", output_path)