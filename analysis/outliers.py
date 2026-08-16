import streamlit as st

import numpy as np

def detect_outliers(df):

    st.header("Outlier Detection")

    numeric = df.select_dtypes(include=np.number)

    if numeric.empty:

        st.info("No Numeric Columns")

        return

    result = {}

    for col in numeric.columns:

        q1 = numeric[col].quantile(.25)

        q3 = numeric[col].quantile(.75)

        iqr = q3-q1

        lower = q1-1.5*iqr

        upper = q3+1.5*iqr

        outliers = numeric[
            (numeric[col]<lower)|
            (numeric[col]>upper)
        ]

        result[col]=len(outliers)

    st.dataframe(result.items())