import streamlit as st

from utils.utils import get_current_year, get_years_range
from constants.constants import (
    BLANK,
    CAR_ID_ADDER,
    CAR_VIN_ID_ADDER,
    CAR_DUA_ID_ADDER,
    CAR_INPUT_DATE_ADDER,
    DATE_FORMAT,
    BRAND_FILTER,
    MODEL_FILTER,
    YEAR_FILTER,
    COLOR_FILTER,
    SELECT_FILTER,
    INITIAL_YEAR,
    TRANSMISSION_FILTER,
    MOTOR_FILTER
)


class CarAdder:
    def __init__(self, key):
        self.key_ = key
        self.car_id_ = BLANK
        self.car_vin_id_ = BLANK
        self.car_dua_id_ = BLANK
        self.car_brand_ = BLANK
        self.car_model_ = BLANK
        self.car_year_ = BLANK
        self.car_color_ = BLANK
        self.car_input_date_ = BLANK
        self.car_transmision_ = BLANK
        self.car_motor_ = BLANK

    def __get_obligatory_data(self, car_data, color_data, car_transmission):
        years = get_years_range(INITIAL_YEAR, get_current_year())
        transmission = ["manual", ]

        row0 = st.columns([4, 1, 4, 1, 4])
        self.car_id_ = row0[0].text_input("🔢 " + CAR_ID_ADDER, max_chars=6)
        self.car_vin_id_ = row0[2].number_input(
            "🔢 " + CAR_VIN_ID_ADDER, value=None, step=1, min_value=0)
        self.car_dua_id_ = row0[4].number_input(
            "🔢 " + CAR_DUA_ID_ADDER, value=None, step=1, min_value=0)

        row1 = st.columns([4, 1, 4, 1, 4])
        self.car_brand_ = row1[0].selectbox(
            '🚓 ' + BRAND_FILTER,
            [SELECT_FILTER] + sorted(car_data[BRAND_FILTER].unique()),
            key=self.key_ + BRAND_FILTER,
        )
        self.car_model_ = row1[2].selectbox(
            '🛻 ' + MODEL_FILTER,
            [SELECT_FILTER] + sorted(car_data[car_data[BRAND_FILTER]
                                              == self.car_brand_][MODEL_FILTER].unique()),
            key=self.key_ + MODEL_FILTER
        )
        self.car_year_ = row1[4].selectbox(
            "📅 " + YEAR_FILTER,
            [SELECT_FILTER] + sorted(years, reverse=True),
            key=self.key_ + YEAR_FILTER,
        )

        row2 = st.columns([4, 1, 4, 1, 4])
        self.car_color_ = row2[0].selectbox(
            "🌈 " + COLOR_FILTER,
            [SELECT_FILTER] + sorted(color_data[COLOR_FILTER]),
            key=self.key_ + COLOR_FILTER,
        )
        self.car_motor_ = row2[2].selectbox(
            "🌈 " + MOTOR_FILTER,
            [SELECT_FILTER] + sorted(car_transmission[MOTOR_FILTER].unique()),
            key=self.key_ + MOTOR_FILTER,
        )
        self.car_transmision_ = row2[4].selectbox(
            "🌈 " + TRANSMISSION_FILTER,
            [SELECT_FILTER] + sorted(car_transmission[car_transmission[MOTOR_FILTER]
                                     == self.car_motor_][TRANSMISSION_FILTER]),
            key=self.key_ + TRANSMISSION_FILTER,
        )

        row3 = st.columns([4, 1, 4, 1, 4])
        self.car_input_date_ = row3[0].date_input(
            "📅 " + CAR_INPUT_DATE_ADDER, format=DATE_FORMAT,
            key=self.key_ + CAR_INPUT_DATE_ADDER
        )

    def get_data(self, car_data, color_data, car_transmission):
        st.markdown('#### Datos')
        self.__get_obligatory_data(car_data, color_data, car_transmission)
