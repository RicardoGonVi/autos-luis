import streamlit as st

from constants.constants import (
    BLANK,
    CAR_ID_ADDER,
    CAR_VIN_ID_ADDER,
    CAR_DUA_ID_ADDER,
    CAR_INPUT_DATE_ADDER,
    DATE_FORMAT
)


class CarAdder:
    def __init__(self):
        self.car_id_ = BLANK
        self.car_vin_id_ = BLANK

    def obligatory_data(self):
        with st.form("CarsObligatoryData"):
            # st.markdown('#### Elementos obligatorios')

            row0 = st.columns([4, 1, 4, 1, 4])
            self.car_id_ = row0[0].text_input("🚗 " + CAR_ID_ADDER, max_chars=6)
            self.car_vin_id_ = row0[2].number_input(
                "🚗 " + CAR_VIN_ID_ADDER, value=None, step=1, min_value=0)
            self.car_vin_id_ = row0[4].number_input(
                "🚗 " + CAR_DUA_ID_ADDER, value=None, step=1, min_value=0)

            row1 = st.columns([4, 1, 4, 1, 4])
            self.car_id_ = row1[0].date_input(
                "🚗 " + CAR_INPUT_DATE_ADDER, format=DATE_FORMAT)
            self.car_vin_id_ = row1[2].date_input(
                "🚗 " + CAR_VIN_ID_ADDER, format=DATE_FORMAT)
            self.car_vin_id_ = row1[4].date_input(
                "🚗 " + CAR_DUA_ID_ADDER, format=DATE_FORMAT)

            st.form_submit_button('Agregar')

    def get_adder(self):
        st.markdown('#### Datos')
        self.obligatory_data()
