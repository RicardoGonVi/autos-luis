import streamlit as st

from constants.constants import CAR_TYPES_DATABASE
from database.database import load_database
from pages.add.cars import *
from utils.utils import make_tabs

# Main page content


def add_car():
    data_adder = CarAdder("CarAdder_")
    car_data = load_database(CAR_TYPES_DATABASE)

    data_adder.get_adder(car_data)


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
