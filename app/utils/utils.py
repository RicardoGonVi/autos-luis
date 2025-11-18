import streamlit as st
from datetime import date as d

from app.constants.constants import INCLUDE_LAST


@st.cache_data(ttl=600)
def get_years_range(init: int, end: int) -> list:
    """
    Gets a list containing all the years between the initial and final year
    of a given range, inclusive.

    This function is cached for 10 minutes (600 seconds) to improve performance
    when repeatedly accessed.

    Args:
        init (int):     The initial year of the range.
        end (int):      The final year of the range.

    Returns:
        years (list):   A list of years from the initial year to the final year.
    """
    years: list = list(range(init, end + INCLUDE_LAST))

    return years


@st.cache_data(ttl=600)
def get_current_year() -> int:
    """
    Gets the current year based on the system date.

    This function is cached for 10 minutes (600 seconds) to improve performance
    when repeatedly accessed.

    Returns:
        current_year (int):  The current year.
    """
    today = d.today()
    current_year: int = today.year

    return current_year


def make_tabs(*names):
    """Wrapper around st.tabs returning the created tab objects."""
    if len(names) == 1 and isinstance(names[0], (list, tuple)):
        names = names[0]
    return st.tabs(list(names))
