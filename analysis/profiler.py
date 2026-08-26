import streamlit as st

def dataset_overview(df):

    st.header("Dataset Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Rows", df.shape[0])

    c2.metric("Columns", df.shape[1])

    memory = df.memory_usage(deep=True).sum()/1024

    c3.metric("Memory (KB)", round(memory,2))

    st.write("### Data Types")

    st.dataframe(df.dtypes.astype(str))