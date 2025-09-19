import streamlit as st

from pages.search.cars import *

# Search page main content
st.markdown("# Buscar 🔍")
st.sidebar.markdown("# Buscar 🔍")

st.markdown('## Vehículos 🚗')

data_filter = CarFilter()
data = load_database()
get_filter(data, data_filter)
filtered_data = apply_filter(data, data_filter)
st.dataframe(filtered_data)
