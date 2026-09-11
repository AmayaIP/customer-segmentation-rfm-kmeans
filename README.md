# Customer Segmentation using RFM Analysis and K-Means Clustering

## Overview
This project segments e-commerce customers into actionable groups using RFM (Recency, Frequency, Monetary) analysis and K-Means clustering. An interactive Streamlit dashboard visualizes the segments and provides business recommendations for each group.

## Live Demo
🔗 [View Dashboard](https://customer-segmentation-rfm-kmeans-qsrprtzab5uenk9wappzwjc.streamlit.app/)

## Dataset
Online Retail II (UCI/Kaggle) — ~1M UK-based online retail transactions (Dec 2009 – Dec 2011).

## Workflow
1. Data cleaning (removed nulls, cancelled orders, duplicates)
2. RFM calculation (Recency, Frequency, Monetary per customer)
3. Log transform + StandardScaler to handle skew
4. Optimal K selection using Elbow Method and Silhouette Score (K=4)
5. K-Means clustering
6. Segment labeling: Champions, New Customers, At-Risk Customers, Lost Customers
7. Interactive Streamlit dashboard with filters, charts, and business recommendations

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Plotly, Streamlit

## Business Value
Identifies high-value customers, flags at-risk/lost customers for re-engagement, and enables targeted marketing strategy per segment.