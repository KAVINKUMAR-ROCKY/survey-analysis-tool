import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from io import BytesIO

st.set_page_config(page_title="Survey Analysis Tool", layout="wide")

st.title("📊 Survey Analysis and Visualization Tool")

uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.subheader("📋 Data Preview")
        st.dataframe(df.head(10))

        column = st.selectbox("Choose a column to analyze", df.columns)

        if df[column].dtype in ['object', 'bool']:
            st.subheader("📊 Bar Chart")
            count_data = df[column].value_counts()
            st.bar_chart(count_data)

            st.subheader("🥧 Pie Chart")
            fig1, ax1 = plt.subplots()
            ax1.pie(count_data, labels=count_data.index, autopct='%1.1f%%', startangle=90)
            st.pyplot(fig1)
        else:
            st.subheader("📈 Histogram")
            fig2, ax2 = plt.subplots()
            sns.histplot(df[column], kde=True, ax=ax2)
            st.pyplot(fig2)

            st.subheader("📊 Statistical Summary")
            st.write(f"**Mean:** {np.mean(df[column])}")
            st.write(f"**Median:** {np.median(df[column])}")
            st.write(f"**Mode:** {df[column].mode()[0]}")
            st.write(f"**Standard Deviation:** {np.std(df[column])}")
            st.write(f"**Min:** {np.min(df[column])}")
            st.write(f"**Max:** {np.max(df[column])}")

    except Exception as e:
        st.error(f"Error: {e}")
