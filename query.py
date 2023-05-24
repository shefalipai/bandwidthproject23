import streamlit as st
import pandas as pd
import altair as alt

#just need to get a dataset for bandwidth. 
@st.cache_data
def get_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


