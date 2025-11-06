import streamlit as st
from datetime import date
from dataclasses import dataclass, field

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


@dataclass
class Location:
    # TODO: add documentation
    province: str = ""
    canton: str = ""
    district: str = ""
    exact_location: str = ""


@dataclass
class Person:
    # TODO: add documentation
    contact_media: str = ""
    id: str = ""
    id_type: str = ""
    name: str = ""
    mail: str = ""
    type: str = ""
    phone: int = 0
    location: Location = field(default_factory=Location)


@dataclass
class Car:
    # TODO: add documentation
    unique_code: str = ""
    id: int = 0
    vin_id: int = 0
    dua_id: int = 0
    brand: str = ""
    model: str = ""
    year: int = 0
    color: str = ""
    status: str = ""
    owner: Person = field(default_factory=Person)
    comment: str = ""
