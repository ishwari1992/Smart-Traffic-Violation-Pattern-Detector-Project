import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

# --- Constants ---
BASE_DIR = Path(__file__).parent
DEFAULT_DATA_PATH = Path(r"D:\Streamlit_Pro_Code\data\Indian_Traffic_Violations.csv")
ASSETS_DIR = BASE_DIR / "assets"

st.set_page_config(page_title="Smart Traffic Violation Pattern Detector",
                   layout="wide",
                   page_icon=":oncoming_police_car:")

# --- FIXED DATA LOADER ---
@st.cache_data
def load_data(file):
    if file is not None and hasattr(file, "read"):
        df = pd.read_csv(file, low_memory=False)

    elif file is None:
        if DEFAULT_DATA_PATH.exists():
            df = pd.read_csv(DEFAULT_DATA_PATH, low_memory=False)
        else:
            st.error(f"Default dataset not found: {DEFAULT_DATA_PATH}")
            return pd.DataFrame()

    else:
        file = Path(file)
        if not file.exists():
            st.error(f"Dataset not found at: {file}")
            return pd.DataFrame()
        df = pd.read_csv(file, low_memory=False)

    df = df.drop_duplicates()

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        if df["Date"].notna().sum() > 0:
            df["Day"] = df["Date"].dt.day_name()
            df["Month"] = df["Date"].dt.month_name()
            df["Hour"] = df["Date"].dt.hour

    if "Time" in df.columns:
        try:
            df["Time"] = pd.to_datetime(df["Time"], errors="coerce").dt.time
        except:
            pass

    return df

# SIDEBAR
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Dashboard"])

st.sidebar.subheader("Dataset Upload")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

df = load_data(uploaded_file if uploaded_file else None)

if not df.empty:
    st.sidebar.write(f"**Rows:** {df.shape[0]} | **Cols:** {df.shape[1]}")

# HELPER PLOTS
def plot_violations_by_day(df):
    fig, ax = plt.subplots(figsize=(10, 4))
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if "Day" not in df.columns:
        ax.text(0.5, 0.5, "Day column missing", ha="center")
        return fig

    vc = df["Day"].value_counts().reindex(order).fillna(0)
    vc.plot(kind="bar", ax=ax, color="skyblue")
    ax.set_title("Violations by Day")
    return fig

def plot_violations_by_hour(df):
    fig, ax = plt.subplots(figsize=(10, 4))

    if "Hour" not in df.columns:
        ax.text(0.5, 0.5, "Hour column missing", ha="center")
        return fig

    vc = df["Hour"].value_counts().sort_index()
    vc.plot(kind="bar", ax=ax, color="orange")
    ax.set_title("Violations by Hour")
    return fig
# --- HOME PAGE ---
if page == "Home":
    st.title("Smart Traffic Violation Pattern Detector")

    img = ASSETS_DIR / "T03.jpg"
    if img.exists():
        st.image(str(img), width='stretch')

    if df.empty:
        st.info("Upload a dataset to begin.")
    else:
        st.metric("Total Records", df.shape[0])
