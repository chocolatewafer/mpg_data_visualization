import streamlit as st


import pandas as pd
import plotly as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from skimage import io

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
    selected_column = st.selectbox("", options="horsepower")
    df_styled = temp.style.set_properties(
        subset=[selected_column], **{"background-color": "#FF474C"}
    )
    st.markdown("```mpg_data[mpg_data.isna().any(axis=1)]```")
    st.dataframe(df_styled)


st.markdown("### Drop/Impute Data")
st.markdown(
    "Since there are not many rows that contain null values in horsepower that are not the extremes, I decided to simply drop these data."
)
st.markdown("```mpg_data.dropna(inplace=True)```")

mpg_data.dropna(inplace=True)
mpg_data["horsepower"] = pd.to_numeric(mpg_data["horsepower"])


st.markdown(
    """
## Summary of the Data
"""
)

st.code("st.dataframe(mpg_data.describe())", language="python")
st.dataframe(mpg_data.describe())


show_code(
    """mpg_data.loc[mpg_data["horsepower"] == mpg_data["horsepower"].max()]
mpg_data.loc[mpg_data["acceleration"] == mpg_data["acceleration"].max()]
mpg_data.loc[mpg_data["mpg"] == mpg_data["mpg"].max()]
mpg_data.loc[mpg_data["mpg"] == mpg_data["mpg"].min()]
mpg_data.loc[mpg_data["cylinders"] == 3]"""
)
st.markdown(
    """```mpg_data.loc[mpg_data['horsepower'] == mpg_data['horsepower'].max()]```"""
)
st.markdown(
    """```mpg_data.loc[mpg_data['acceleration'] == mpg_data['acceleration'].max()]```"""
)
st.markdown("""```mpg_data.loc[mpg_data['mpg'] == mpg_data['mpg'].max()]```""")
st.markdown("""```mpg_data.loc[mpg_data['mpg'] == mpg_data['mpg'].min()]```""")
st.markdown("""```mpg_data.loc[mpg_data['cylinders']==3]```""")

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.markdown(
        """```mpg_data.loc[mpg_data['cylinders']==3].sort_values(by= 'horsepower',ascending=False).iloc[0]```"""
    )
    mpg_data.loc[mpg_data["cylinders"] == 3].sort_values(
        by="horsepower", ascending=False
    ).iloc[0]
with c2:
    st.markdown(
        """```mpg_data.loc[mpg_data['cylinders']==4].sort_values(by= 'horsepower',ascending=False).iloc[0]```"""
    )
    mpg_data.loc[mpg_data["cylinders"] == 4].sort_values(
        by="horsepower", ascending=False
    ).iloc[0]
with c3:
    st.markdown(
        """```mpg_data.loc[mpg_data['cylinders']==5].sort_values(by= 'horsepower',ascending=False).iloc[0]```"""
    )
    mpg_data.loc[mpg_data["cylinders"] == 5].sort_values(
        by="horsepower", ascending=False
    ).iloc[0]
with c4:
    st.markdown(
        """```mpg_data.loc[mpg_data['cylinders']==6].sort_values(by= 'horsepower',ascending=False).iloc[0]```"""
    )
    mpg_data.loc[mpg_data["cylinders"] == 6].sort_values(
        by="horsepower", ascending=False
    ).iloc[0]
with c5:
    st.markdown(
        """```mpg_data.loc[mpg_data['cylinders']==8].sort_values(by= 'horsepower',ascending=False).iloc[0]```"""
    )
    mpg_data.loc[mpg_data["cylinders"] == 8].sort_values(
        by="horsepower", ascending=False
    ).iloc[0]


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


st.code(
    """px.box(
        data_frame=mpg_data.sort_values(by="cylinders"),
        y=["horsepower"],
        facet_col="cylinders",
    )""",
    language="python",
)
st.plotly_chart(
    px.box(
        data_frame=mpg_data.sort_values(by="cylinders"),
        y=["horsepower"],
        facet_col="cylinders",
    )
)


st.code(
    px.box(
        data_frame=mpg_data.sort_values(by="cylinders"),
        y=["mpg"],
        facet_col="cylinders",
    ),
    language="python",
)
st.plotly_chart(
    px.box(
        data_frame=mpg_data.sort_values(by="cylinders"),
        y=["mpg"],
        facet_col="cylinders",
    )
)


# ### Inspecting Outliers


st.dataframe(mpg_data[mpg_data.horsepower == 165])


