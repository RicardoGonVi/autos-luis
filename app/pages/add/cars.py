import streamlit as st

from constants.constants import (
    BLANK,
    CAR_ID_FILTER,
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
    MOTOR_FILTER,
    CAR_COMMENT_ADDER,
    NAME_FILTER,
    OWNER_FILTER,
    ADD,
    CAR_DATABASE,
    ID_FILTER,
    CAR_SELL_DATE,
    CAR_INPUT_PRICE,
    CAR_INPUT_PUBLIC_DEED,
    CAR_NUMBER_INPUT_PUBLIC_DEED,
)
from database.database import append_data
from utils.utils import get_current_year, get_years_range


class CarAdder:
    """
    TODO: add documentation
    """

    def __init__(self, key):
        """
        Class initializer method.

        Args:
            self(CarAdder): Class atributes
            key(str):       Key unique-name used in streamlit gears to
                            differentiate them.
        """
        self.key_ = key
        self.car_owner_ = BLANK
        self.car_brand_ = BLANK
        self.car_model_ = BLANK
        self.car_year_ = BLANK
        self.car_color_ = BLANK
        self.car_id_ = BLANK
        self.car_vin_id_ = BLANK
        self.car_dua_id_ = BLANK
        self.car_input_date_ = BLANK
        self.car_transmision_ = BLANK
        self.car_motor_ = BLANK
        self.car_comment_ = BLANK
        self.submit_button_ = BLANK

    def __data_to_dict(self):
        return {
            # TODO: finish this method
        }

    def __get_obligatory_data(
            self,
            car_type_data,
            color_data,
            car_transmission_data,
            person_data):
        """
        Method that uses streamlit widgets to get the obligatory data from the user
        in order to add a car into the main car-database.

        Uses the car_type_data, color_data and car_transmission_data datasets
        to show the options in the selectboxes so the user doesn't have to type
        them manually. If any other option is needed, it needs to be added manually
        to the dataset.

        Uses the person_data database that is an internal database from the customer.

        Args:
            self(CarAdder):             Class atributes
            car_type_data(pd):          Pandas variable that contains a dataset
                                        with all the available type of cars.
            color_data(pd):             Pandas variable that contains a dataset
                                        with all the type of colors.
            car_transmission_data(pd):  Pandas variable that contains a dataset
                                        with all the type of car transmissions.
            person_data(pd):            Pandas variable that contains a database
                                        with all the persons from the  main
                                        person-database.
        """
        years = get_years_range(INITIAL_YEAR, get_current_year())

        row0 = st.columns([4, 1, 4, 1, 4])
        self.car_id_ = row0[0].text_input("🔢 " + CAR_ID_FILTER, max_chars=6)
        self.car_vin_id_ = row0[2].number_input(
            "🔢 " + CAR_VIN_ID_ADDER, value=None, step=1, min_value=0)
        self.car_dua_id_ = row0[4].number_input(
            "🔢 " + CAR_DUA_ID_ADDER, value=None, step=1, min_value=0)

        row1 = st.columns([4, 1, 4, 1, 4])
        self.car_brand_ = row1[0].selectbox(
            '🚓 ' + BRAND_FILTER,
            [SELECT_FILTER] + sorted(car_type_data[BRAND_FILTER].unique()),
            key=self.key_ + BRAND_FILTER,
        )
        self.car_model_ = row1[2].selectbox(
            '🛻 ' + MODEL_FILTER,
            [SELECT_FILTER] + sorted(car_type_data[car_type_data[BRAND_FILTER]
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
            "🛵💨 " + MOTOR_FILTER,
            [SELECT_FILTER] +
            sorted(car_transmission_data[MOTOR_FILTER].unique()),
            key=self.key_ + MOTOR_FILTER,
        )
        self.car_transmision_ = row2[4].selectbox(
            "⚙️ " + TRANSMISSION_FILTER,
            [SELECT_FILTER] + sorted(car_transmission_data[car_transmission_data[MOTOR_FILTER]
                                     == self.car_motor_][TRANSMISSION_FILTER]),
            key=self.key_ + TRANSMISSION_FILTER,
        )

        row3 = st.columns([1, 4, 1, 4, 1])
        self.car_input_date_ = row3[1].date_input(
            "📅 " + CAR_INPUT_DATE_ADDER, format=DATE_FORMAT,
            key=self.key_ + CAR_INPUT_DATE_ADDER
        )
        self.car_owner_ = row3[3].selectbox(
            "👩🏽🧑🏼 " + OWNER_FILTER,
            [SELECT_FILTER] + sorted(person_data[NAME_FILTER]),
            accept_new_options=True,
            key=self.key_ + NAME_FILTER
        )

        row4 = st.columns([1])
        self.car_comment_ = row4[0].text_area(
            "✍🏽 " + CAR_COMMENT_ADDER
        )

        row5 = st.columns([4, 1, 4, 1, 4])
        self.submit_button_ = st.button(ADD)

    def __add_data(self, car_data):
        """
        Method that adds the filled data into the main car-database. It ensures
        that the database shows the new data by clearing cache memory of streamlit
        widgets.

        Uses the car_data database that is an internal database from the customer.

        Args:
            self(CarAdder): Class atributes
            car_data(pd):   Pandas variable that contains a database with all
                            the cars from the  main car-database.
        """
        if self.submit_button_:
            append_data(car_data, CAR_DATABASE, self.__data_to_dict())
            st.cache_data.clear()

    def get_data(
            self,
            car_type_data,
            color_data,
            car_transmission_data,
            person_data,
            car_data):
        """
        Public method that handles how the data is recollected and filled into the
        main car-database.

        Uses the car_type_data, color_data and car_transmission_data datasets
        to show the options in the selectboxes so the user doesn't have to type
        them manually. If any other option is needed, it needs to be added manually
        to the dataset.

        Uses the person_data database that is an internal database from the customer.

        Args:
            self(CarAdder):             Class atributes
            car_type_data(pd):          Pandas variable that contains a dataset
                                        with all the available type of cars.
            color_data(pd):             Pandas variable that contains a dataset
                                        with all the type of colors.
            car_transmission_data(pd):  Pandas variable that contains a dataset
                                        with all the type of car transmissions.
            person_data(pd):            Pandas variable that contains a database
                                        with all the persons from the  main
                                        person-database.
            car_data(pd):               Pandas variable that contains a database
                                        with all the cars from the main
                                        car-database.
        """
        st.markdown('#### Datos')
        self.__get_obligatory_data(
            car_type_data,
            color_data,
            car_transmission_data,
            person_data)
        st.markdown("---")
        self.__add_data(car_data)
