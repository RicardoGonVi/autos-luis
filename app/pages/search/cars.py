import streamlit as st
import pandas as pd

from constants.constants import *


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
        min_year = data[YEAR_FILTER].min()
        max_year = data[YEAR_FILTER].max()
        min_price = data[PRICE_FILTER].min() / MILLION
        max_price = data[PRICE_FILTER].max() / MILLION

        st.markdown('#### Filtros rápidos')

        row1 = st.columns([4, 1, 4])
        filter.price_range_ = row1[0].slider(
            "💵 Rango de precio ( ₡1.000.000 )",
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
        filter.car_id_ = row2[0].text_input("🚗 " + CAR_ID_FILTER)
        filter.id_ = row2[2].text_input("#️⃣" + ID_FILTER + "Autos Luis")

        st.form_submit_button('Buscar')


def specific_filter(data, filter: "CarFilter"):
    with st.form("SpecificFilters"):
        st.markdown('#### Filtros específicos')
        row3 = st.columns([4, 1, 4, 1, 4])
        filter.car_brand_ = row3[0].selectbox(
            '🚓 ' + BRAND_FILTER,
            [SELECT_FILTER] + sorted(data[BRAND_FILTER].unique())
        )
        filter.car_model_ = row3[2].selectbox(
            '🛻 ' + MODEL_FILTER,
            [SELECT_FILTER] + sorted(
                data[MODEL_FILTER].unique())
        )
        filter.car_color_ = row3[4].selectbox(
            '🌈 ' + COLOR_FILTER,
            [SELECT_FILTER] + sorted(
                data[COLOR_FILTER].unique())
        )

        row4 = st.columns([4, 1, 4, 1, 4])
        filter.car_status_ = row4[0].selectbox(
            '⁉️ ' + STATUS_FILTER,
            [SELECT_FILTER] + sorted(data[STATUS_FILTER].unique())
        )
        filter.car_facturation_ = row4[2].selectbox(
            '🔜 ' + FACTURATION_STATUS_FILTER,
            [SELECT_FILTER] + sorted(data[FACTURATION_STATUS_FILTER].unique())
        )
        filter.car_owner_ = row4[4].selectbox(
            '🙎🏻 ' + OWNER_FILTER,
            [SELECT_FILTER] + sorted(
                data[OWNER_FILTER].unique())
        )

        row5 = st.columns([4, 1, 4, 1, 4])
        filter.car_year_ = row5[2].selectbox(
            '📅 ' + YEAR_FILTER,
            [SELECT_FILTER] + sorted(data[YEAR_FILTER].unique())
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
        (filtered_data[PRICE_FILTER] >= filter.price_range_[0] * MILLION) &
        (filtered_data[PRICE_FILTER] <= filter.price_range_[1] * MILLION)
    ]

    filtered_data = filtered_data[
        (filtered_data[YEAR_FILTER] >= filter.year_range_[0]) &
        (filtered_data[YEAR_FILTER] <= filter.year_range_[1])
    ]

    if filter.car_id_:
        filtered_data = filtered_data[filtered_data[CAR_ID_FILTER].str.contains(
            filter.car_id_, case=False, na=False)]

    if filter.id_:
        filtered_data = filtered_data[filtered_data[ID_FILTER].str.contains(
            filter.id_, case=False, na=False)]

    # Specific filters
    if filter.car_brand_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data[BRAND_FILTER]
                                      == filter.car_brand_]

    if filter.car_model_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data[MODEL_FILTER]
                                      == filter.car_model_]

    if filter.car_color_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data[COLOR_FILTER]
                                      == filter.car_color_]

    if filter.car_status_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data[STATUS_FILTER]
                                      == filter.car_status_]

    if filter.car_facturation_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data[FACTURATION_STATUS_FILTER]
                                      == filter.car_facturation_]

    if filter.car_owner_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data[OWNER_FILTER]
                                      == filter.car_owner_]

    if filter.car_year_ != SELECT_FILTER:
        filtered_data = filtered_data[filtered_data[YEAR_FILTER]
                                      == filter.car_year_]

    return filtered_data
