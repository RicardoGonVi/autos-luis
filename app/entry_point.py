import streamlit as st

# Define the pages
main_page = st.Page(
    "pages/main_page.py",
    title="Control de Inventario",
    icon="🚗")
search_page = st.Page("pages/search/search.py", title="Buscar", icon="🔍")
add_page = st.Page("pages/add/add.py", title="Agregar", icon="➕")
sell_page = st.Page("pages/sell.py", title="Vender", icon="💰")


# Set up navigation
pg = st.navigation([main_page, search_page, add_page, sell_page])

# Run the selected page
pg.run()
