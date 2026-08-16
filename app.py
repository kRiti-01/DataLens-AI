import streamlit as st
import pandas as pd

#from analysis.profiler import dataset_overview
from analysis.cleaner import missing_values, duplicate_rows, missing_value_percentage
from analysis.outliers import detect_outliers

st.set_page_config(
    page_title="DataLens AI",
    layout="wide"
)
st.title("📊 DataLens AI")
uploaded_file=st.file_uploader(
    "Upload CSV",
    type=["CSV"]
)
if uploaded_file:
    df= pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    #dataset_overview(df)
    missing_values(df)
    missing_value_percentage(df)
    duplicate_rows(df)
    detect_outliers(df)