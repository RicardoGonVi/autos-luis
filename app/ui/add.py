import streamlit as st

from app.constants.database import *
from app.core.add.cars import CarAdder
from app.core.add.persons import PersonAdder
from app.database.database import load_database
from app.utils.utils import make_tabs


def add_person(shared_data: dict) -> None:
    """
    Displays a tab in Streamlit that allows the user to add a person to the main
    persons database.

    This function initializes a `PersonAdder` instance, retrieves user input
    through Streamlit widgets, and then saves the collected data into the
    corresponding dataset.

    Args:
        shared_data (dict): A dictionary containing the preloaded datasets used
            by the `PersonAdder` instance.
    """
    data_adder = PersonAdder("PersonAdder_", PERSONS_DATABASE, shared_data)

    data_adder.get_data()
    data_adder.add_data()


def add_car(shared_data: dict) -> None:
    """
    Displays a tab in Streamlit that allows the user to add a car to the main
    persons database.

    This function initializes a `CarAdder` instance, retrieves user input
    through Streamlit widgets, and then saves the collected data into the
    corresponding dataset.

    Args:
        shared_data (dict): A dictionary containing the preloaded datasets used
            by the `CarAdder` instance.
    """
    data_adder = CarAdder("CarAdder_", CAR_DATABASE, shared_data)

    data_adder.get_data()
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
    shared_data = {
        "car_types": load_database(CAR_TYPES_DATABASE),
        "options": load_database(GENERAL_OPTIONS_DATABASE),
        "car_transmissions": load_database(CAR_TRANSMISSIONS_DATABASE),
        "persons": load_database(PERSONS_DATABASE),
        "locations": load_database(LOCATIONS_DATABASE)
    }

    with cars_tab:
        add_car(shared_data)

    with persons_tab:
        add_person(shared_data)

    with garages_tab:
        None
