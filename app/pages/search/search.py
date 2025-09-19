import streamlit as st

from pages.search.cars import *


def search_car():
    data_filter = CarFilter()
    data = load_database()
    get_filter(data, data_filter)
    filtered_data = apply_filter(data, data_filter)
    st.dataframe(filtered_data)


def main():
    st.markdown("# Buscar 🔍")
    st.sidebar.markdown("# Buscar 🔍")

    st.markdown('## Vehículos 🚗')
    search_car()


main()
