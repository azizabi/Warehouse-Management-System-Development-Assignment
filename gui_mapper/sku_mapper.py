import pandas as pd
import re
import logging
from typing import Optional

# Setup basic logging
logging.basicConfig(filename='sku_mapper.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class SKUMapper:
    def __init__(self, mapping_input):
        if isinstance(mapping_input, pd.DataFrame):
            self.mapping_df = mapping_input
        else:
            self.mapping_file = mapping_input
            self.mapping_df = self.load_mapping()

    def load_mapping(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.mapping_file)
            df = df.rename(columns=lambda x: x.strip().lower())
            logging.info("Mapping file loaded successfully.")
            return df
        except Exception as e:
            logging.error(f"Failed to load mapping file: {e}")
            raise

    def map_sku(self, sku: str) -> Optional[str]:
        if not isinstance(sku, str):
            return None

        sku_clean = sku.strip().upper()

        # Handle single SKU mapping
        row = self.mapping_df[
            (self.mapping_df['sku'].str.upper() == sku_clean)
        ]
        if not row.empty:
            return row.iloc[0]['msku']

        # Handle combo products (e.g., "SKU1+SKU2")
        if '+' in sku_clean:
            parts = sku_clean.split('+')
            mapped = []
            for part in parts:
                msku = self.map_sku(part)
                if msku:
                    mapped.append(msku)
                else:
                    logging.warning(f"Missing mapping for part: {part}")
                    return None
            return '+'.join(mapped)

        # If no match found
        logging.warning(f"SKU not found in mapping: {sku}")
        return None

    def map_dataframe(self, df: pd.DataFrame, sku_column: str = 'sku') -> pd.DataFrame:
        df['mapped_msku'] = df[sku_column].apply(self.map_sku)
        return df
