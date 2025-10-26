import streamlit as st

from constants.constants import (
    CAR_TYPES_DATABASE,
    AUTOS_LUIS_DATABASE,
    CAR_TRANSMISSIONS_DATABASE,
    PERSONS_DATABASE,
    CAR_DATABASE
)
from database.database import load_database
from pages.add.cars import *
from utils.utils import make_tabs


def add_car():
    """
    Tabs that adds a car into the main car-database by using streamlit widgets.
    """
    data_adder = CarAdder("CarAdder_")
    car_type_data = load_database(CAR_TYPES_DATABASE)
    autos_luis_data = load_database(AUTOS_LUIS_DATABASE)
    car_transmission_data = load_database(CAR_TRANSMISSIONS_DATABASE)
    person_data = load_database(PERSONS_DATABASE)
    car_data = load_database(CAR_DATABASE)

    data_adder.get_data(car_type_data, autos_luis_data,
                        car_transmission_data, person_data, car_data)


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
        None

    with garages_tab:
        None


main()
