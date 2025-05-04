import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Aviation Data Analysis Dashboard", layout="wide")

# Display current working directory for debug
st.write("Current Working Directory:", os.getcwd())

# Title
st.title("Aviation Data Analysis Dashboard")

# Load Data
df = pd.read_csv("dataset.csv")

# Sidebar Filters
st.sidebar.header("Filters")

# Overview
st.header("1. Dataset Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isnull().sum().sum())

if st.checkbox("Show Dataset Info"):
    st.text(df.info())

if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Nationality Analysis
st.header("2. Passenger Demographics")
nation_count = df["Nationality"].value_counts().reset_index()
nation_count.columns = ["Nationality", "Count"]
top_10 = nation_count.head(10)

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x="Nationality", y="Count", data=top_10, palette="coolwarm", ax=ax1)
ax1.set_title("Top 10 Nationalities")
ax1.set_xlabel("Nationality")
ax1.set_ylabel("Passenger Count")
plt.xticks(rotation=45)
st.pyplot(fig1)

# More Visuals Section (Add as needed)
st.header("3. Further Visual Insights")
col_plot = st.selectbox("Select Column to Visualize", df.select_dtypes(include=['object', 'category']).columns)

fig2, ax2 = plt.subplots()
df[col_plot].value_counts().head(10).plot(kind="bar", ax=ax2, color="skyblue")
ax2.set_title(f"Top 10 {col_plot}")
ax2.set_ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Download Option
st.header("4. Download Data")
st.download_button("Download Cleaned Dataset", data=df.to_csv(index=False), file_name="cleaned_airline_data.csv", mime="text/csv")
