import streamlit as st
from PIL import Image

st.title("Google Sheets Example")

'''
In this section, we will make an app that connect with Google Sheets and visualize it.
The data used is Iris dataset, available at Kaggle can be downloaded [here](https://www.kaggle.com/datasets/uciml/iris).
First, you need to import the dataset to your Google Sheets and make it public.
'''

image = Image.open("assets/public-gsheets.png")
st.image(image)

'''
After that, you can click `Salin link` to copy the link.
You can use the link to connect to Google Sheets like the example below:
'''

with st.echo():
    import streamlit as st
    import pandas as pd
    from streamlit_gsheets import GSheetsConnection
    import altair as alt

    url = "https://docs.google.com/spreadsheets/d/1YJgBYp285fXHBvATelWXpu2BxxWqjsbnNjDcsfbbQYU/edit?usp=sharing"
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)

'''
To read the data, you can use `read` method from the connection object and display it using `st.dataframe`:
'''

with st.echo():
    data = conn.read(spreadsheet=url)
    st.dataframe(data, hide_index=True)

'''
We will use the data to make a simple visualization to see the distribution of the species.
'''

with st.echo():
    st.bar_chart(data['Species'].value_counts())

'''
From the chart, we can see that the data is balanced, where each species has the same number of data.
Next, we will try to use the petal length and width to get insight about the species.
'''
with st.echo():
    chart = alt.Chart(data).mark_circle().encode(
        x='PetalLengthCm',
        y='PetalWidthCm',
        color='Species',
    )
    st.altair_chart(chart, use_container_width=True)

'''
From the chart above, we can see that the species can be separated by the petal length and width.
Iris-setosa has the smallest petal length and width, while Iris-virginica has the largest petal length and width.
'''

'''
This is just a simple example of how to connect to Google Sheets and visualize the data.
You can try to connect to your own Google Sheets and make your own visualization.
'''
