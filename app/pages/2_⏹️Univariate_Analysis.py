import streamlit as st
import plotly.express as px

from data.dataframe import mpg_data

color_map = {"japan": "#c25553", "europe": "#ed7d31", "usa": "#5b9bd5"}

st.set_page_config(page_title="Univariate", page_icon="⏹️", layout="wide")
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

st.markdown("# Univariate Analysis")
st.markdown("## Graphs and Visualizations")


st.code('px.histogram(data_frame=mpg_data, x="cylinders")', language="python")
st.plotly_chart(px.histogram(data_frame=mpg_data, x="cylinders"))


st.markdown(
    """
We can see from this chart that most Cars are **4, 6** or **8** cylinders. This might be due to even numbers of cylinders providing better manufacturing cost, efficiency or performance, due to which car manufacturers choose this configuration.

A quick search gives us a good overview: [why-arent-there-seven-cylinder-engines](https://carbuzz.com/news/why-arent-there-seven-cylinder-engines/#:~:text=This%20is%20why%20even%20number,perfect%20option%20for%20most%20applications.). It turns out engines with odd configurations are rather unstable and have vibrations, making even configurations preferable for balance and smoothness.

What we can also observe is that we have higher number of 4 cylinder cars in our data. One hypothesis might be that 4 cylinder cars are more fuel efficient. On the contrary it can also be that while 6 and 8 are more fuel efficient, they might be more expensive and hence less sought ought by average buyers.

One final consideration to this line of thinking should be that the data collection might be uneven, giving us this particular distribution of cars; making both of our hypothesis completely invalid.
"""
)


show_code(
    """
    px.box(data_frame=mpg_data.sort_values(by="cylinders"),y=["horsepower"],facet_col="cylinders")
    px.box(data_frame=mpg_data.sort_values(by="cylinders"),y=["horsepower"],facet_col="mpg")
    px.box(data_frame=mpg_data.sort_values(by="cylinders"),y=["horsepower"],facet_col="acceleration")
    """
)

tab1, tab2, tab3 = st.tabs(["Horsepower", "Mpg", "Acceleration"])
tab1.plotly_chart(
    px.box(
        data_frame=mpg_data.sort_values(by="cylinders"),
        y=["horsepower"],
        facet_col="cylinders",
        color="cylinders",
    )
)
tab2.plotly_chart(
    px.box(
        data_frame=mpg_data.sort_values(by="cylinders"),
        y=["mpg"],
        facet_col="cylinders",
        color="cylinders",
    )
)
tab3.plotly_chart(
    px.box(
        data_frame=mpg_data.sort_values(by="cylinders"),
        y=["acceleration"],
        facet_col="cylinders",
        color="cylinders",
    )
)


st.markdown("### Inspecting Outliers")
show_code(
    """
mpg_data[mpg_data.horsepower == 165 ]
mpg_data[mpg_data.horsepower == 230]
mpg_data[(mpg_data.mpg == 38) & (mpg_data.cylinders == 6)]
mpg_data[(mpg_data.mpg == 26.6) & (mpg_data.cylinders == 8)]"""
)


st.markdown(
    """
### Observations

From these two graphs we can have some insights as to how:
- **4 cylinder** cars have lower horsepower but are more fuel efficient.
- **6 cylinder** cars seems to have a balanced horsepower and fuel consumption.
-  On the contrary, **8 cylinder** cars have greater horsepower but are quite fuel hungry in general.

All this seems to be in line with the hypothesis that the 3 and 5 cylinder engines are not very performant, giving relatively low horsepower over average fuel efficiency. The **4 cylinder** cars seem to have a good balance between horsepower and miles per gallon.

### Spread and Outliers

There is a varied mpg and horsepower observed in 8 cylinder cars meaning there are a regular cars and then there are muscle cars giving a greater range of mpgs and horsepowers.

There are some outliers is both mpg and horsepower graphs.

### Muscle Cars
"""
)
with st.popover("High horsepower cars", use_container_width=True):
    df = mpg_data[mpg_data.horsepower > 220]
    st.dataframe(
        df.style.apply(
            lambda x: [
                "background-color: lightgreen; color: black"
                if x.name == "horsepower"
                else ""
                for _ in x
            ]
        )
    )
