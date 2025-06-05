import streamlit as st


import pandas as pd

st.set_page_config(page_title="Data Viz", page_icon="📈", layout="wide")
if "expand_code" not in st.session_state:
    st.session_state.expand_code = False


def show_code(lines_of_code):
    with st.expander("See Python Code", expanded=st.session_state.expand_code):
        st.code(lines_of_code, language="python")


with st.sidebar:
    on = st.toggle("Show Code")
    if on:
        st.session_state.expand_code = True
    else:
        st.session_state.expand_code = False


st.markdown(
    """
# Data Visualization of seaborn-data
Analyzing mpg.csv data from seaborn-data dataset: https://github.com/mwaskom/seaborn-data/blob/master/mpg.csv

I am using Plotly and Streamlit for this task.
"""
)

show_code(
    """
mpg_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/mpg.csv')
# or read from local_path../mpg.csv
st.dataframe(mpg_data.head(10))
"""
)

mpg_data = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/mpg.csv"
)
st.dataframe(mpg_data.head(10))
st.markdown("---")

st.markdown("## Reading and cleaning dataset")
st.markdown(
    """### Initial Observation
The car dataset has many models of cars produced across different years. The origin and engine performance metrics are listed out.
"""
)
st.markdown(
    """
### Check for missing values
"""
)

col1, col2 = st.columns(spec=[0.3, 0.7])

with col1:

    st.markdown("```mpg_data.isna().sum()```")
    st.dataframe(mpg_data.isna().sum())

with col2:

    temp = mpg_data[mpg_data.isna().any(axis=1)]
    selected_column = "horsepower"
    df_styled = temp.style.set_properties(
        subset=[selected_column], **{"background-color": "#FF474C"}
    )
    st.markdown("```mpg_data[mpg_data.isna().any(axis=1)]```")
    st.dataframe(df_styled)


st.markdown("### Drop/Impute Data")
st.markdown(
    "Since there are not many rows that contain null values in horsepower that are not the extremes, I decided to simply drop these data."
)
show_code("mpg_data.dropna(inplace=True)")

mpg_data.dropna(inplace=True)
mpg_data["horsepower"] = pd.to_numeric(mpg_data["horsepower"])


st.markdown(
    """
## Summary of the Data
"""
)

show_code("st.dataframe(mpg_data.describe())")
st.dataframe(mpg_data.describe())
