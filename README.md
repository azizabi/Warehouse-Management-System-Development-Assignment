# 📦 Warehouse Management System (WMS) - Assignment Submission

This project is a Minimum Viable Product (MVP) for a **Warehouse Management System (WMS)**. It enables users to map SKUs to MSKUs, visualize sales data, and push results to a relational database (Baserow).

---

## 🔧 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python (Pandas, Altair, Requests)
* **Database:** Baserow\.io (as a relational Airtable alternative)
* **AI Tools:** ChatGPT (prompt engineering, code generation assistance)

---

## 📂 Project Structure

```
warehouse-management-system/
├── gui_mapper/
│   └── streamlit_app.py        # Main Streamlit App
├── integration/
│   ├── fetch_from_baserow.py  # Fetch mappings from Baserow
│   └── push_to_baserow.py     # Push mapped results to Baserow
├── data/
│   └── mappings/              # Local CSVs (optional)
├── sku_mapper.py              # SKU → MSKU mapping logic
├── standardize_sales.py       # Standardize input sales data
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## ✅ Features Implemented

### Part 1: Data Cleaning & Mapping

* Upload CSV sales data from Amazon/Meesho
* Standardize sales input columns
* Map SKU to MSKU using:

  * Local CSV (`msku_sku_mapping.csv`)
  * Live Baserow fetch
* Preview and download mapped output

### Part 2: Relational Database

* Baserow\.io database:

  * `MSKU Mapping` table
  * `Sales Data` table
* Linked using the `sku` → `Sales Data` relationship

### Part 3: Streamlit Web App

* Upload file via GUI
* Metrics displayed:

  * Total Quantity
  * Top 5 MSKUs
  * Marketplace Distribution
* Charts:

  * Bar (Top MSKUs)
  * Pie (Marketplace breakdown)
* Push mapped data to Baserow via API

### Part 4: AI Over Data Layer

* Future scope: Add [Lumina AI](https://lumina-app.vercel.app/) / SQL-to-text layer for querying Baserow data

---

## 🚀 How to Run

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the Streamlit app
streamlit run gui_mapper/streamlit_app.py
```

---

## 🔑 Baserow Configuration

Update your `integration/fetch_from_baserow.py` and `push_to_baserow.py` with:

```python
API_TOKEN = "your_token_here"
BASE_ID = 254308
TABLE_ID = 601212
```

---

## ✉️ Submission Details

* **Name:** Abinesh
* **Assignment:** WMS Development MVP
* **GitHub:** [https://github.com/azizabi/Warehouse-Management-System-Development-Assignment](https://github.com/azizabi/Warehouse-Management-System-Development-Assignment)

---

## 🙏 Special Thanks

Thanks to **CSTE** for this practical assignment. Also grateful for AI tools like **ChatGPT** that helped accelerate development.
