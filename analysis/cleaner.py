import streamlit as st
import pandas as pd
def missing_values(df):

    st.header("Missing Values")

    missing = df.isnull().sum()

    missing = missing[missing>0]

    if missing.empty:

        st.success("No Missing Values")

    else:

        st.dataframe(missing)

def duplicate_rows(df):

    st.header("Duplicate Rows")

    duplicates = df.duplicated().sum()

    st.metric(
        "Duplicate Rows",
        duplicates
    )
def missing_value_percentage(df):
    st.header("Missing Value Percentage")

    percentage = (df.isnull().sum() / len(df) * 100).round(2)

    result = pd.DataFrame({
        "Missing Values": df.isnull().sum(),
        "Missing %": percentage
    })

    st.dataframe(result)

    high_missing = result[result["Missing %"] > 30]

    if not high_missing.empty:
        st.warning("Some columns have more than 30% missing values.")
        st.dataframe(high_missing)