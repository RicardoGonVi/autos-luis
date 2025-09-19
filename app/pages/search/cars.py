import streamlit as st
import pandas as pd

from constants.constants import CAR_DATABASE, SELECT_FILTER


class CarFilter:
    def __init__(self):
        self.year_range_ = []
        self.price_range_ = []
        self.car_id_ = -1
        self.id_ = -1
        self.car_brand_ = SELECT_FILTER
        self.car_model_ = SELECT_FILTER
        self.car_color_ = SELECT_FILTER
        self.car_status_ = SELECT_FILTER
        self.car_facturation_ = SELECT_FILTER
        self.car_owner_ = SELECT_FILTER
        self.car_year_ = SELECT_FILTER


@st.cache_data(ttl=600)
def load_database():
    data = pd.read_csv(CAR_DATABASE, sep=";", encoding="utf-8")
    return data


def quick_filter(data, filter: "CarFilter"):
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

        st.form_submit_button('Buscar')


def specific_filter(data, filter: "CarFilter"):
    with st.form("SpecificFilters"):
        st.markdown('#### Filtros específicos')
        row3 = st.columns([4, 1, 4, 1, 4])
        filter.car_brand_ = row3[0].selectbox(
            '🚓 Marca',
            [SELECT_FILTER] + sorted(data['Marca'].unique())
        )
        filter.car_model_ = row3[2].selectbox(
            '🛻 Modelo',
            [SELECT_FILTER] + sorted(
                data['Modelo'].unique())
        )
        filter.car_color_ = row3[4].selectbox(
            '🌈 Color',
            [SELECT_FILTER] + sorted(
                data['Color'].unique())
        )

        row4 = st.columns([4, 1, 4, 1, 4])
        filter.car_status_ = row4[0].selectbox(
            '⁉️ Estado',
            [SELECT_FILTER] + sorted(data['Estado'].unique())
        )
        filter.car_facturation_ = row4[2].selectbox(
            '🔜 Estado de facturación',
            [SELECT_FILTER] + sorted(data['Estado de facturacion'].unique())
        )
        filter.car_owner_ = row4[4].selectbox(
            '🙎🏻 Dueño',
            [SELECT_FILTER] + sorted(
                data['Dueño'].unique())
        )

        row5 = st.columns([4, 1, 4, 1, 4])
        filter.car_year_ = row5[2].selectbox(
            '📅 Año',
            [SELECT_FILTER] + sorted(data['Año'].unique())
        )

        st.form_submit_button('Buscar')


def get_filter(data, filter: "CarFilter"):
    quick_filter(data, filter)

    show_sf = st.checkbox("Filtros específicos")
    if show_sf:
        specific_filter(data, filter)


def apply_filter(data, filter: "CarFilter"):
    filtered_data = data.copy()

    # Quick filters
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

    # Specific filters
    if filter.car_brand_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data['Marca']
                                      == filter.car_brand_]

    if filter.car_model_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data['Modelo']
                                      == filter.car_model_]

    if filter.car_color_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data['Color']
                                      == filter.car_color_]

    if filter.car_status_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data['Estado']
                                      == filter.car_status_]

    if filter.car_facturation_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data['Estado de facturacion']
                                      == filter.car_facturation_]

    if filter.car_owner_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data['Dueño']
                                      == filter.car_owner_]

    if filter.car_year_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data['Año'] == filter.car_year_]

    return filtered_data
