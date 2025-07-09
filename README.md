# 📦 Warehouse Management System (WMS) - Assignment Submission

This project is a Minimum Viable Product (MVP) for a **Warehouse Management System (WMS)**. It enables users to map SKUs to MSKUs, visualize sales data, and push results to a relational database (Baserow).

---

## 🔧 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python (Pandas, Altair, Requests)
* **Database:** Baserow\.io (as a relational Airtable alternative)
* **AI Tools:** ChatGPT (prompt engineering, code generation assistance)

---
🧠 Why Streamlit for This Project?
While I primarily applied for a Full Stack Developer (MERN) role, this assignment leaned heavily into data processing, transformation, and visualization. Here's why I chose to implement it using Streamlit:

⚙️ Streamlit vs React — Purpose Matters
Feature	✅ Streamlit	🔄 React + Express
Built For	Rapid data apps and internal tools	Complex UI apps and user-facing experiences
Language	Python	JavaScript (React) + Backend (Node/Express)
File Uploads, CSV Handling	Native support	Requires manual file handling logic
Data Visualization	Built-in support with Altair, Plotly, etc.	Needs Chart.js, Recharts, etc.
Time to MVP	Extremely fast	Slower, needs separate API and frontend setup
Backend Integration	Direct Python functions and scripts	Requires API layer and state management

🧩 Why Streamlit was the Best Fit:
The project focused on data cleaning, SKU–MSKU mapping, and interactive dashboards.

I could directly use Python libraries like pandas, altair, and requests for fast development.

It saved time and let me focus more on the core problem-solving, rather than setting up boilerplate frontend/backend code.

✅ Although this was my first time working on a Data Analytics–focused project, I ensured that my solution was clean, modular, and user-friendly — showcasing my problem-solving ability and tech adaptability.

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
