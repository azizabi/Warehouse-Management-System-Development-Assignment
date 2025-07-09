import requests
import pandas as pd

# === CONFIG ===
API_TOKEN = "GaYDC6VGdwXqXbWjcuyWNZOik7GlnszL"
TABLE_ID = 601212
URL = f"https://api.baserow.io/api/database/rows/table/{TABLE_ID}/?user_field_names=true"

HEADERS = {
    "Authorization": f"Token {API_TOKEN}"
}

def fetch_msku_mapping():
    all_rows = []
    next_url = URL

    while next_url:
        response = requests.get(next_url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"❌ Failed to fetch: {response.text}")

        data = response.json()
        all_rows.extend(data['results'])
        next_url = data.get('next')

    # Convert to DataFrame
    df = pd.DataFrame(all_rows)
    return df[['msku', 'sku']]

# Run standalone
if __name__ == "__main__":
    df = fetch_msku_mapping()
    print(df.head())
