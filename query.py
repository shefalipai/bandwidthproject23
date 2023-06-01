import streamlit as st
import pandas as pd
import altair as alt

#just need to get a dataset for bandwidth. 
#you can make sql queries to load data when working with databases. 

# connection = database.connect()

# @st.cache_data
# def query():
#     return pd.read_sql_query("SELECT * from table", connection)



@st.cache_data
def get_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

#create a dashboard that allows other teams to query data with out having to run a sql command. 
#do it for multiple data sets or make one template where multiple data sets can be replaced and query data from multiple data sets. 
# make it ui friendly, as people who don't know much about data and queries will be using it. 

try: 
    df = get_data()
    countries = st.multiselect(
        "Choose countries", list(df.index), ["China", "United States of America"]
    )
    st.write(df.index)
except: 
     st.error("""
#         **This demo requires internet access.**
#         Connection error: %s
#     """)