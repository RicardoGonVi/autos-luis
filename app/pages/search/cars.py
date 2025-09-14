import streamlit as st
import pandas as pd

from constants.constants import CAR_DATABASE


@st.cache_data(ttl=600)
def load_database():
    data = pd.read_csv(CAR_DATABASE, sep=";", encoding="utf-8")
    return data


def filter_search(data):
    filtered_data = data.copy()

    with st.form("my_form"):
        min_year = data['Año'].min()
        max_year = data['Año'].max()
        min_price = data['Precio base'].min()
        max_price = data['Precio base'].max()

        st.markdown('#### Filtros rápidos')

        row1 = st.columns([4, 1, 4])
        value_range = row1[0].slider(
            "💵 Rango de precio ( ₡ )",
            min_value=min_price,
            max_value=max_price,
            value=[
                min_price,
                max_price])
        year_range = row1[2].slider(
            "📅 Rango de años",
            min_value=min_year,
            max_value=max_year,
            value=[
                min_year,
                max_year])

        row2 = st.columns([4, 1, 4])
        car_id = row2[0].text_input("🚗 Placa")
        id = row2[2].text_input("#️⃣ ID")

        st.markdown('#### Filtros específicos')
        row3 = st.columns([4, 1, 4, 1, 4])
        car_brand = row3[0].selectbox(
            '🚓 Marca', sorted(
                data['Marca'].unique()))
        car_model = row3[2].selectbox(
            '🛻 Modelo', sorted(
                data['Modelo'].unique()))
        car_color = row3[4].selectbox(
            '🌈 Color', sorted(
                data['Color'].unique()))

        row4 = st.columns([4, 1, 4, 1, 4])
        car_status = row4[0].selectbox('⁉️ Estado', data['Estado'].unique())
        car_facturation = row4[2].selectbox(
            '🔜 Estado de facturación', data['Estado de facturacion'].unique())
        car_owner = row4[4].selectbox(
            '🙎🏻 Dueño', sorted(
                data['Dueño'].unique()))

        row5 = st.columns([4, 1, 4, 1, 4])
        car_year = row5[2].selectbox('📅 Año', sorted(data['Año'].unique()))

        st.form_submit_button('Buscar')