mpg_data[mpg_data.horsepower == 230]


mpg_data[(mpg_data.mpg == 38) & (mpg_data.cylinders == 6)]


mpg_data[(mpg_data.mpg == 26.6) & (mpg_data.cylinders == 8)]


### Observations
st.markdown(
    """
From these two graphs we can have some insights as to how:
- **4 cylinder** cars have lower horsepower but are more fuel efficient.
- **6 cylinder** cars seems to have a balanced horsepower and fuel consumption.
-  On the contrary, **8 cylinder** cars have greater horsepower but are quite fuel hungry in general.

All this seems to be in line with the hypothesis that the 3 and 5 cylinder engines are not very performant, giving relatively low horsepower over average fuel efficiency. The **4 cylinder** cars seem to have a good balance between horsepower and miles per gallon.

### Spread and Outliers

There is a varied mpg and horsepower observed in 8 cylinder cars meaning there are a regular cars and then there are muscle cars giving a greater range of mpgs and horsepowers.

There are some outliers is both mpg and horsepower graphs.

### Muscle Cars
The 6 cylinder **buick regal sport coupe (turbo)** is a muscle car giving a very high horsepower and comes in line with other average 8 cylinder cars. Similarly the 230hp **pontiac grand prix** is a 8 cylinder beast of a muscle car which explains the very high horsepower.

### Efficient Cars
There are certain economy or diesel version of cars that make them exceptionally fuel efficient like the 6 cylinder **oldsmobile cutlass ciera (diesel)** or the 8 cylinder **oldsmobile cutlass ls**


To get a more complete picture, we need to perform further analysis. Let us hence try to gather more insights from our data regarding engine performance with respect to number of cylinders, displacement, weight and country of origin.
"""
)


px.histogram(data_frame=mpg_data, y="origin", color="origin")


# Seems like most cars in our dataset are **USA** based and there are only two other origins i.e. **Japan** and **Europe**.
# We can now analyze our cars categoirically based on the countries. Let us see what differences cars of each country possess.


px.histogram(data_frame=mpg_data, x="model_year", facet_col="origin")


px.box(data_frame=mpg_data, y=["mpg", "acceleration"], facet_col="origin")


px.box(data_frame=mpg_data, y="horsepower", facet_col="origin")


mpg_data.groupby("origin").agg(mean_horsepower=("horsepower", "mean")).reset_index()


# This shows us that Japanese cars are the most fuel efficient while USA has on average, more powerful cars. Also worth noting is that USA has a higher fence for hp meaning that there are car variants that are very powerful (muscle cars) which we see lacking in other countires.


# ## Bivariate analysis


px.scatter(data_frame=mpg_data, x="cylinders", y="origin", color="origin")


# In the dataset, US based cars have a higher count of cylinders, while Japanese and European cars have lower cylinders, but innovate in 3 cylinder or 5 cylinder engines.
# This might be due to racing being more poular and prevalant in the US or due to road networks being better in the US with consumer culture demanding more powerful cars.


# px.box(data_frame=mpg_data, x='mpg')
px.scatter(data_frame=mpg_data, x="model_year", y="mpg", facet_col="origin")


avg_group = pd.DataFrame()
avg_group = mpg_data.groupby(by="model_year").agg(average_mpg=("mpg", "mean"))
avg_group.reset_index()


# A trend of mpg getting better across the years can be seen in all the countries.


px.line(data_frame=avg_group, y="average_mpg")


# Getting the ***average mpg*** for models that came out each year across all countries shows that there is actually a steady **increase** in the fuel efficiency across the years.


# ### Getting names of company to see the Distribution of Car according to company


def get_first_name(x):
    full_name = x.split(" ")
    company = full_name[0]
    return company


mpg_data["company"] = mpg_data["name"].apply(lambda x: get_first_name(x))


company_hist = px.histogram(data_frame=mpg_data, x="company")
company_hist.show()


country_df = mpg_data.groupby("company").agg(mean_mpg=("mpg", "mean"))
country_df.reset_index().sort_values(by="mean_mpg", ascending=False).head()


country_df = mpg_data.groupby("company").agg(mean_horsepower=("horsepower", "mean"))
country_df.reset_index().sort_values(by="mean_horsepower", ascending=False).head()


# # Bivariate Analysis of Numerical Data


# To gain proper insigts and explore, I wrote code to plot all values vs all other values.


from plotly.subplots import make_subplots

