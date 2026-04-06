E-commerce Data Analytics Pipeline

Overview

This project builds an end-to-end data analytics pipeline using Python on an e-commerce dataset.

It covers:

- Data ingestion (Kaggle API)
- Data cleaning and preprocessing
- Data transformation and merging
- Business insights generation
- Data visualization

---

Project Structure

ecommerce-data-pipeline/

│── data/
│ ├── raw/
│ ├── cleaned/

│── src/
│ ├── ingest.py
│ ├── analyze.py
│ ├── transform.py
│ ├── insights.py
│ ├── visualize.py

│── reports/
│ (saved graphs)

│── README.md
│── requirements.txt

---

Technologies Used

- Python
- Pandas
- Matplotlib
- Kaggle API

---

Pipeline Steps

1. Data Ingestion

Dataset is downloaded using Kaggle API into "data/raw".

2. Data Cleaning

- Missing values handled
- Datetime columns converted
- New features created (delivery time, month, year)

3. Data Transformation

- Multiple datasets merged
- Final dataset created

4. Business Insights

- Total revenue
- Monthly revenue trends
- Top cities by revenue
- Top customers
- Delivery performance

5. Visualization

- Monthly revenue trend (line chart)
- Top cities (bar chart)
- Delivery time distribution (histogram)
- Top customers (bar chart)

---

How to Run

Install dependencies:
pip install -r requirements.txt

Run pipeline:
python src/ingest.py
python src/analyze.py
python src/transform.py
python src/insights.py
python src/visualize.py

---

Output

- Cleaned datasets → "data/cleaned/"
- Graphs → "reports/"

---

Result

This project demonstrates a complete Python-based data pipeline that converts raw e-commerce data into business insights and visual reports.
