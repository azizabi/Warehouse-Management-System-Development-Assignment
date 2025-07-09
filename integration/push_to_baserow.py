import requests
import pandas as pd

# Baserow credentials
API_TOKEN = "GaYDC6VGdwXqXbWjcuyWNZOik7GlnszL"
DATABASE_ID = 254308
TABLE_ID = 601212

API_URL = f"https://api.baserow.io/api/database/rows/table/{TABLE_ID}/"

HEADERS = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json"
}

# Mapping Baserow field names to their IDs
FIELD_IDS = {
    "msku": "field_4870530",
    "sku": "field_4870531"
}

def push_to_baserow(df: pd.DataFrame):
    success_count = 0
    failed_rows = []

    for _, row in df.iterrows():
        data = {
            FIELD_IDS["msku"]: str(row.get("mapped_msku", "")).strip(),
            FIELD_IDS["sku"]: str(row.get("sku", "")).strip()
        }

        response = requests.post(API_URL, headers=HEADERS, json={"fields": data})
        if response.status_code == 200 or response.status_code == 201:
            success_count += 1
        else:
            failed_rows.append({"row": row.to_dict(), "error": response.text})

    return success_count, failed_rows
