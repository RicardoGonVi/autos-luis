import streamlit as st
import pandas as pd


@st.cache_data(ttl=600)
def load_database(database):
    """
    Loads a datatabase csv file and saves it into a pandas variable.
    The csv file is in utf-8 format and has its content separated by ";"

    Args:
        database(str):  Path of the csv database file to be read.

    Returns:
        data(pd):       Contains the csv dataset in pandas type.
    """
    data = pd.read_csv(database, sep=";", encoding="utf-8")
    return data


def save_database(data, database):
    """
    Saves a database pandas variable into a csv file.
    The csv file is in utf-8 format and has its content separated by ";"

    Args:
        data(pd):       Contains the csv database in pandas type.
        database(str):  Path of the csv database file to be saved.
    """
    data.to_csv(database, sep=";", index=False, encoding="utf-8")


def append_data(data, database, new_row):
    """
    Appends a row of data into a pandas data variable.
    Then calls save_database() to save updated variable into a csv file.

    Args:
        data(pd):       Contains the csv database in pandas type.
        database(str):  Path of the csv database file to be saved.
        new_row(dict):  New row to be added to the database. User
                        must make sure that the data matches the
                        database content order.
    """
    data.loc[len(data)] = new_row
    save_database(data, database)
