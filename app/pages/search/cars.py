import streamlit as st
import pandas as pd

from constants.constants import CAR_DATABASE


@st.cache_data(ttl=600)
def load_database():
    data = pd.read_csv(CAR_DATABASE, sep=";", encoding="utf-8")
    return data
