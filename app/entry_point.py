import streamlit as st

st.set_page_config(
    layout="wide"
)

# Define the ui
main_page = st.Page(
    "ui/main_page.py",
    title="Control de Inventario",
    icon="🚗")
search_page = st.Page("ui/search.py", title="Buscar", icon="🔍")
add_page = st.Page("ui/add.py", title="Agregar", icon="➕")
sell_page = st.Page("ui/sell.py", title="Vender", icon="💰")


# Set up navigation
pg = st.navigation([main_page, search_page, add_page, sell_page])

# Run the selected page
pg.run()
