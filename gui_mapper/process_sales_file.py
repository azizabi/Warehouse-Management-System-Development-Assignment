import os
import pandas as pd
from sku_mapper import SKUMapper

# === CONFIGURATIONS === #
MAPPING_FILE = 'data/mappings/sku_msku_mapping.xlsx'  # your master mapping sheet
SALES_FILE = 'data/raw_sales/CSTE AMAZON/270142020122.csv'         # sample sales file to process
OUTPUT_FOLDER = 'output/'
SKU_COLUMN_NAME = 'sku'                                # make sure the sales file has this column

def main():
    # Check if output folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Step 1: Load sales CSV
    try:
        sales_df = pd.read_csv(SALES_FILE)
        print(f"Loaded sales file: {SALES_FILE}")
    except Exception as e:
        print(f"Error loading sales file: {e}")
        return

    # Step 2: Create mapper object
    try:
        mapper = SKUMapper(MAPPING_FILE)
    except Exception as e:
        print(f"Error loading mapping file: {e}")
        return

    # Step 3: Map SKUs to MSKUs
    mapped_df = mapper.map_dataframe(sales_df, sku_column=SKU_COLUMN_NAME)

    # Step 4: Export to output folder
    output_file = os.path.join(OUTPUT_FOLDER, f"mapped_{os.path.basename(SALES_FILE)}")
    mapped_df.to_csv(output_file, index=False)
    print(f"Mapped data saved to: {output_file}")

if __name__ == "__main__":
    main()
