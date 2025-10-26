import streamlit as st
import pandas as pd

from constants.constants import (
    SELECT_FILTER,
    YEAR_FILTER,
    PRICE_FILTER,
    MILLION,
    CAR_ID_FILTER,
    ID_FILTER,
    BRAND_FILTER,
    MODEL_FILTER,
    COLOR_FILTER,
    STATUS_FILTER,
    FACTURATION_STATUS_FILTER,
    OWNER_FILTER,
    SPECIFIC_FILTERS_HELP_TEXT
)


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

    def __quick_filter(self, data):
        min_year = data[YEAR_FILTER].min()
        max_year = data[YEAR_FILTER].max()
        min_price = data[PRICE_FILTER].min() / MILLION
        max_price = data[PRICE_FILTER].max() / MILLION

        row1 = st.columns([4, 1, 4])
        self.price_range_ = row1[0].slider(
            "💵 Rango de precio ( ₡1.000.000 )",
            min_value=min_price,
            max_value=max_price,
            value=[
                min_price,
                max_price])
        self.year_range_ = row1[2].slider(
            "📅 Rango de años",
            min_value=min_year,
            max_value=max_year,
            value=[
                min_year,
                max_year])

        row2 = st.columns([4, 1, 4])
        self.car_id_ = row2[0].text_input("🚗 " + CAR_ID_FILTER)
        self.id_ = row2[2].text_input("#️⃣" + ID_FILTER + " (Autos Luis)")

    def __specific_filter(self, data):
        with st.form("CarsSpecificFilters"):
            st.markdown('#### Filtros específicos')
            row3 = st.columns([4, 1, 4, 1, 4])
            self.car_brand_ = row3[0].selectbox(
                '🚓 ' + BRAND_FILTER,
                [SELECT_FILTER] + sorted(data[BRAND_FILTER].unique())
            )
            self.car_model_ = row3[2].selectbox(
                '🛻 ' + MODEL_FILTER,
                [SELECT_FILTER] + sorted(
                    data[MODEL_FILTER].unique())
            )
            self.car_color_ = row3[4].selectbox(
                '🌈 ' + COLOR_FILTER,
                [SELECT_FILTER] + sorted(
                    data[COLOR_FILTER].unique())
            )

            row4 = st.columns([4, 1, 4, 1, 4])
            self.car_status_ = row4[0].selectbox(
                '⁉️ ' + STATUS_FILTER,
                [SELECT_FILTER] + sorted(data[STATUS_FILTER].unique())
            )
            self.car_facturation_ = row4[2].selectbox(
                '🔜 ' +
                FACTURATION_STATUS_FILTER,
                [SELECT_FILTER] +
                sorted(
                    data[FACTURATION_STATUS_FILTER].unique()))
            self.car_owner_ = row4[4].selectbox(
                '🙎🏻 ' + OWNER_FILTER,
                [SELECT_FILTER] + sorted(
                    data[OWNER_FILTER].unique())
            )

            row5 = st.columns([4, 1, 4, 1, 4])
            self.car_year_ = row5[2].selectbox(
                '📅 ' + YEAR_FILTER,
                [SELECT_FILTER] + sorted(data[YEAR_FILTER].unique())
            )

            st.form_submit_button('Buscar')

    def get_filter(self, data):
        st.markdown('#### Filtros')
        self.__quick_filter(data)

        show_sf = st.checkbox("Más filtros",
                              key="Car Checkbox",
                              help=SPECIFIC_FILTERS_HELP_TEXT
                              )
        if show_sf:
            self.__specific_filter(data)

    def apply_filter(self, data):
        filtered_data = data.copy()

        # Quick filters
        filtered_data = filtered_data[
            (filtered_data[PRICE_FILTER] >= self.price_range_[0] * MILLION) &
            (filtered_data[PRICE_FILTER] <= self.price_range_[1] * MILLION)
        ]

        filtered_data = filtered_data[
            (filtered_data[YEAR_FILTER] >= self.year_range_[0]) &
            (filtered_data[YEAR_FILTER] <= self.year_range_[1])
        ]

        if self.car_id_:
            filtered_data = filtered_data[filtered_data[CAR_ID_FILTER].str.contains(
                self.car_id_, case=False, na=False)]

        if self.id_:
            filtered_data = filtered_data[filtered_data[ID_FILTER].str.contains(
                self.id_, case=False, na=False)]

        # Specific filters
        if self.car_brand_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[BRAND_FILTER]
                                          == self.car_brand_]

        if self.car_model_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[MODEL_FILTER]
                                          == self.car_model_]

        if self.car_color_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[COLOR_FILTER]
                                          == self.car_color_]

        if self.car_status_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[STATUS_FILTER]
                                          == self.car_status_]

        if self.car_facturation_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[FACTURATION_STATUS_FILTER]
                                          == self.car_facturation_]

        if self.car_owner_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[OWNER_FILTER]
                                          == self.car_owner_]

        if self.car_year_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[YEAR_FILTER]
                                          == self.car_year_]

        return filtered_data

    def show_filter(self, data):
        st.markdown("---")
        st.markdown('#### Resultados')
        st.dataframe(data, on_select="rerun")
