import pandas as pd
import os

# File paths
AMAZON_FILE = 'data/raw_sales/CSTE_AMAZON/270142020122.csv'
OUTPUT_FILE = 'data/mappings/msku_sku_mapping.csv'

def extract_amazon_mapping():
    try:
        df = pd.read_csv(AMAZON_FILE)

        # Print column headers to debug
        print("📌 Columns in file:", df.columns.tolist())

        # Normalize column names
        df.columns = df.columns.str.strip().str.lower()

        if 'msku' not in df.columns or 'title' not in df.columns:
            print("❌ MSKU or Title column not found.")
            return

        # Check how many non-empty MSKU rows exist
        non_empty = df[df['msku'].notna()]
        print(f"✅ Total rows: {len(df)} | Non-empty MSKUs: {len(non_empty)}")

        # Extract mapping
        mapping_df = non_empty[['msku', 'title']].drop_duplicates()
        mapping_df = mapping_df.rename(columns={'title': 'sku'})

        # Format text
        mapping_df['sku'] = mapping_df['sku'].str.strip().str.upper()
        mapping_df['msku'] = mapping_df['msku'].str.strip().str.upper()

        if mapping_df.empty:
            print("⚠️ Mapping DataFrame is empty after processing.")
        else:
            os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
            mapping_df.to_csv(OUTPUT_FILE, index=False)
            print(f"✅ Mapping saved to {OUTPUT_FILE}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    extract_amazon_mapping()
