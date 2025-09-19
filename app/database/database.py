import streamlit as st
import pandas as pd


@st.cache_data(ttl=600)
def load_database(database):
    data = pd.read_csv(database, sep=";", encoding="utf-8")
    return data