col_names = [
    "mpg",
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "model_year",
]
graph_names = [f"{col_names[0].upper()} vs {x.upper()}" for x in col_names[1:]]
print(graph_names)
fig = make_subplots(rows=3, cols=2)
subplots = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]

for i in range(1, len(col_names)):
    row, col = subplots[i - 1]
    fig.add_trace(
        go.Scatter(
            x=mpg_data[col_names[0]],
            y=mpg_data[col_names[i]],
            mode="markers",
            name=graph_names[i - 1],
        ),
        row=row,
        col=col,
    )
    fig.update_xaxes(title_text=col_names[0], row=row, col=col)
    fig.update_yaxes(title_text=col_names[i], row=row, col=col)

fig.update_layout(height=720, width=1080, title_text=f"{col_names[0]} vs others")
fig.show()


# ### Observations: mpg vs others
#
# From these graphs, we can make a number of Observations.
# - A trend that shows more number of cylinders reduces fuel efficiency.
# - Higher horsepower,displacement and weight show lower fuel efficiency.
# - Acceleration and mpg do not have a obvious relationship due to a highly scattered plot. We do see a proportional trend, which is quite counter intuitive.
# - As the years progress, cars are getting more fuel efficient.


from plotly.subplots import make_subplots

col_names = [
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "model_year",
]
graph_names = [f"{col_names[0].upper()} vs {x.upper()}" for x in col_names[1:]]
print(graph_names)
fig = make_subplots(rows=3, cols=2)
subplots = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]

for i in range(1, len(col_names)):
    row, col = subplots[i - 1]
    fig.add_trace(
        go.Scatter(
            y=mpg_data[col_names[0]],
            x=mpg_data[col_names[i]],
            mode="markers",
            name=graph_names[i - 1],
        ),
        row=row,
        col=col,
    )
    fig.update_yaxes(title_text=col_names[0], row=row, col=col)
    fig.update_xaxes(title_text=col_names[i], row=row, col=col)

fig.update_layout(height=720, width=1080, title_text=f"{col_names[0]} vs others")
fig.show()


# ### Observations: Cylinders vs others
# We can see that more number of **cylinder** means higher **horse power**, more **displacement** and also a **heavier engine**.
#
# There is no clear relationship between the model year and the number of cylinders, indicating that cars with varying engine types were produced across all years.
#
# Checking out the **4 cylinder** engines, we observe that they give great fuel efficiency with light engines but with lower horse power. This could also mean they are both cheaper to manufacture and to use. This could explain why there are greater number of cars with 4 cylinder engines produced.
#
# We can not however, say for sure that these 4 cylinder cars are the most poular or most bought cars though. For that, we would need the sales data of these models to be certain.
#
# **6 cylinder engines** have a good balance of efficiency and horsepower. **8 cylinder engines** pack a punch with higher horsepower but guzzle a lot of fuel. The **8 cylinder** engines are some of the most powerful engines with very high horsepower. This makes sense as more cylinders will displace more fuel, producing more power but meaning lower fuel efficiency. At the same time bigger and heavier engines are needed to accomodate more number of cylinders.


from plotly.subplots import make_subplots

col_names = ["displacement", "horsepower", "weight", "acceleration", "model_year"]
graph_names = [f"{col_names[0].upper()} vs {x.upper()}" for x in col_names[1:]]
print(graph_names)
fig = make_subplots(rows=2, cols=2)
subplots = [(1, 1), (1, 2), (2, 1), (2, 2)]

for i in range(1, len(col_names)):
    row, col = subplots[i - 1]
    fig.add_trace(
        go.Scatter(
            x=mpg_data[col_names[0]],
            y=mpg_data[col_names[i]],
            mode="markers",
            name=graph_names[i - 1],
        ),
        row=row,
        col=col,
    )
    fig.update_xaxes(title_text=col_names[0], row=row, col=col)
    fig.update_yaxes(title_text=col_names[i], row=row, col=col)

fig.update_layout(height=720, width=1080, title_text=f"{col_names[0]} vs others")
fig.show()


from plotly.subplots import make_subplots

col_names = ["horsepower", "weight", "acceleration", "model_year"]
graph_names = [f"{col_names[0].upper()} vs {x.upper()}" for x in col_names[1:]]
print(graph_names)
fig = make_subplots(rows=2, cols=2)
subplots = [(1, 1), (1, 2), (2, 1), (2, 2)]

