import sys
import os
import streamlit as st
import pandas as pd
import altair as alt

# Add integration directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sku_mapper import SKUMapper
from standardize_sales import standardize_sales
from integration.fetch_from_baserow import fetch_msku_mapping
from integration.push_to_baserow import push_to_baserow

# Page config
st.set_page_config(page_title="WMS Mapper", layout="wide")
st.title("📦 Warehouse Management System — SKU to MSKU Mapper")

# File upload
uploaded_file = st.file_uploader("📤 Upload your sales CSV file", type=["csv"])

if uploaded_file:
    try:
        # Show uploaded data preview
        raw_df = pd.read_csv(uploaded_file)
        st.subheader("📄 Raw Data Preview")
        st.dataframe(raw_df.head(10))

        # Save temporarily to disk (required by standardizer)
        temp_path = "temp_uploaded_file.csv"
        raw_df.to_csv(temp_path, index=False)

        # 1️⃣ Standardize
        df_standard = standardize_sales(temp_path)

        # 2️⃣ Fetch MSKU mapping from Baserow
        df_mapping = fetch_msku_mapping()

        # 3️⃣ Perform mapping
        mapper = SKUMapper(df_mapping)
        mapped_df = mapper.map_dataframe(df_standard, sku_column='sku')

        # ✅ Show mapped result
        st.subheader("✅ Mapped Data")
        st.dataframe(mapped_df.head(20))

        # 💾 Download Mapped CSV
        st.subheader("📥 Download Mapped CSV")
        csv = mapped_df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Mapped CSV", csv, file_name="mapped_output.csv", mime="text/csv")

        # 📊 Summary Metrics
        st.subheader("📊 Summary Metrics")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📟 Total Orders", len(mapped_df))
        with col2:
            st.metric("📦 Total Quantity", int(mapped_df['quantity'].sum()))
        with col3:
            st.metric("🔁 Unique MSKUs", mapped_df['mapped_msku'].nunique())

        # 🏆 Top 5 MSKUs
        st.subheader("🏆 Top 5 MSKUs by Quantity")
        top_5 = mapped_df.groupby('mapped_msku')['quantity'].sum().nlargest(5).reset_index()
        st.dataframe(top_5)

        bar_chart = alt.Chart(top_5).mark_bar().encode(
            x=alt.X('mapped_msku:N', title='MSKU'),
            y=alt.Y('quantity:Q', title='Quantity'),
            color='mapped_msku:N',
            tooltip=['mapped_msku', 'quantity']
        ).properties(width=600, height=400)
        st.altair_chart(bar_chart)
               # 🚀 Push to Baserow
        st.subheader("🔗 Sync to Baserow")
        if st.button("🚀 Push Mapped Data to Baserow"):
            with st.spinner("Uploading to Baserow..."):
                success, failed = push_to_baserow(mapped_df)
                st.success(f"✅ Successfully pushed {success} rows to Baserow.")
                if failed:
                    st.warning(f"⚠️ {len(failed)} rows failed to upload.")

        # 🌍 Orders by Marketplace
        st.subheader("🌍 Orders by Marketplace")
        marketplace_counts = (
            mapped_df['marketplace'].value_counts()
            .reset_index().rename(columns={'index': 'marketplace', 'marketplace': 'orders'})
        )
        st.dataframe(marketplace_counts)

        # Clean data types
        marketplace_counts['marketplace'] = marketplace_counts['marketplace'].astype(str)
        marketplace_counts['orders'] = pd.to_numeric(marketplace_counts['orders'], errors='coerce').fillna(0)

        pie_chart = alt.Chart(marketplace_counts).mark_arc().encode(
            theta=alt.Theta(field="orders", type="quantitative"),
            color=alt.Color(field="marketplace", type="nominal"),
            tooltip=["marketplace", "orders"]
        ).properties(width=500, height=400)
        st.altair_chart(pie_chart)

 

    except Exception as e:
        st.error(f"❌ Failed to process file: {e}")
