import streamlit as st
from PIL import Image

st.title("SQL Example")

'''
In this section, we will make an app that connect with MySQL and visualize it. 
The data used is `Basketball_men` database from [RELATIONAL DATASET REPOSITORY](https://relational.fit.cvut.cz/dataset/BasketballMen), 
'''

image = Image.open("assets/public-database.png")
st.image(image)

'''
First, remember to add the database credentials to the `.streamlit/secrets.toml` file.
After that, we can start to connect to the database like example below:
'''

with st.echo():
    import streamlit as st
    conn = st.experimental_connection("sql")

'''
Next, we will try to view the data from `players` table.
'''

with st.echo():
    sql = "SELECT * FROM players"
    data = conn.query(sql)
    st.dataframe(data, hide_index=True)

'''
We can see the data is quite large, so we will try to filter the data by country and visualize it.
'''

with st.echo():
    sql = '''
        SELECT birthCountry, COUNT(*) AS total
        FROM players
        GROUP BY birthCountry
        ORDER BY total DESC
        LIMIT 5
    '''
    countries = conn.query(sql)
    st.dataframe(countries, hide_index=True)

'''
From the chart above, we can see that most of the players are from USA but the missing values are quite large.
Next, let's try with another table.
We will try to get the information from `coaches` table.
'''

with st.echo():
    sql = '''
        SELECT year, won, lost
        FROM coaches
        WHERE coachID = "adelmri01"
    '''
    coaches = conn.query(sql)
    st.line_chart(coaches, x='year', y=['won', 'lost'])

'''
The chart above shows the statistics of the coach with coachID `adelmri01` with the number of wins and losses. 
'''

'''
his is just a simple example of how to connect to database and visualize the data. You can try to connect to your own database and make your own visualization.
'''
