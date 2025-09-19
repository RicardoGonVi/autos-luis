import streamlit as st
import pandas as pd

from constants.constants import CAR_DATABASE


class CarFilter:
    def __init__(self):
        self.year_range_ = []
        self.price_range_ = []
        self.car_id_ = -1
        self.id_ = -1


@st.cache_data(ttl=600)
def load_database():
    data = pd.read_csv(CAR_DATABASE, sep=";", encoding="utf-8")
    return data


def get_filter(data, filter: "CarFilter"):
    with st.form("QuickFilters"):
        min_year = data['Año'].min()
        max_year = data['Año'].max()
        min_price = data['Precio base'].min()
        max_price = data['Precio base'].max()

        st.markdown('#### Filtros rápidos')

        row1 = st.columns([4, 1, 4])
        filter.price_range_ = row1[0].slider(
            "💵 Rango de precio ( ₡ )",
            min_value=min_price,
            max_value=max_price,
            value=[
                min_price,
                max_price])
        filter.year_range_ = row1[2].slider(
            "📅 Rango de años",
            min_value=min_year,
            max_value=max_year,
            value=[
                min_year,
                max_year])

        row2 = st.columns([4, 1, 4])
        filter.car_id_ = row2[0].text_input("🚗 Placa")
        filter.id_ = row2[2].text_input("#️⃣ Código Autos Luis")

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


def apply_filter(data, filter: "CarFilter"):
    filtered_data = data.copy()

    filtered_data = filtered_data[
        (filtered_data['Precio base'] >= filter.price_range_[0]) &
        (filtered_data['Precio base'] <= filter.price_range_[1])
    ]

    filtered_data = filtered_data[
        (filtered_data['Año'] >= filter.year_range_[0]) &
        (filtered_data['Año'] <= filter.year_range_[1])
    ]

    if filter.car_id_:
        filtered_data = filtered_data[filtered_data['Placa'].str.contains(
            filter.car_id_, case=False, na=False)]

    if filter.id_:
        filtered_data = filtered_data[filtered_data['Código'].str.contains(
            filter.id_, case=False, na=False)]

    return filtered_data
