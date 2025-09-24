import streamlit as st

from utils.utils import make_tabs
from pages.add.cars import *

# Main page content


def add_car():
    data_adder = CarAdder()
    data_adder.get_adder()


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