with st.popover(
    "6 cylinder Buick regal in comparision to other 8 cylinder cars",
    use_container_width=True,
):
    df = mpg_data[mpg_data.horsepower == 165]
    st.dataframe(
        df.style.apply(
            lambda x: [
                "background-color: lightgreen; color: black"
                if x.name == "horsepower"
                else ""
                for _ in x
            ]
        )
    )

st.markdown(
    """
The 6 cylinder **buick regal sport coupe (turbo)** is a muscle car giving a very high horsepower and comes in line with other average 8 cylinder cars. Similarly the 230hp **pontiac grand prix** is a 8 cylinder beast of a muscle car which explains the very high horsepower.

### Efficient Cars
"""
)
with st.popover("6 cylinder cars with good efficiency", use_container_width=True):
    df = mpg_data[(mpg_data.mpg > 30) & (mpg_data.cylinders == 6)]
    st.dataframe(
        df.style.apply(
            lambda x: [
                "background-color: lightgreen; color: black" if x.name == "mpg" else ""
                for _ in x
            ]
        )
    )

with st.popover("8 cylinder cars with good efficiency", use_container_width=True):
    df = mpg_data.loc[(mpg_data.mpg > 20) & (mpg_data.cylinders == 8)]
    st.dataframe(
        df.style.apply(
            lambda x: [
                "background-color: lightgreen; color: black" if x.name == "mpg" else ""
                for _ in x
            ]
        )
    )

st.markdown(
    """
There are certain economy or diesel version of cars that make them exceptionally fuel efficient like the 6 cylinder **oldsmobile cutlass ciera (diesel)** or the 8 cylinder **oldsmobile cutlass ls**

To get a more complete picture, we need to perform further analysis. Let us hence try to gather more insights from our data regarding engine performance with respect to number of cylinders, displacement, weight and country of origin.
"""
)


st.plotly_chart(
    px.histogram(
        data_frame=mpg_data, y="origin", color="origin", color_discrete_map=color_map
    )
)


st.markdown(
    "Seems like most cars in our dataset are **USA** based and there are only two other origins i.e. **Japan** and **Europe**."
)
st.markdown(
    "We can now analyze our cars categoirically based on the countries. Let us see what differences cars of each country possess."
)

orig1, orig2, orig3, orig4 = st.tabs(
    ["Model Year", "Miles Per Gallon", "Acceleration", "Horsepower"]
)

orig1.plotly_chart(
    px.histogram(
        mpg_data,
        x="model_year",
        color="origin",
        marginal="box",
        color_discrete_map=color_map,
        hover_data=mpg_data.columns,
    )
)
orig2.plotly_chart(
    px.histogram(
        mpg_data,
        x="mpg",
        color="origin",
        marginal="box",
        color_discrete_map=color_map,
        hover_data=mpg_data.columns,
    )
)
orig3.plotly_chart(
    px.histogram(
        mpg_data,
        x="acceleration",
        color="origin",
        marginal="box",
        color_discrete_map=color_map,
        hover_data=mpg_data.columns,
    )
)
orig4.plotly_chart(
    px.histogram(
        mpg_data,
        x="horsepower",
        color="origin",
        marginal="box",
        color_discrete_map=color_map,
        hover_data=mpg_data.columns,
    )
)


st.markdown(
    """This shows us that Japanese cars are the most fuel efficient while USA has on average, more powerful cars.
Also worth noting is that USA has a higher fence for hp meaning that there are car variants that are very powerful (muscle cars) which we see lacking in other countires."""
)
