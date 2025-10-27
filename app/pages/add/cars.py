import streamlit as st

from constants.constants import (
    BLANK,
    CAR_ID,
    CAR_VIN_ID,
    CAR_DUA_ID,
    CAR_INPUT_DATE,
    DATE_FORMAT,
    CAR_BRAND,
    CAR_MODEL,
    CAR_YEAR,
    CAR_COLOR,
    SELECT_FILTER,
    INITIAL_YEAR,
    CAR_TRANSMISSION_TYPE,
    CAR_MOTOR_TPYE,
    CAR_INPUT_COMMENT,
    NAME,
    CAR_OWNER,
    ADD,
    CAR_DATABASE,
    ID,
    CAR_SELL_DATE,
    CAR_INPUT_PUBLIC_DEED_TYPE,
    CAR_INPUT_PUBLIC_DEED_NUMBER,
    CAR_INPUT_ORIGIN,
    CAR_BUY_DATE,
    CAR_BUY_PRICE,
    CAR_INPUT_PUBLIC_DEED_DATE,
    CAR_INPUT_LAWYER,
    CAR_INPUT_TAX_VALUE,
    CAR_RENT_NUMBER,
    CAR_SELL_BASE_PRICE,
    CAR_STATUS,
    CAR_SELL_PUBLIC_DEED_NUMBER,
    CAR_SELLER_ENTERPRISE,
    CAR_ATTORNEY_POWER,
    CAR_SELL_CURRENCY,
    CAR_SELL_PRICE,
    CAR_SELL_LAWYER,
    CAR_SELL_TYPE,
    CAR_SELL_TYPE_CASH,
    CAR_SELL_TYPE_CAR,
    CAR_SELL_TYPE_LOAN,
    CAR_SELL_PAWN,
    CAR_SELL_PAWN_VALUE,
    CAR_SELLER_WORKER,
    CAR_SELLER_WORKER_COMMISSION,
    CAR_SELL_PUBLIC_DEED_DATE,
    CAR_SELL_TAX_VALUE,
    CAR_SELL_BILL_VALUE,
    CAR_BUYER,
    CAR_BUYER_ID_TYPE,
    CAR_BUYER_ID,
    PHONE,
    MAIL,
    CAR_BUYER_HOME,
    PROVINCE,
    CANTON,
    DISTRICT,
    CONTACT_MEDIA,
    CAR_FACTURATION_STATUS,
    AUTOS_LUIS_NAME,
    ANC_NAME,
    CAR_INPUT_TRANSFER_FEE,
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
        self.car_comment_ = BLANK
        self.car_input_date_ = BLANK
        self.car_input_origin_ = BLANK

        self.car_transmision_ = BLANK
        self.car_motor_ = BLANK

        self.car_sell_base_price_ = BLANK
        self.car_status_ = BLANK

        self.submit_button_ = BLANK

    def __data_to_dict(self):
        # TODO: add documentation
        return {
            # Car characteristics
            ID: "TODO",
            CAR_OWNER: self.car_owner_,
            CAR_BRAND: self.car_brand_,
            CAR_MODEL: self.car_model_,
            CAR_YEAR: self.car_year_,
            CAR_COLOR: self.car_color_,
            CAR_ID: self.car_id_,
            CAR_VIN_ID: self.car_vin_id_,
            CAR_DUA_ID: self.car_dua_id_,
            CAR_INPUT_COMMENT: self.car_comment_,
            CAR_INPUT_DATE: self.car_input_date_,
            CAR_INPUT_ORIGIN: self.car_input_origin_,

            # Buying/input characteristics
            CAR_BUY_DATE: "TODO",
            CAR_BUY_PRICE: "TODO",
            CAR_INPUT_PUBLIC_DEED_TYPE: "TODO",
            CAR_INPUT_PUBLIC_DEED_NUMBER: "TODO",
            CAR_INPUT_TRANSFER_FEE: "TODO",
            CAR_INPUT_PUBLIC_DEED_DATE: "TODO",
            CAR_INPUT_LAWYER: "TODO",
            CAR_INPUT_TAX_VALUE: "TODO",
            CAR_RENT_NUMBER: "TODO",
            CAR_SELL_BASE_PRICE: self.car_sell_base_price_,
            CAR_STATUS: self.car_status_,

            # Sell characteristics. Not used when adding a car.
            CAR_SELL_DATE: BLANK,
            CAR_SELL_PUBLIC_DEED_NUMBER: BLANK,
            CAR_SELL_LAWYER: BLANK,
            CAR_SELLER_ENTERPRISE: BLANK,
            CAR_ATTORNEY_POWER: BLANK,
            CAR_SELL_CURRENCY: BLANK,
            CAR_SELL_PRICE: BLANK,
            CAR_SELL_TYPE: BLANK,
            CAR_SELL_TYPE_CASH: BLANK,
            CAR_SELL_TYPE_CAR: BLANK,
            CAR_SELL_TYPE_LOAN: BLANK,
            CAR_SELL_PAWN: BLANK,
            CAR_SELL_PAWN_VALUE: BLANK,
            CAR_SELLER_WORKER: BLANK,
            CAR_SELLER_WORKER_COMMISSION: BLANK,
            CAR_SELL_PUBLIC_DEED_DATE: BLANK,

            # Sell characteristics: contabillity usage
            CAR_SELL_TAX_VALUE: BLANK,
            CAR_SELL_BILL_VALUE: BLANK,

            # Buyer characteristics
            CAR_BUYER: BLANK,
            CAR_BUYER_ID_TYPE: BLANK,
            CAR_BUYER_ID: BLANK,
            PHONE: BLANK,
            MAIL: BLANK,
            CAR_BUYER_HOME: BLANK,
            PROVINCE: BLANK,
            CANTON: BLANK,
            DISTRICT: BLANK,
            CONTACT_MEDIA: BLANK,
            CAR_FACTURATION_STATUS: "TODO",
        }

    def __get_obligatory_data(
            self,
            car_type_data,
            autos_luis_data,
            car_transmission_data,
            person_data):
        """
        Method that uses streamlit widgets to get the obligatory data from the user
        in order to add a car into the main car-database.

        Uses the car_type_data, autos_luis_data and car_transmission_data datasets
        to show the options in the selectboxes so the user doesn't have to type
        them manually. If any other option is needed, it needs to be added manually
        to the dataset.

        Uses the person_data database that is an internal database from the customer.

        Args:
            self(CarAdder):             Class atributes
            car_type_data(pd):          Pandas variable that contains a dataset
                                        with all the available type of cars.
            autos_luis_data(pd):        Pandas variable that contains a dataset
                                        with autos luis internal types.
            car_transmission_data(pd):  Pandas variable that contains a dataset
                                        with all the type of car transmissions.
            person_data(pd):            Pandas variable that contains a database
                                        with all the persons from the  main
                                        person-database.
        """
        years = get_years_range(INITIAL_YEAR, get_current_year())

        with st.container(border=True):
            # First row
            row0 = st.columns([4, 1, 4, 1, 4])
            self.car_input_date_ = row0[0].date_input(
                "📅 " + CAR_INPUT_DATE, format=DATE_FORMAT,
                key=self.key_ + CAR_INPUT_DATE
            )
            self.car_owner_ = row0[2].selectbox(
                "👩🏽🧑🏼 " + CAR_OWNER,
                [AUTOS_LUIS_NAME, ANC_NAME] + sorted(person_data[NAME]),
                accept_new_options=True,
                key=self.key_ + NAME
            )
            self.car_id_ = row0[4].text_input("🔢 " + CAR_ID, max_chars=6)

            # Second row
            row1 = st.columns([4, 1, 4, 1, 4])
            self.car_brand_ = row1[0].selectbox(
                '🚓 ' + CAR_BRAND,
                [SELECT_FILTER] + sorted(car_type_data[CAR_BRAND].unique()),
                key=self.key_ + CAR_BRAND,
            )
            self.car_model_ = row1[2].selectbox(
                '🛻 ' + CAR_MODEL,
                [SELECT_FILTER] + sorted(car_type_data[car_type_data[CAR_BRAND]
                                                       == self.car_brand_][CAR_MODEL].unique()),
                key=self.key_ + CAR_MODEL
            )
            self.car_year_ = row1[4].selectbox(
                "📅 " + CAR_YEAR,
                [SELECT_FILTER] + sorted(years, reverse=True),
                key=self.key_ + CAR_YEAR,
            )

            # Third row
            row2 = st.columns([4, 1, 4, 1, 4])
            self.car_color_ = row2[0].selectbox(
                "🌈 " + CAR_COLOR,
                [SELECT_FILTER] + sorted(autos_luis_data[CAR_COLOR].dropna()),
                key=self.key_ + CAR_COLOR,
            )
            self.car_motor_ = row2[2].selectbox(
                "🛵💨 " + CAR_MOTOR_TPYE,
                [SELECT_FILTER] +
                sorted(car_transmission_data[CAR_MOTOR_TPYE].unique()),
                key=self.key_ + CAR_MOTOR_TPYE,
            )
            self.car_transmision_ = row2[4].selectbox(
                "⚙️ " + CAR_TRANSMISSION_TYPE,
                [SELECT_FILTER] + sorted(car_transmission_data[car_transmission_data[CAR_MOTOR_TPYE]
                                                               == self.car_motor_][CAR_TRANSMISSION_TYPE]),
                key=self.key_ + CAR_TRANSMISSION_TYPE,
            )

            # Fourth row
            row3 = st.columns([4, 1, 4, 1, 4])
            self.car_input_origin_ = row3[0].selectbox(
                "⁉️ " +
                CAR_INPUT_ORIGIN,
                [SELECT_FILTER] +
                sorted(
                    autos_luis_data[CAR_INPUT_ORIGIN].dropna()),
                key=self.key_ +
                CAR_INPUT_ORIGIN
            )
            self.car_sell_base_price_ = row3[2].number_input(
                "💵 " + CAR_SELL_BASE_PRICE + " ( ₡ )",
                step=1,
                value=None,
                key=self.key_ + CAR_SELL_BASE_PRICE
            )
            self.car_status_ = row3[4].selectbox(
                "⁉️ " +
                CAR_STATUS,
                [SELECT_FILTER] +
                sorted(
                    autos_luis_data[CAR_STATUS].dropna()),
                key=self.key_ + CAR_STATUS
            )

            # Fifth row
            row4 = st.columns([1])
            self.car_comment_ = row4[0].text_area(
                "✍🏽 " + CAR_INPUT_COMMENT
            )

    def __get_non_obligatory_data(
            self,
            car_type_data,
            autos_luis_data,
            car_transmission_data,
            person_data):
        """
        Method that uses streamlit widgets to get the non-obligatory data from the
        user in order to add a car into the main car-database.

        Uses the car_type_data, autos_luis_data and car_transmission_data datasets
        to show the options in the selectboxes so the user doesn't have to type
        them manually. If any other option is needed, it needs to be added manually
        to the dataset.

        Uses the person_data database that is an internal database from the customer.

        Args:
            self(CarAdder):             Class atributes
            car_type_data(pd):          Pandas variable that contains a dataset
                                        with all the available type of cars.
            autos_luis_data(pd):        Pandas variable that contains a dataset
                                        with autos luis internal types.
            car_transmission_data(pd):  Pandas variable that contains a dataset
                                        with all the type of car transmissions.
            person_data(pd):            Pandas variable that contains a database
                                        with all the persons from the  main
                                        person-database.
        """
        with st.container(border=True):
            # First row
            row0 = st.columns([4, 1, 4, 1, 4])
            self.car_vin_id_ = row0[0].text_input(
                "🔢 " + CAR_VIN_ID, max_chars=17
            )
            self.car_dua_id_ = row0[2].text_input(
                "🔢 " + CAR_DUA_ID, max_chars=18
            )
            self.car_input_date_ = row0[4].date_input(
                "📅 " + CAR_BUY_DATE, format=DATE_FORMAT,
                value=None,
                key=self.key_ + CAR_BUY_DATE
            )

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
            autos_luis_data,
            car_transmission_data,
            person_data,
            car_data):
        """
        Public method that handles how the data is recollected and filled into the
        main car-database.

        Uses the car_type_data, autos_luis_data and car_transmission_data datasets
        to show the options in the selectboxes so the user doesn't have to type
        them manually. If any other option is needed, it needs to be added manually
        to the dataset.

        Uses the person_data database that is an internal database from the customer.

        Args:
            self(CarAdder):             Class atributes
            car_type_data(pd):          Pandas variable that contains a dataset
                                        with all the available type of cars.
            autos_luis_data(pd):        Pandas variable that contains a dataset
                                        with autos luis internal types.
            car_transmission_data(pd):  Pandas variable that contains a dataset
                                        with all the type of car transmissions.
            person_data(pd):            Pandas variable that contains a database
                                        with all the persons from the  main
                                        person-database.
            car_data(pd):               Pandas variable that contains a database
                                        with all the cars from the main
                                        car-database.
        """
        st.markdown('#### Datos obligatorios')
        self.__get_obligatory_data(
            car_type_data,
            autos_luis_data,
            car_transmission_data,
            person_data)
        st.markdown('#### Datos no obligatorios')
        self.__get_non_obligatory_data(
            car_type_data,
            autos_luis_data,
            car_transmission_data,
            person_data)
        self.submit_button_ = st.button(ADD)
        st.markdown("---")
        self.__add_data(car_data)
