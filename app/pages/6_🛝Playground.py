import streamlit as st

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from data.dataframe import mpg_data

st.set_page_config(page_title="Playground", page_icon="🛝", layout="wide")

col_names = [
    "mpg",
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "model_year",
]


ch1, ch2, ch3 = st.columns(spec=[0.3, 0.3, 0.3])

with ch1:
    x = st.selectbox("x-axis", col_names)
with ch2:
    y = st.selectbox("y-axis", col_names)
with ch3:
    color = st.selectbox("colour", [None] + col_names)

st.plotly_chart(px.scatter(data_frame=mpg_data, x=x, y=y, color=color))


st.markdown("---")

if "selected" not in st.session_state:
    st.session_state.selected = "mpg"

selected = st.selectbox("Plot a graph of Others vs:", col_names)
fig = make_subplots(rows=3, cols=2)
subplots = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
i = 0
for name in col_names:
    if selected != name:
        i = i + 1
        row, col = subplots[i - 1]
        graph_name = f"{selected.capitalize()} vs {name.capitalize()}"
        fig.add_trace(
            go.Scatter(
                x=mpg_data[selected],
                y=mpg_data[name],
                mode="markers",
                name=graph_name,
            ),
            row=row,
            col=col,
        )
        fig.update_xaxes(title_text=selected.capitalize(), row=row, col=col)
        fig.update_yaxes(title_text=name.capitalize(), row=row, col=col)
fig.update_layout(
    height=720, width=1080, title_text=f"{selected.capitalize()} vs Others"
)
st.plotly_chart(fig)