# DASHBOARD PAGE
elif page == 'Dashboard':
    st.title('Dashboard')

    category = st.selectbox(
        'Select category',
        [
            'Overview',
            'Violation Types',
            'Hotspots',
            'Payment & Fines',
            'Weather & Conditions',
            'Vehicle_Type VS Fine_Amount',
            'Average Fine per Location'
        ]
    )
    if df.empty:
        st.warning('Please upload or load the dataset first.')
    else:
        # --- Overview ---
        if category == 'Overview':
            col1, = st.columns(1)

            with col1:
                st.subheader('Top 10 Violation Types')

                if 'Violation_Type' in df.columns:
                    topn = df['Violation_Type'].value_counts().head(10)
                    st.bar_chart(topn)
                else:
                    st.error("Violation_Type column missing.")

                st.subheader('Top 5 Locations')

                if 'Location' in df.columns:
                    top_locations = df['Location'].value_counts().head(5).reset_index()
                    top_locations.columns = ['Location', 'Count']

                    # Auto-fit column width
                    st.dataframe(
                        top_locations,
                        width='stretch',   # Makes it responsive
                        hide_index=True,
                    )
                else:
                    st.error("Location column missing.")

        # --- Violation Types ---
        elif category == 'Violation Types':
            st.subheader('Most Common Violation Types')

            if 'Violation_Type' in df.columns:
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.countplot(y='Violation_Type', data=df,
                              order=df['Violation_Type'].value_counts().index[:20])
                st.pyplot(fig)
            else:
                st.info('Violation_Type column missing')

        # --- Hotspots ---
        elif category == 'Hotspots':
            st.subheader('Top Hotspots')

            if 'Location' in df.columns:
                top_locations = df['Location'].value_counts().head(10)
                st.bar_chart(top_locations)

               
            else:
                st.info('Location column missing')

        # --- Payment & Fines ---
        elif category == 'Payment & Fines':
            st.subheader('Fine distribution')

            if 'Fine_Amount' in df.columns:

                # --- Histplot with separated bars + KDE line ---
                fig, ax = plt.subplots(figsize=(8, 4))
                sns.histplot(
                    df['Fine_Amount'].dropna(),
                    bins=60,
                    kde=True,
                    edgecolor="black",  # separates the bars clearly
                    linewidth=0.5,
                    ax=ax
                )
                ax.set_xlabel('Fine Amount')
                ax.set_ylabel('Density-Count')
                ax.set_title('Fine Amount Distribution (with KDE)')
                st.pyplot(fig)

                # --- Bar chart: Fine Amount by Vehicle Type ---
                st.subheader('Fine Amount by Vehicle Type')

                if 'Vehicle_Type' in df.columns:
                    fines = (
                        df.groupby('Vehicle_Type')['Fine_Amount']
                        .sum()
                        .sort_values(ascending=False)
                    )
                    st.bar_chart(fines)
                else:
                    st.info('Vehicle_Type column missing')

            else:
                st.info('Fine_Amount column missing')


        # --- Weather ---
        elif category == 'Weather & Conditions':
            st.subheader('Violations by Weather Condition')

            if 'Weather_Condition' in df.columns:
                fig, ax = plt.subplots(figsize=(6,4))
                sns.countplot(y='Weather_Condition', data=df,
                              order=df['Weather_Condition'].value_counts().index)
                st.pyplot(fig)
            else:
                st.info('Weather_Condition column missing')

        # --- Pie Chart: Vehicle Type vs Fine ---
        elif category == 'Vehicle_Type VS Fine_Amount':
            st.subheader("Vehicle Type vs Total Fine Amount (Pie Chart)")

            if 'Vehicle_Type' not in df.columns or 'Fine_Amount' not in df.columns:
                st.error("Vehicle_Type or Fine_Amount column missing.")
            else:
                fine_data = df.groupby('Vehicle_Type')['Fine_Amount'].sum()

                fig, ax = plt.subplots(figsize=(2.5,2.5))
                ax.pie(
                    fine_data.values,
                    labels=fine_data.index,
                    autopct='%1.1f%%',
                    startangle=45
                )
                ax.set_title("Vehicle Type vs Fine Amount")
                st.pyplot(fig)

        # --- Line Chart: Average Fine per Location ---
        elif category == 'Average Fine per Location':
            st.subheader("Average Fine per Location (Line Chart)")

            if 'Location' not in df.columns or 'Fine_Amount' not in df.columns:
                st.error("Location or Fine_Amount column is missing.")
            else:
                df_temp = df[['Location', 'Fine_Amount']].copy()
                df_temp['Fine_Amount'] = pd.to_numeric(
                    df_temp['Fine_Amount'].astype(str).str.replace(r'[^\d\.\-]', '', regex=True),
                    errors='coerce'
                )
                df_temp = df_temp.dropna(subset=['Location', 'Fine_Amount'])

                if df_temp.empty:
                    st.info("No valid data available after cleaning.")
                else:
                    avg_fine = df_temp.groupby('Location')['Fine_Amount'].mean().sort_values()

                    fig, ax = plt.subplots(figsize=(12, 6))
                    ax.plot(avg_fine.index, avg_fine.values, marker='o', linewidth=2)

                    ax.set_title("Average Fine per Location")
                    ax.set_xlabel("Location")
                    ax.set_ylabel("Average Fine Amount")
                    plt.xticks(rotation=90)
                    plt.tight_layout()

                    st.pyplot(fig)

                    st.write("### Top 10 Locations by Highest Average Fine")
                    st.table(avg_fine.sort_values(ascending=False).head(10).rename("Average Fine"))
st.sidebar.markdown("---")
