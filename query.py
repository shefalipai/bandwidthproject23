import streamlit as st
import pandas as pd
import altair as alt

#just need to get a dataset for bandwidth. 
@st.cache_data
def get_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

#create a dashboard that allows other teams to query data with out having to run a sql command. 
#do it for multiple data sets or make one template where multiple data sets can be replaced and query data from multiple data sets. 
# make it ui friendly, as people who don't know much about data and queries will be using it. 
