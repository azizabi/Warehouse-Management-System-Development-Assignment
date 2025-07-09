import pandas as pd
import os

def detect_marketplace(cols):
    cols = [c.strip().lower() for c in cols]
    if 'msku' in cols and 'fnsku' in cols:
        return 'Amazon'
    elif 'order item id' in cols and 'sku' in cols:
        return 'Flipkart'
    elif 'sub order no' in cols and 'sku' in cols:
        return 'Meesho'
    return 'Unknown'

def standardize_sales(file_path):
    df = pd.read_csv(file_path)
    original_columns = df.columns.tolist()
    df.columns = df.columns.str.strip().str.lower()

    platform = detect_marketplace(original_columns)

    if platform == 'Amazon':
        df['sku'] = df['title'].str.strip().str.upper()
        df['quantity'] = df['quantity']
        df['order_date'] = df['date']
    elif platform == 'Flipkart':
        df['sku'] = df['sku'].str.strip().str.upper()
        df['quantity'] = df['quantity']
        df['order_date'] = df['ordered on']
    elif platform == 'Meesho':
        df['sku'] = df['sku'].str.strip().str.upper()
        df['quantity'] = df['quantity']
        df['order_date'] = df['order date']
    else:
        raise Exception(f"Unknown platform format for: {file_path}")

    df['marketplace'] = platform

    return df[['sku', 'quantity', 'order_date', 'marketplace']]

# Test
if __name__ == "__main__":
    TEST_FILE = 'data/raw_sales/CSTE_AMAZON/270142020122.csv'  # replace as needed
    df = standardize_sales(TEST_FILE)
    print(df.head())
