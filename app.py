# importing necessary packages
import streamlit as st
import pandas as pd
from utils import api_extracter

# create an instance of a class
client = api_extracter()

st.set_page_config(page_title="IMDB Top Movies Project",layout="wide")
# create website title
st.title("IMDB movies app")

st.subheader("By Prathamesh Lembhe")

button = st.button("Click here to view most popular movie titles")
if button:
    data = client.get_data()
    df = pd.DataFrame(data,columns=["Movie Names","Release Year","Rank"])
    st.dataframe(df)
    csv_data = df.to_csv(index=False).encode("utf-8")

    # TO include a download button
    st.download_button(
        label = "Download above content as csv file",
        data = csv_data,
        file_name = "IMDB Popular Movie data.csv",
        mime = "text/csv"
    )

