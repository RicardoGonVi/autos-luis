import streamlit as st

from core.search.cars import *
from core.search.persons import *
from core.search.garage import *
from utils.utils import make_tabs
from database.database import load_database
from constants.database import *


def search_car():
    data_filter = CarFilter()
    data = load_database(CAR_DATABASE)

    data_filter.get_filter(data)
    filtered_data = data_filter.apply_filter(data)

    data_filter.show_filter(filtered_data)


def search_person():
    data_filter = PersonFilter()
    data = load_database(PERSONS_DATABASE)

    data_filter.get_filter(data)
    filtered_data = data_filter.apply_filter(data)

    data_filter.show_filter(filtered_data)


def search_garage():
    data_filter = GarageFilter()
    data = load_database(GARAGE_DATABASE)

    data_filter.get_filter(data)
    filtered_data = data_filter.apply_filter(data)

    data_filter.show_filter(filtered_data)


def main():
    st.sidebar.markdown("# Buscar 🔍")

    st.header(
        "Buscar 🔍", help="Pestaña de búsqueda.")
    cars_tab, persons_tab, garages_tab = \
        make_tabs(["VEHÍCULOS 🚗", "PERSONAS 🙋", "TALLERES MECÁNICOS 🛠️"])

    with cars_tab:
        search_car()

    with persons_tab:
        search_person()

    with garages_tab:
        search_garage()


main()
