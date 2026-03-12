# app.py
import streamlit as st
import pandas as pd
from PIL import Image
import os

# ------------------------------
# Page config
# ------------------------------
st.set_page_config(
    page_title="DashMancer Portfolio",
    layout="wide"
)

# ------------------------------
# Load custom CSS
# ------------------------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("🚀 DashMancer Portfolio")
project = st.sidebar.radio(
    "📂 Select Project:",
    ["🛒 Superstore", "🚗 Toyota", "🍲 Recipe Traffic"]
)

# ------------------------------
# Superstore Project
# ------------------------------
if project == "🛒 Superstore":
    st.header("🛒 Superstore Sales Analysis")
    st.markdown(
        "📌 **Project Summary:** This analysis identifies the top-performing regions and product categories, helping management focus on high-impact sales areas."
    )

    df = pd.read_csv("superstore/superstore_sales.csv")

    # Key metrics
    st.subheader("📊 Key Metrics")
    top_region_sales = df.groupby("Region")["Sales"].sum().idxmax()
    top_region_profit = df.groupby("Region")["Profit"].sum().idxmax()
    total_orders = df.shape[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("Top Region by Sales", top_region_sales)
    col2.metric("Top Region by Profit", top_region_profit)
    col3.metric("Total Orders", total_orders)

    # CSV preview
    st.subheader("📋 Data Preview")
    st.dataframe(df.head(10))

    # Charts in rows of 3
    st.subheader("🖼 Charts")
    chart_files = sorted([f for f in os.listdir("superstore/results") if f.endswith(".png")])
    for i in range(0, len(chart_files), 3):
        cols = st.columns(3)
        for j, chart_file in enumerate(chart_files[i:i+3]):
            img = Image.open(f"superstore/results/{chart_file}")
            cols[j].image(img, caption=chart_file, use_column_width=True)

    # Collapsible code
    with st.expander("📜 View Superstore Code"):
        with open("superstore/analysis.py") as f:
            code = f.read()
        st.code(code, language="python")

# ------------------------------
# Toyota Project
# ------------------------------
elif project == "🚗 Toyota":
    st.header("🚗 Toyota Used Car Analysis")
    st.markdown(
        "📌 **Project Summary:** Explores the UK Toyota used car market, focusing on hybrid share, pricing trends, and vehicle type distributions."
    )

    df = pd.read_csv("Toyota/toyota.csv")

    # Key metrics
    st.subheader("📊 Key Metrics")
    total_cars = df.shape[0]
    if "fuelType" in df.columns:
        hybrid_sales = df[df["fuelType"] == "Hybrid"].shape[0]
        hybrid_share = round(hybrid_sales / total_cars * 100, 1)
    else:
        hybrid_share = "N/A"

    col1, col2 = st.columns(2)
    col1.metric("Total Cars", total_cars)
    col2.metric("Hybrid Share (%)", f"{hybrid_share}%")

    # CSV preview
    st.subheader("📋 Data Preview")
    st.dataframe(df.head(10))

    # Charts in rows of 3
    st.subheader("🖼 Charts")
    chart_files = sorted([f for f in os.listdir("Toyota/Results") if f.endswith(".png")])
    for i in range(0, len(chart_files), 3):
        cols = st.columns(3)
        for j, chart_file in enumerate(chart_files[i:i+3]):
            img = Image.open(f"Toyota/Results/{chart_file}")
            cols[j].image(img, caption=chart_file, use_column_width=True)

    # GitHub link
    st.markdown(
        "[📂 View Toyota Notebook on GitHub](https://github.com/MattPollockUK/Toyota-Dataset-for-used-cars)"
    )

# ------------------------------
# Recipe Traffic Project
# ------------------------------
elif project == "🍲 Recipe Traffic":
    st.header("🍲 Recipe Traffic Prediction")
    st.markdown(
        "📌 **Project Summary:** Predicts recipe page traffic, evaluates category performance, and visualizes model results."
    )

    df = pd.read_csv("Traffic_Recipe/recipe.csv")

    # Key metrics
    st.subheader("📊 Key Metrics")
    total_pages = df.shape[0]
    col1 = st.columns(1)[0]
    col1.metric("Total Pages", total_pages)

    # CSV preview
    st.subheader("📋 Data Preview")
    st.dataframe(df.head(10))

    # Charts in rows of 3
    st.subheader("🖼 Charts")
    chart_files = sorted([f for f in os.listdir("Traffic_Recipe/Results") if f.endswith(".png")])
    for i in range(0, len(chart_files), 3):
        cols = st.columns(3)
        for j, chart_file in enumerate(chart_files[i:i+3]):
            img = Image.open(f"Traffic_Recipe/Results/{chart_file}")
            cols[j].image(img, caption=chart_file, use_column_width=True)

    # GitHub link
    st.markdown(
        "[📂 View Recipe Traffic Notebook on GitHub](https://github.com/MattPollockUK/recipe-traffic-prediction)"
    )