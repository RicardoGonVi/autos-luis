import streamlit as st
import pandas as pd

from constants.constants import (
    SELECT_FILTER,
    CAR_YEAR,
    CAR_SELL_BASE_PRICE,
    MILLION,
    CAR_ID,
    ID,
    CAR_BRAND,
    CAR_MODEL,
    CAR_COLOR,
    CAR_STATUS,
    CAR_FACTURATION_STATUS,
    CAR_OWNER,
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
        min_year = data[CAR_YEAR].min()
        max_year = data[CAR_YEAR].max()
        min_price = data[CAR_SELL_BASE_PRICE].min() / MILLION
        max_price = data[CAR_SELL_BASE_PRICE].max() / MILLION

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
        self.car_id_ = row2[0].text_input("🚗 " + CAR_ID)
        self.id_ = row2[2].text_input("#️⃣" + ID + " (Autos Luis)")

    def __specific_filter(self, data):
        with st.form("CarsSpecificFilters"):
            st.markdown('#### Filtros específicos')
            row3 = st.columns([4, 1, 4, 1, 4])
            self.car_brand_ = row3[0].selectbox(
                '🚓 ' + CAR_BRAND,
                [SELECT_FILTER] + sorted(data[CAR_BRAND].unique())
            )
            self.car_model_ = row3[2].selectbox(
                '🛻 ' + CAR_MODEL,
                [SELECT_FILTER] + sorted(
                    data[CAR_MODEL].unique())
            )
            self.car_color_ = row3[4].selectbox(
                '🌈 ' + CAR_COLOR,
                [SELECT_FILTER] + sorted(
                    data[CAR_COLOR].unique())
            )

            row4 = st.columns([4, 1, 4, 1, 4])
            self.car_status_ = row4[0].selectbox(
                '⁉️ ' + CAR_STATUS,
                [SELECT_FILTER] + sorted(data[CAR_STATUS].unique())
            )
            self.car_facturation_ = row4[2].selectbox(
                '🔜 ' +
                CAR_FACTURATION_STATUS,
                [SELECT_FILTER] +
                sorted(
                    data[CAR_FACTURATION_STATUS].unique()))
            self.car_owner_ = row4[4].selectbox(
                '🙎🏻 ' + CAR_OWNER,
                [SELECT_FILTER] + sorted(
                    data[CAR_OWNER].unique())
            )

            row5 = st.columns([4, 1, 4, 1, 4])
            self.car_year_ = row5[2].selectbox(
                '📅 ' + CAR_YEAR,
                [SELECT_FILTER] + sorted(data[CAR_YEAR].unique())
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
            (filtered_data[CAR_SELL_BASE_PRICE] >= self.price_range_[0] * MILLION) &
            (filtered_data[CAR_SELL_BASE_PRICE] <= self.price_range_[1] * MILLION)
        ]

        filtered_data = filtered_data[
            (filtered_data[CAR_YEAR] >= self.year_range_[0]) &
            (filtered_data[CAR_YEAR] <= self.year_range_[1])
        ]

        if self.car_id_:
            filtered_data = filtered_data[filtered_data[CAR_ID].str.contains(
                self.car_id_, case=False, na=False)]

        if self.id_:
            filtered_data = filtered_data[filtered_data[ID].str.contains(
                self.id_, case=False, na=False)]

        # Specific filters
        if self.car_brand_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CAR_BRAND]
                                          == self.car_brand_]

        if self.car_model_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CAR_MODEL]
                                          == self.car_model_]

        if self.car_color_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CAR_COLOR]
                                          == self.car_color_]

        if self.car_status_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CAR_STATUS]
                                          == self.car_status_]

        if self.car_facturation_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CAR_FACTURATION_STATUS]
                                          == self.car_facturation_]

        if self.car_owner_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CAR_OWNER]
                                          == self.car_owner_]

        if self.car_year_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CAR_YEAR]
                                          == self.car_year_]

        return filtered_data

    def show_filter(self, data):
        st.markdown("---")
        st.markdown('#### Resultados')
        st.dataframe(
            data,
            on_select='rerun',
            hide_index=True,
            selection_mode='single-row')
