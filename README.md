# 🛍️ Customer Segmentation using RFM Analysis & K-Means Clustering

An end-to-end data science project that segments e-commerce customers into actionable groups using **RFM Analysis** and **K-Means Clustering**, visualized through an interactive **Streamlit dashboard**.

**🔗 Live Demo:** [customer-segmentation-rfm-kmeans.streamlit.app](https://customer-segmentation-rfm-kmeans-qsrprtzab5uenk9wappzwjc.streamlit.app/)

---

## 📌 Overview

Businesses often treat every customer the same — but a small fraction usually drives most of the revenue. This project analyzes over **1 million e-commerce transactions** to uncover distinct customer segments based on their purchasing behavior, so a business can target each group with the right strategy instead of a one-size-fits-all approach.

## ✨ Key Results

| Metric | Value |
|---|---|
| Transactions analyzed | 1,067,371 → cleaned to 779,425 |
| Unique customers | 5,878 |
| Optimal clusters (K) | 4 (validated via Elbow Method + Silhouette Score) |
| Silhouette Score | 0.365 |
| Revenue concentration | Top 20% of customers ("Champions") drive ~74% of total revenue |

## 🧩 Customer Segments

| Segment | Behavior | Recommended Action |
|---|---|---|
| 🏆 Champions | Recent, frequent, high spenders | Loyalty rewards, early access |
| 🌱 New Customers | Recent but low frequency | Welcome offers, onboarding discounts |
| ⚠️ At-Risk Customers | Haven't purchased in a while, decent past spend | Personalized win-back offers |
| 💤 Lost Customers | Long inactive, low spend | Re-engagement campaigns |

## 🛠️ Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn (K-Means, StandardScaler)
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Dashboard & Deployment:** Streamlit, Streamlit Community Cloud
- **Version Control:** Git, GitHub

## ⚙️ Workflow

```
Raw Transaction Data
      ↓
Data Cleaning (remove nulls, cancellations, duplicates)
      ↓
RFM Feature Engineering (Recency, Frequency, Monetary)
      ↓
Log Transform + StandardScaler
      ↓
K Selection (Elbow Method + Silhouette Score)
      ↓
K-Means Clustering (K=4)
      ↓
Segment Labeling & Business Recommendations
      ↓
Interactive Streamlit Dashboard
```

## 📊 Dataset

**Online Retail II** (UCI Machine Learning Repository / Kaggle) — ~1M transaction records from a UK-based online retailer, Dec 2009–Dec 2011.

## 🚀 Running Locally

```bash
# Clone the repository
git clone https://github.com/AmayaIP/customer-segmentation-rfm-kmeans.git
cd customer-segmentation-rfm-kmeans

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run dashboard.py
```

## 📁 Project Structure

```
customer-segmentation-rfm-kmeans/
├── customer_segmentation.ipynb   # Full analysis: cleaning, RFM, clustering
├── dashboard.py                  # Streamlit dashboard app
├── rfm_segmented.csv             # Final segmented customer data
├── requirements.txt              # Python dependencies
└── README.md
```

## 📈 Dashboard Features

- Real-time filtering by customer segment
- Revenue and customer count breakdown per segment
- Recency vs. Frequency vs. Monetary scatter visualization
- Segment-wise business recommendations

## 🔮 Future Improvements

- Add Customer Lifetime Value (CLV) estimation per segment
- Track segment migration over time (cohort analysis)
- Compare segment revenue contribution as a % of total, visualized directly on dashboard

## 👤 Author

**Amaya I P**
BCA (Data Science) student | Aspiring Data Analyst / Software Developer
[LinkedIn](https://linkedin.com/in/amaya-ip) · [GitHub](https://github.com/AmayaIP)