for i in range(1, len(col_names)):
    row, col = subplots[i - 1]
    fig.add_trace(
        go.Scatter(
            x=mpg_data[col_names[0]],
            y=mpg_data[col_names[i]],
            mode="markers",
            name=graph_names[i - 1],
        ),
        row=row,
        col=col,
    )
    fig.update_xaxes(title_text=col_names[0], row=row, col=col)
    fig.update_yaxes(title_text=col_names[i], row=row, col=col)

fig.update_layout(height=720, width=1080, title_text=f"{col_names[0]} vs others")
fig.show()


# ### Observation: horsepower vs others & displacement vs others
# We can see the relationships between weight, displacement and horsepower, i.e
#
# **more displacement &rarr; more horsepower**
#
# **more displacement &rarr; more weight**
#
# meaning **higher horsepower** engines are **heavier** like we observed before.
#
# The relationshoip between acceleration and displacement and acceleration and horsepower is negatively proportional though. This is rather counter intuitive as you might think cars having higher horsepower/displacement should provide higher acceleration as well. But that is not the case at all.
#
# What we can also see is that newer models have lower horsepower.
#
# To make more sense out of this we can create a correlation heatmap and perform further multivariate analysis.


# ## CORRELATION HEATMAP


correlation = mpg_data.select_dtypes("number").corr("pearson")
correlation


px.imshow(correlation, text_auto=True, color_continuous_scale="thermal", aspect="auto")


# The correlation heatmaps confirms the relation between **cylinder, displacement, horsepower and weight.**
# We also see that these affect mpg negatively as expected.
#
# We can also see that there is a fair relationship between mpg and model years, meaning newer models tend to be fuel efficient.
#
# But then acceleration is negatively proportional to cylinder, displacement, horsepower and weight, which is still unexplained.
# Whats more, there is a weakly positive relation between acceleration and mpg meaning higher acceleration gives better mileage, which is not logical.


px.scatter(data_frame=mpg_data, x="horsepower", y="mpg", color="model_year")


# From this plot we can confirm that newer models are more efficient than the older ones. However, we can see that the newer models also have lower horsepower.


px.scatter(data_frame=mpg_data, x="weight", y="horsepower", color="model_year")


# With this graph we find that heavier models are all older models, which also have a lot of horse power. The newer models are not only fuel efficient but are lighter and provide lower power output.
#
# This raises a questions as why the companies would build such cars with low power and weight but better fuel efficiency?


px.scatter(data_frame=mpg_data, x="horsepower", y="acceleration", color="model_year")


# This tells us almost all new models have low horse power but high acceleration. Even though there were some older models that had low horsepower/high acceleration.


px.scatter(
    data_frame=mpg_data,
    x="weight",
    y="acceleration",
    color="horsepower",
    color_continuous_scale="temps",
)


# Higher horsepower cars are almost always rather heavy with lower acceleration.


cyl = (
    mpg_data.groupby("model_year")
    .aggregate(avg_no_of_cylinders=("cylinders", "mean"), avg_mpg=("mpg", "mean"))
    .reset_index()
)
px.scatter(data_frame=cyl, x="model_year", y="avg_no_of_cylinders", color="avg_mpg")


# Newer cars have fewer no of cylinders on average.


# These final graphs give us answers to a few questions we were asking.
#
# # Conclusions
#
# ## Why would acceleration increase when horsepower is decreasing?
#
# Newer cars have higher acceleration despite lower horsepower. And along with good acceleration, these cars are also fuel efficient.
#
# Turns out the acceleration in cars are increasing beacuse cars are getting lighter, requiring less power to accelerate.
#
#
# ## Why did the companies start making lower power, fuel efficient cars?
#
#  This data does make it clear that cars do not only need raw horsepower. They can be fast and fuel efficient even with lower horsepower. With fuel emmisions being a major concern and major technological breakthroughs, it is compeletely sensible now that the companies chose to make their cars this way. What is more that the cars could be cheaper with less materials being used and the car would be less expensive to operate for the customers as well all while being better for the environment.
#
# There might be several factors that the data does not capture. The newer cars would have better technology like lighter materials, aerodynamics, better fuel composition and better engineering as well. But the fact is that car companies did make lighter, fuel efficient cars earlier too; only that they chose to keep making newer cars that were lower power and less fuel hungry.
#
# ## Why are there so many 4 cylinder cars?
#
# This falls in line with the fact that the newer models have on average lower number of cylinders. This also makes us understand as why there are more number of 4 cylinder cars which are the lightest and most fuel efficient, with better stability, lower vibration and possibly the cost.
#
