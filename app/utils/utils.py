import streamlit as st
from datetime import date as d
from dataclasses import dataclass, field

from constants.constants import INCLUDE_LAST


@st.cache_data(ttl=600)
def get_years_range(init, end):
    years = list(range(init, end + INCLUDE_LAST))

    return years


@st.cache_data(ttl=600)
def get_current_year():
    today = d.today()
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
class PurchaseInfo:
    # TODO: add documentation
    date: d = None
    price: int = 0


@dataclass
class LegalInfo:
    # TODO: add documentation
    public_deed_type: str = ""
    public_deed_date: d = None
    public_deed_number: str = ""
    transfer_fee: float = 0
    tax_value: float = 0
    lawyer: Person = field(default_factory=Person)


@dataclass
class CarRegistration:
    # TODO: add documentation
    owner: Person = field(default_factory=Person)
    date: d = None
    origin: str = ""
    rent_unit: str = ""
    status: str = ""

    # Legal info
    legal: LegalInfo = field(default_factory=LegalInfo)


@dataclass
class Car:
    # TODO: add documentation
    # Codes
    unique_code: str = ""
    id: int = 0
    vin_id: int = 0
    dua_id: int = 0

    # Characteristics
    brand: str = ""
    model: str = ""
    year: int = 0
    color: str = ""
    comment: str = ""

    # Entry data
    registration: CarRegistration = field(default_factory=CarRegistration)

    # Purchase info
    purchase: PurchaseInfo = field(default_factory=PurchaseInfo)
