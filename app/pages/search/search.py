import streamlit as st

from pages.search.cars import *
from pages.search.persons import *
from pages.search.garage import *
from database.database import load_database
from constants.constants import CAR_DATABASE, LAWYER_DATABASE, GARAGE_DATABASE


def search_car():
    data_filter = CarFilter()
    data = load_database(CAR_DATABASE)

    data_filter.get_filter(data)
    filtered_data = data_filter.apply_filter(data)
    st.dataframe(filtered_data)


def search_person():
    data_filter = PersonFilter()
    data = load_database(LAWYER_DATABASE)

    data_filter.get_filter(data)
    filtered_data = data_filter.apply_filter(data)

    st.dataframe(filtered_data, on_select="rerun")


def search_garage():
    data_filter = GarageFilter()
    data = load_database(GARAGE_DATABASE)

    data_filter.get_filter(data)


def main():
    st.markdown("# Buscar 🔍")
    st.sidebar.markdown("# Buscar 🔍")

    st.markdown('## Vehículos 🚗')
    search_car()

    st.markdown('## Personas 🙋🏼')
    search_person()


main()
