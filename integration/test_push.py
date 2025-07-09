import pandas as pd
from push_to_baserow import push_to_baserow

# Dummy mapped DataFrame for testing
data = {
    "sku": ["CSTE_0545_ST_Animal_Breathing_Dog_B_2", "Breathing_Lilo_Stich_Blue"],
    "mapped_msku": ["MSKU123", "MSKU124"]
}

df = pd.DataFrame(data)

success, failed = push_to_baserow(df)
print(f"✅ Success: {success}")
if failed:
    print("❌ Failed rows:")
    for f in failed:
        print(f)
