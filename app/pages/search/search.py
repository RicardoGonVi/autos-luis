import streamlit as st

from pages.search.cars import *

# Search page main content
st.markdown("# Buscar 🔍")
st.sidebar.markdown("# Buscar 🔍")

st.markdown('## Vehículos 🚗')
data = load_database()
filter_search(data)
st.dataframe(data)
