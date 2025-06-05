import streamlit as st
import pandas as pd

from data.dataframe import mpg_data

st.set_page_config(page_title="Initial Analysis", page_icon="🔍", layout="wide")
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


st.markdown("# Extreme values: Max and Min")

st.markdown(
    "Observe the maximum and minimum extremeties of data and also observe the data to get to know what data we have at hand. For this data, we have different cars, which were produced form 1970 to 1982."
)

show_code(
    """mpg_data.loc[mpg_data["horsepower"] == mpg_data["horsepower"].max()]
mpg_data.loc[mpg_data["horsepower"] == mpg_data["horsepower"].min()]
mpg_data.loc[mpg_data["acceleration"] == mpg_data["acceleration"].max()]
mpg_data.loc[mpg_data["acceleration"] == mpg_data["acceleration"].min()]
mpg_data.loc[mpg_data["mpg"] == mpg_data["mpg"].max()]
mpg_data.loc[mpg_data["mpg"] == mpg_data["mpg"].min()]
mpg_data.loc[mpg_data["model_year"] == mpg_data["model_year"].max()]
mpg_data.loc[mpg_data["model_year"] == mpg_data["model_year"].min()]
mpg_data.loc[mpg_data["cylinders"] == 3]"""
)


selected_column = st.selectbox(
    "Field", options=["horsepower", "mpg", "acceleration", "model_year"]
)

if selected_column == "model_year":
    st.write("Newest cars")
else:
    st.write("Max value for:", selected_column)
st.dataframe(mpg_data.loc[mpg_data[selected_column] == mpg_data[selected_column].max()])

if selected_column == "model_year":
    st.write("Oldest cars")
else:
    st.write("Min value for:", selected_column)
st.dataframe(mpg_data.loc[mpg_data[selected_column] == mpg_data[selected_column].min()])


cylinder_val = st.slider("No of cylinders:", max_value=8, min_value=3, value=4)
if not cylinder_val == 7:
    series = (
        mpg_data.loc[mpg_data["cylinders"] == cylinder_val]
        .sort_values(by="horsepower", ascending=False)
        .iloc[0]
    )
    st.dataframe(pd.DataFrame([series]))
else:
    st.write("No Cars with 7 cylinders!")

st.markdown("---")
st.markdown("# Cars in the Dataset")

col1, col2 = st.columns(spec=[0.5, 0.5])
with col1:
    st.image(
        image="assets/1977_mazda_rx-4.jpg",
        caption="Powerful 3 cylinder car: 1977 Mazda RX-4",
    )
    st.image(
        image="assets/1980_mazda_rx-7.jpg",
        caption="Newer gen 3 cylinder car: 1980 Mazda RX-7",
    )
    st.image(image="assets/audi_5000.jpg", caption="Powerful 5 cylinder car: Audi 5000")
    st.image(
        image="assets/buick_regal_sport_coupe.jpg",
        caption='Powerful 6 cylinder car: Buick Regal Sport "coupe"',
    )
    st.image(image="assets/saab_99le.jpg", caption="Powerful 4 cylinder car: Saab 91LE")
with col2:
    st.image(
        image="assets/harvester_intl_1200D.png",
        caption="Least fuel efficient in the dataset: Harvester Intl 1200D",
    )
    st.image(
        image="assets/mazda_glc.png",
        caption="Most fuel efficient in the dataset: Mazda GLC",
    )
    st.image(
        image="assets/pontiac_GP.jpg",
        caption="Highest Horsepower in the dataset: Pontiac GP",
    )
    st.image(
        image="assets/pugeot_504.png",
        caption="Highest Acceleration in the dataset: Pugeot 504",
    )
