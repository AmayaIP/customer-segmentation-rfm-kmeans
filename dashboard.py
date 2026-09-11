import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")


df = pd.read_csv('rfm_segmented.csv')

st.title("Customer Segmentation Dashboard")
st.markdown("RFM Analysis + K-Means Clustering")


col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", len(df))
col2.metric("Total Revenue", f"₹{df['Monetary'].sum():,.0f}")
col3.metric("Avg Order Value", f"₹{df['Monetary'].mean():,.0f}")

st.divider()


segments = st.multiselect("Filter by Segment", options=df['Segment'].unique(), default=df['Segment'].unique())
filtered_df = df[df['Segment'].isin(segments)]


col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Count by Segment")
    fig1 = px.bar(filtered_df['Segment'].value_counts().reset_index(), x='Segment', y='count')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Revenue by Segment")
    revenue_by_segment = filtered_df.groupby('Segment')['Monetary'].sum().reset_index()
    fig2 = px.pie(revenue_by_segment, names='Segment', values='Monetary')
    st.plotly_chart(fig2, use_container_width=True)

st.divider()


st.subheader("Recency vs Frequency vs Monetary")
fig3 = px.scatter(filtered_df, x='Recency', y='Frequency', size='Monetary', color='Segment', hover_data=['Monetary'])
st.plotly_chart(fig3, use_container_width=True)

st.divider()


st.subheader("Customer Data")
st.dataframe(filtered_df)


st.divider()
st.subheader("Recommendations")

recommendations = {
    "Champions": "Give loyalty rewards, early access to new products, VIP treatment.",
    "New Customers": "Send welcome offers, onboarding discounts to build habit.",
    "At-Risk Customers": "Send personalized win-back offers, special discount to bring them back.",
    "Lost Customers": "Try re-engagement campaign, big discount or survey to understand why they left."
}

for seg in filtered_df['Segment'].unique():
    st.markdown(f"**{seg}**: {recommendations.get(seg, '')}")