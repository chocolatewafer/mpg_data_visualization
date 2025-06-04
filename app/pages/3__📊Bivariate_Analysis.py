import streamlit as st

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from Data_exploration import mpg_data, color_map

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

st.markdown("## Bivariate analysis")

show_code(
    """
px.scatter(data_frame=mpg_data, x='cylinders', y = 'origin', color= 'origin')
px.scatter(data_frame=mpg_data, x='model_year', y='mpg',facet_col='origin')
avg_group = pd.DataFrame()
avg_group = mpg_data.groupby(by='model_year').agg(average_mpg = ('mpg', 'mean'))
avg_group.reset_index()
px.line(data_frame=avg_group,  y='average_mpg')"""
)

st.plotly_chart(
    px.scatter(
        data_frame=mpg_data,
        x="cylinders",
        y="origin",
        color="origin",
        color_discrete_map=color_map,
    )
)


st.markdown(
    """
In the dataset, US based cars have a higher count of cylinders, while Japanese and European cars have lower cylinders, but innovate in 3 cylinder or 5 cylinder engines.
This might be due to racing being more poular and prevalant in the US or due to road networks being better in the US with consumer culture demanding more powerful cars.
"""
)


st.plotly_chart(
    px.scatter(data_frame=mpg_data, x="model_year", y="mpg", facet_col="origin")
)
st.markdown(
    "A trend of mpg getting better across the years can be seen in all the countries."
)

avg_group = pd.DataFrame()
avg_group = mpg_data.groupby(by="model_year").agg(average_mpg=("mpg", "mean"))
avg_group.reset_index()
st.plotly_chart(px.line(data_frame=avg_group, y="average_mpg"))

st.markdown(
    "Getting the ***average mpg*** for models that came out each year across all countries shows that there is actually a steady **increase** in the fuel efficiency across the years."
)


st.markdown(
    "### Getting names of company to see the Distribution of Car according to company"
)

show_code(
    """
def get_first_name(x):
    full_name = x.split(" ")
    company = full_name[0]
    return company
mpg_data["company"] = mpg_data["name"].apply(lambda x: get_first_name(x))
company_hist = px.histogram(data_frame=mpg_data, x="company")
company_hist.show()
"""
)


def get_first_name(x):
    full_name = x.split(" ")
    company = full_name[0]
    return company


mpg_data["company"] = mpg_data["name"].apply(lambda x: get_first_name(x))
st.plotly_chart(px.histogram(data_frame=mpg_data, x="company"))


show_code(
    """
country_df= mpg_data.groupby('company').agg(mean_mpg = ('mpg','mean'))
country_df.reset_index().sort_values(by='mean_mpg', ascending=False).head()

country_df = mpg_data.groupby("company").agg(mean_horsepower=("horsepower", "mean"))
country_df.reset_index().sort_values(by="mean_horsepower", ascending=False).head()
"""
)

country_df = mpg_data.groupby("company").agg(mean_mpg=("mpg", "mean"))
st.dataframe(
    country_df.reset_index().sort_values(by="mean_mpg", ascending=False).head()
)


country_df = mpg_data.groupby("company").agg(mean_horsepower=("horsepower", "mean"))
st.dataframe(
    country_df.reset_index().sort_values(by="mean_horsepower", ascending=False).head()
)

st.markdown(
    """
Company based breakdown shows Volkswagen has a good fuel efficiency on average.
Similary Harvester International has a pretty high horse power, which makes sense as it is a truck.
The US companies like Chrysler and Caldillac have very high horsepower cars on general
"""
)


st.markdown("# Bivariate Analysis of Numerical Data")


st.markdown(
    "To gain proper insigts and explore, I wrote code to plot all values vs all other values."
)


col_names = [
    "mpg",
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "model_year",
]
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


st.markdown(
    """
### Observations: others vs Miles per Gallon(mpg)

From these graphs, we can make a number of Observations.
- A trend that shows more number of cylinders reduces fuel efficiency.
- Higher horsepower,displacement and weight show lower fuel efficiency.
- Acceleration and mpg do not have a obvious relationship due to a highly scattered plot. We do see a proportional trend, which is quite counter intuitive.
- As the years progress, cars are getting more fuel efficient.

---

### Observations: others vs Cylinders

We can see that more number of **cylinder** means higher **horse power**, more **displacement** and also a **heavier engine**.

There is no clear relationship between the model year and the number of cylinders, indicating that cars with varying engine types were produced across all years.

Checking out the **4 cylinder** engines, we observe that they give great fuel efficiency with light engines but with lower horse power. This could also mean they are both cheaper to manufacture and to use. This could explain why there are greater number of cars with 4 cylinder engines produced.

We can not however, say for sure that these 4 cylinder cars are the most poular or most bought cars though. For that, we would need the sales data of these models to be certain.
**6 cylinder engines** have a good balance of efficiency and horsepower. **8 cylinder engines** pack a punch with higher horsepower but guzzle a lot of fuel. The **8 cylinder** engines are some of the most powerful engines with very high horsepower. This makes sense as more cylinders will displace more fuel, producing more power but meaning lower fuel efficiency. At the same time bigger and heavier engines are needed to accomodate more number of cylinders.

---

### Observation: others vs horsepower &  others vs displacement

We can see the relationships between weight, displacement and horsepower, i.e

**more displacement &rarr; more horsepower**
**more displacement &rarr; more weight**
meaning **higher horsepower** engines are **heavier** like we observed before.

The relationshoip between acceleration and displacement and acceleration and horsepower is negatively proportional though. This is rather counter intuitive as you might think cars having higher horsepower/displacement should provide higher acceleration as well. But that is not the case at all.

What we can also see is that newer models have lower horsepower.
To make more sense out of this we can create a correlation heatmap and perform further multivariate analysis.
"""
)
