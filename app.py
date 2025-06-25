import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Streamlit page setup ---
st.set_page_config(page_title="INTROEXTROAMBI", layout="wide")
st.title("personality synthetic – Powered by Streamlit")

# --- Load dataset from Dataset folder ---
csv_path = os.path.join("Dataset", "personality_synthetic_dataset.csv")

try:
    df = pd.read_csv(csv_path)
    st.success(f"✅ Loaded dataset: {csv_path}")
except FileNotFoundError:
    st.error("❌ Dataset not found. Please check the file name and make sure it's inside the 'Dataset' folder.")
    st.stop()

# --- Data Preview ---
st.subheader("📋 Dataset Preview")
st.dataframe(df.head())

# --- Summary Info ---
st.subheader("📊 Dataset Summary")
st.write("🧾 Shape:", df.shape)
st.write("🧩 Columns:", df.columns.tolist())
st.write("🧠 Data Types:")
st.write(df.dtypes)

# --- Sidebar Filtering for categorical columns ---
st.sidebar.header("🔍 Filter Data")
for col in df.select_dtypes(include=['object', 'category']):
    selected_values = st.sidebar.multiselect(f"Filter by {col}:", df[col].unique())
    if selected_values:
        df = df[df[col].isin(selected_values)]

st.subheader("📌 Filtered Data")
st.dataframe(df)

# --- Visualization Section ---
st.subheader("📉 Visualizations")
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

if numeric_columns:
    chart_type = st.selectbox("Choose Chart Type", ["Histogram", "Box Plot", "Correlation Heatmap"])
    col_x = st.selectbox("Select Numeric Column", numeric_columns)

    if chart_type == "Histogram":
        plt.figure(figsize=(10, 4))
        plt.hist(df[col_x], bins=30, color='lightgreen', edgecolor='black')
        st.pyplot(plt)

    elif chart_type == "Box Plot":
        plt.figure(figsize=(10, 4))
        sns.boxplot(x=df[col_x], color='orange')
        st.pyplot(plt)

    elif chart_type == "Correlation Heatmap":
        plt.figure(figsize=(12, 6))
        sns.heatmap(df[numeric_columns].corr(), annot=True, cmap="YlGnBu", fmt=".2f")
        st.pyplot(plt)
else:
    st.warning("⚠ No numeric columns available for plotting.")