import streamlit as st
from datetime import date

from constants.constants import INCLUDE_LAST


@st.cache_data(ttl=600)
def get_years_range(init, end):
    years = list(range(init, end + INCLUDE_LAST))

    return years


@st.cache_data(ttl=600)
def get_current_year():
    today = date.today()
    current_year = today.year

    return current_year


def make_tabs(*names):
    """Wrapper around st.tabs returning the created tab objects."""
    if len(names) == 1 and isinstance(names[0], (list, tuple)):
        names = names[0]
    return st.tabs(list(names))
