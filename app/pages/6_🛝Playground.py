import streamlit as st

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from Data_exploration import mpg_data

st.write(mpg_data.isna().any())

st.set_page_config(page_title="Playground", page_icon="🛝", layout="wide")

st.plotly_chart(
    px.scatter(data_frame=mpg_data, x="horsepower", y="mpg", color="model_year")
)


st.markdown("---")

if "selected" not in st.session_state:
    st.session_state.selected = "mpg"
col_names = mpg_data.columns

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
