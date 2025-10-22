import streamlit as st
import pandas as pd


@st.cache_data(ttl=600)
def load_database(database):
    data = pd.read_csv(database, sep=";", encoding="utf-8")
    return data


def save_dataset(data, database):
    data.to_csv(database, sep=";", index=False, encoding="utf-8")


def append_data(data, database, new_row):
    data.loc[len(data)] = new_row
    save_dataset(data, database)
