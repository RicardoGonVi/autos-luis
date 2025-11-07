import streamlit as st

from constants.database import *
from core.add.cars import CarAdder
from core.add.persons import PersonAdder
from database.database import load_database
from utils.utils import make_tabs


def add_person():
    """
    Tabs that adds a car into the main car-database by using streamlit widgets.
    """
    data_adder = PersonAdder("PersonAdder_", PERSONS_DATABASE)
    general_options_data = load_database(GENERAL_OPTIONS_DATABASE)
    locations_data = load_database(LOCATIONS_DATABASE)

    data_adder.get_data(general_options_data, locations_data)
    data_adder.add_data()


def add_car():
    """
    Tabs that adds a car into the main car-database by using streamlit widgets.
    """
    data_adder = CarAdder("CarAdder_", CAR_DATABASE)
    car_type_data = load_database(CAR_TYPES_DATABASE)
    general_options_data = load_database(GENERAL_OPTIONS_DATABASE)
    car_transmission_data = load_database(CAR_TRANSMISSIONS_DATABASE)
    person_data = load_database(PERSONS_DATABASE)
    car_data = load_database(CAR_DATABASE)

    data_adder.get_data(car_type_data, general_options_data,
                        car_transmission_data, person_data, car_data)
    data_adder.add_data()


# Main page content
def main():
    """
    Add main window. Contains three tabs that the user can navigate through:

    -cars:      tab used to add cars into a database.
    -persons:   tab used to add persons into a database.
    -garages:   tab used to add garages into a database.
    """
    st.sidebar.markdown("# Agregar ➕")

    st.header("Agregar ➕", help="Pestaña de agregado.")
    cars_tab, persons_tab, garages_tab = \
        make_tabs(["VEHÍCULOS 🚗", "PERSONAS 🙋", "TALLERES MECÁNICOS 🛠️"])

    with cars_tab:
        add_car()

    with persons_tab:
        add_person()

    with garages_tab:
        None


main()
