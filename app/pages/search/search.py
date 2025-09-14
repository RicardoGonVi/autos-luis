import streamlit as st

from pages.search.cars import *

# Search page main content
st.markdown("# Buscar 🔍")
st.sidebar.markdown("# Buscar 🔍")

st.subheader('Vehículos 🚗')
data = load_database()
st.dataframe(data)
