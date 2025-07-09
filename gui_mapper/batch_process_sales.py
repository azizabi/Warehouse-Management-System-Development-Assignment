import os
import pandas as pd
from standardize_sales import standardize_sales
from sku_mapper import SKUMapper

# Paths
RAW_FOLDER = "data/raw_sales"
MAPPING_FILE = "data/mappings/msku_sku_mapping.csv"
OUTPUT_FOLDER = "output"

def process_all_files():
    # Load SKUMapper
    mapper = SKUMapper(MAPPING_FILE)

    # Loop through all CSVs in raw_sales
    for filename in os.listdir(RAW_FOLDER):
        if filename.endswith(".csv"):
            file_path = os.path.join(RAW_FOLDER, filename)
            print(f"🟡 Processing {filename}...")

            try:
                df = standardize_sales(file_path)
                df_mapped = mapper.map_dataframe(df, sku_column='sku')

                output_file = os.path.join(OUTPUT_FOLDER, f"mapped_{filename}")
                os.makedirs(OUTPUT_FOLDER, exist_ok=True)
                df_mapped.to_csv(output_file, index=False)
                print(f"✅ Saved: {output_file}")
            except Exception as e:
                print(f"❌ Failed to process {filename}: {e}")

if __name__ == "__main__":
    process_all_files()
