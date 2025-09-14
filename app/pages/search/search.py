import streamlit as st

from pages.search.cars import *

# Main page content
st.markdown("# Buscando 🔍")
st.sidebar.markdown("# Buscar 🔍")

load_cars()
