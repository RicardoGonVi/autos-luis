import streamlit as st

from constants.constants import CAR_TYPES_DATABASE, COLOR_DATABASE, CAR_TRANSMISSIONS_DATABASE, PERSONS_DATABASE
from database.database import load_database
from pages.add.cars import *
from utils.utils import make_tabs

# Main page content


def add_car():
    data_adder = CarAdder("CarAdder_")
    car_data = load_database(CAR_TYPES_DATABASE)
    color_data = load_database(COLOR_DATABASE)
    car_transmission = load_database(CAR_TRANSMISSIONS_DATABASE)
    person_data = load_database(PERSONS_DATABASE)

    data_adder.get_data(car_data, color_data, car_transmission, person_data)


def main():
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
