import streamlit as st

import plotly.express as px

from data.dataframe import mpg_data

st.set_page_config(page_title="Multivariate", page_icon="📈", layout="wide")
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


st.markdown("# Multivariate Analysis")
st.markdown("## CORRELATION HEATMAP")


correlation = mpg_data.select_dtypes("number").corr("pearson")
st.plotly_chart(
    px.imshow(
        correlation, text_auto=True, color_continuous_scale="thermal", aspect="auto"
    )
)


st.markdown(
    """The correlation heatmaps confirms the relation between **cylinder, displacement, horsepower and weight.**
We also see that these affect mpg negatively as expected.

We can also see that there is a fair relationship between mpg and model years, meaning newer models tend to be fuel efficient.

But then acceleration is negatively proportional to cylinder, displacement, horsepower and weight, which is still unexplained.
Whats more, there is a weakly positive relation between acceleration and mpg meaning higher acceleration gives better mileage, which is not logical.

Now for a more better understanding, we can take more than two variables in a graph:
"""
)

ins1, ins2, ins3, ins4 = st.tabs(
    [
        "🐎hp vs mpg⛽/ year",
        "🏋️weight vs mpg⛽/ year",
        "🐎hp vs acclr🏎️/ year",
        "🏋️weight vs acclr🏎️/ hp",
    ]
)
with ins1:
    st.plotly_chart(
        px.scatter(data_frame=mpg_data, x="horsepower", y="mpg", color="model_year")
    )
    st.markdown(
        "From this plot we can confirm that newer models are more efficient than the older ones. However, we can see that the newer models also have lower horsepower."
    )

with ins2:
    st.plotly_chart(
        px.scatter(data_frame=mpg_data, x="weight", y="horsepower", color="model_year")
    )
    st.markdown(
        """With this graph we find that heavier models are all older models, which also have a lot of horse power. The newer models are not only fuel efficient but are lighter and provide lower power output.

    This raises a questions as why the companies would build such cars with low power and weight but better fuel efficiency?"""
    )

with ins3:
    st.plotly_chart(
        px.scatter(
            data_frame=mpg_data, x="horsepower", y="acceleration", color="model_year"
        )
    )
    st.markdown(
        "This tells us almost all new models have low horse power but high acceleration. Even though there were some older models that had low horsepower/high acceleration."
    )

with ins4:
    st.plotly_chart(
        px.scatter(
            data_frame=mpg_data,
            x="weight",
            y="acceleration",
            color="horsepower",
            color_continuous_scale="temps",
        )
    )
    st.markdown(
        "Higher horsepower cars are almost always rather heavy with lower acceleration."
    )


cyl = (
    mpg_data.groupby("model_year")
    .aggregate(avg_no_of_cylinders=("cylinders", "mean"), avg_mpg=("mpg", "mean"))
    .reset_index()
)
st.plotly_chart(
    px.scatter(
        data_frame=cyl,
        x="model_year",
        y="avg_no_of_cylinders",
        color="avg_mpg",
        trendline="ols",
    )
)


st.markdown("Newer cars have fewer no of cylinders on average.")
