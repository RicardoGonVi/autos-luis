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
    CAR_RENT_UNIT,
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
    PERSON_TYPE,
    LAWYER,
    CAR_ID_SIZE,
)
from core.add.adder import Adder
from database.database import append_data
from utils.utils import get_current_year, get_years_range


class CarAdder(Adder):
    """
    Class that adds the data filled by the user into a database.

    To use it the user must create a CarAdder object, call the get_data()
    method and then the add_data() method.

    Example:
    --------
    from database.database import load_database
    DATABASE = "path/to/database.csv"

    data = load_database(DATABASE)
    adder = CarAdder("adder_example")

    adder.get_data()
    adder.add_data(data, DATABASE)
    """

    def __init__(self, key):
        """
        Class initializer method.

        Args:
            key(str):       Key unique-name used in streamlit gears to
                            differentiate them.
        """
        super().__init__(key)

        # Car characteristics
        self.unique_code_ = BLANK
        self.owner_ = BLANK
        self.brand_ = BLANK
        self.model_ = BLANK
        self.year_ = BLANK
        self.color_ = BLANK
        self.id_ = BLANK
        self.vin_id_ = BLANK
        self.dua_id_ = BLANK
        self.comment_ = BLANK

        # Buying/input characteristics
        self.input_date_ = BLANK
        self.input_origin_ = BLANK
        self.buy_date_ = BLANK
        self.buy_price_ = BLANK
        self.input_public_deed_type_ = BLANK
        self.input_public_deed_number_ = BLANK
        self.input_transfer_fee_ = BLANK
        self.input_public_deed_date_ = BLANK
        self.input_lawyer_ = BLANK
        self.input_tax_value_ = BLANK
        self.rent_unit_ = BLANK

        # TODO: add to database
        self.transmision_ = BLANK
        self.motor_ = BLANK

        # Sell characteristics. Not used when adding a car.
        self.sell_base_price_ = BLANK
        self.status_ = BLANK

    def _validate_data(self) -> bool:
        """
        Method that validates that the introduced data is filled as expected.

        Returns:
            successfull(bool):  True if the validation runned successfully.
                                False if the validation detected an error.
        """
        successfull = True

        self.id_ = self.id_.upper()
        if len(self.id_) != CAR_ID_SIZE:
            st.error(f"La placa debe de contener {CAR_ID_SIZE} dígitos")
            successfull = False

        elif self.brand_ == SELECT_FILTER:
            st.error("Seleccione la marca del vehículo")
            successfull = False

        elif self.model_ == SELECT_FILTER:
            st.error("Seleccione el modelo del vehículo")
            successfull = False

        elif self.year_ == SELECT_FILTER:
            st.error("Seleccione el año del vehículo")
            successfull = False

        elif self.color_ == SELECT_FILTER:
            st.error("Seleccione el color del vehículo")
            successfull = False

        elif self.motor_ == SELECT_FILTER:
            st.error("Seleccione el motor del vehículo")
            successfull = False

        elif self.transmision_ == SELECT_FILTER:
            st.error("Seleccione la transmisión del vehículo")
            successfull = False

        elif self.input_origin_ == SELECT_FILTER:
            st.error("Seleccione el origen del vehículo")
            successfull = False

        elif self.sell_base_price_ is None:
            st.error("Introduzca el precio base de venta del vehículo")
            successfull = False

        elif self.sell_base_price_ == 0:
            st.error("El precio base de venta debe ser mayor a 0")
            successfull = False

        elif self.status_ == SELECT_FILTER:
            st.error("Seleccione el estado que desea otorgar al vehículo")
            successfull = False

        return successfull

    def _data_to_dict(self) -> dict:
        """
        Method that saves the class atributes in a dictionary variable.

        Returns:
            data(dict): Dictionary that contains all the class atributes data. Used
                        to save the data into a csv-database.
        """
        return {
            # Car characteristics
            ID: self.unique_code_,
            CAR_OWNER: self.owner_,
            CAR_BRAND: self.brand_,
            CAR_MODEL: self.model_,
            CAR_YEAR: self.year_,
            CAR_COLOR: self.color_,
            CAR_ID: self.id_,
            CAR_VIN_ID: self.vin_id_,
            CAR_DUA_ID: self.dua_id_,
            CAR_INPUT_COMMENT: self.comment_,

            # Buying/input characteristics
            CAR_INPUT_DATE: self.input_date_,
            CAR_INPUT_ORIGIN: self.input_origin_,
            CAR_BUY_DATE: self.buy_date_,
            CAR_BUY_PRICE: self.buy_price_,
            CAR_INPUT_PUBLIC_DEED_TYPE: self.input_public_deed_type_,
            CAR_INPUT_PUBLIC_DEED_NUMBER: self.input_public_deed_number_,
            CAR_INPUT_TRANSFER_FEE: self.input_transfer_fee_,
            CAR_INPUT_PUBLIC_DEED_DATE: self.input_public_deed_date_,
            CAR_INPUT_LAWYER: self.input_lawyer_,
            CAR_INPUT_TAX_VALUE: self.input_tax_value_,
            CAR_RENT_UNIT: self.rent_unit_,


            # Sell characteristics. Not used when adding a car.
            CAR_SELL_BASE_PRICE: self.sell_base_price_,
            CAR_STATUS: self.status_,
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
            CAR_FACTURATION_STATUS: BLANK,
        }

    def __get_obligatory_data(
            self,
            car_type_data,
            general_options_data,
            car_transmission_data,
            person_data,
            car_data):
        """
        Method that uses streamlit widgets to get the obligatory data from the user
        and saves them into the class atributes.

        Uses the car_type_data, general_options_data, car_transmission_data, person_data
        and car_data datasets to show the options in the selectboxes so the user doesn't
        have to type them manually. If any other option is needed, it needs to be added
        manually to the dataset.

        Args:
            car_type_data(pd):          Pandas variable that contains a dataset with
                                        all the available brands and models of cars.
            general_options_data(pd):   Pandas variable that contains a dataset with
                                        all the general options.
            car_transmission_data(pd):  Pandas variable that contains a dataset with
                                        all the type of car transmissions.
            person_data(pd):            Pandas variable that contains a database with
                                        all the persons from a person-database.
            car_data(pd):               Pandas variable that contains a database with
                                        all the cars from a car-database.
        """
        self.unique_code_ = "AL" + str(len(car_data) + 1)
        years = get_years_range(INITIAL_YEAR, get_current_year())

        with st.container(border=True):
            # First row
            row0 = st.columns([4, 1, 4, 1, 4])
            self.input_date_ = row0[0].date_input(
                "📅 " + CAR_INPUT_DATE,
                format=DATE_FORMAT,
                key=self.key_ + CAR_INPUT_DATE
            )
            self.owner_ = row0[2].selectbox(
                "👩🏽🧑🏼 " + CAR_OWNER,
                [AUTOS_LUIS_NAME, ANC_NAME] + sorted(person_data[NAME]),
                key=self.key_ + NAME
            )
            self.id_ = row0[4].text_input(
                "🔢 " + CAR_ID, max_chars=CAR_ID_SIZE,
                key=self.key_ + CAR_ID
            )

            # Second row
            row1 = st.columns([4, 1, 4, 1, 4])
            self.brand_ = row1[0].selectbox(
                '🚓 ' + CAR_BRAND,
                [SELECT_FILTER] + sorted(car_type_data[CAR_BRAND].unique()),
                key=self.key_ + CAR_BRAND,
            )
            self.model_ = row1[2].selectbox(
                '🛻 ' + CAR_MODEL,
                [SELECT_FILTER] + sorted(car_type_data[car_type_data[CAR_BRAND]
                                                       == self.brand_][CAR_MODEL].unique()),
                accept_new_options=True,
                key=self.key_ + CAR_MODEL
            )
            self.year_ = row1[4].selectbox(
                "📅 " + CAR_YEAR,
                [SELECT_FILTER] + sorted(years, reverse=True),
                key=self.key_ + CAR_YEAR,
            )

            # Third row
            row2 = st.columns([4, 1, 4, 1, 4])
            self.color_ = row2[0].selectbox(
                "🌈 " +
                CAR_COLOR,
                [SELECT_FILTER] +
                sorted(
                    general_options_data[CAR_COLOR].dropna()),
                key=self.key_ +
                CAR_COLOR,
            )
            self.motor_ = row2[2].selectbox(
                "🛵💨 " + CAR_MOTOR_TPYE,
                [SELECT_FILTER] +
                sorted(car_transmission_data[CAR_MOTOR_TPYE].unique()),
                key=self.key_ + CAR_MOTOR_TPYE,
            )
            self.transmision_ = row2[4].selectbox(
                "⚙️ " + CAR_TRANSMISSION_TYPE,
                [SELECT_FILTER] + sorted(car_transmission_data[car_transmission_data[CAR_MOTOR_TPYE]
                                                               == self.motor_][CAR_TRANSMISSION_TYPE]),
                key=self.key_ + CAR_TRANSMISSION_TYPE,
            )

            # Fourth row
            row3 = st.columns([4, 1, 4, 1, 4])
            self.input_origin_ = row3[0].selectbox(
                "⁉️ " +
                CAR_INPUT_ORIGIN,
                [SELECT_FILTER] +
                sorted(
                    general_options_data[CAR_INPUT_ORIGIN].dropna()),
                key=self.key_ + CAR_INPUT_ORIGIN
            )
            self.sell_base_price_ = row3[2].number_input(
                "💵 " + CAR_SELL_BASE_PRICE + " ( ₡ )",
                step=1,
                value=None,
                key=self.key_ + CAR_SELL_BASE_PRICE
            )
            self.status_ = row3[4].selectbox(
                "⁉️ " +
                CAR_STATUS,
                [SELECT_FILTER] +
                sorted(
                    general_options_data[CAR_STATUS].dropna()),
                key=self.key_ + CAR_STATUS
            )

    def __get_non_obligatory_data(
            self,
            general_options_data,
            person_data):
        """
        Method that uses streamlit widgets to get the non-obligatory data from the user
        and saves them into the class atributes.

        Uses the general_options_data and person_data database, to show the selectboxes
        options in streamlit widgets.

        Args:
            general_options_data(pd):   Pandas variable that contains a dataset with
                                        all the general options.
            person_data(pd):            Pandas variable that contains a database with
                                        all the persons from a person-database.
        """
        with st.container(border=True):
            # First row
            row0 = st.columns([4, 1, 4, 1, 4])
            self.vin_id_ = row0[0].text_input(
                "🔢 " + CAR_VIN_ID, max_chars=17,
                key=self.key_ + CAR_VIN_ID
            )
            self.dua_id_ = row0[2].text_input(
                "🔢 " + CAR_DUA_ID, max_chars=18,
                key=self.key_ + CAR_DUA_ID
            )
            self.rent_unit_ = row0[4].selectbox(
                '🛣️🚗 ' + CAR_RENT_UNIT,
                [SELECT_FILTER] +
                sorted(
                    general_options_data[CAR_RENT_UNIT].dropna()),
                key=self.key_ + CAR_RENT_UNIT
            )

            # Second row
            row1 = st.columns([1])
            self.comment_ = row1[0].text_area(
                "✍🏽 " + CAR_INPUT_COMMENT,
                key=self.key_ + CAR_INPUT_COMMENT
            )

            # Third row
            row2 = st.columns([4, 1, 4, 1, 4])
            self.buy_date_ = row2[0].date_input(
                "📅 " + CAR_BUY_DATE,
                format=DATE_FORMAT,
                value=None,
                key=self.key_ + CAR_BUY_DATE
            )
            self.buy_price_ = row2[2].number_input(
                "💵 " + CAR_BUY_PRICE + " ( ₡ )",
                step=1,
                value=None,
                key=self.key_ + CAR_BUY_PRICE
            )
            self.input_public_deed_type_ = row2[4].selectbox(
                '🚓 ' +
                CAR_INPUT_PUBLIC_DEED_TYPE,
                [SELECT_FILTER] +
                sorted(
                    general_options_data[CAR_INPUT_PUBLIC_DEED_TYPE].dropna()),
                key=self.key_ +
                CAR_INPUT_PUBLIC_DEED_TYPE,
            )

            # Fourth row
            row3 = st.columns([4, 1, 4, 1, 4])
            self.input_public_deed_number_ = row3[0].text_input(
                "📝 " + CAR_INPUT_PUBLIC_DEED_NUMBER,
                key=self.key_ + CAR_INPUT_PUBLIC_DEED_NUMBER
            )
            self.input_transfer_fee_ = row3[2].number_input(
                "💵 " + CAR_INPUT_TRANSFER_FEE,
                step=1,
                value=None,
                key=self.key_ + CAR_INPUT_TRANSFER_FEE
            )
            self.input_public_deed_date_ = row3[4].date_input(
                "📅 " + CAR_INPUT_PUBLIC_DEED_DATE,
                format=DATE_FORMAT,
                value=None,
                key=self.key_ + CAR_INPUT_PUBLIC_DEED_DATE
            )

            # Fifth row
            row4 = st.columns([1, 4, 1, 4, 1])
            self.input_lawyer_ = row4[1].selectbox(
                '🧑🏼‍💼 ' + CAR_INPUT_LAWYER,
                [SELECT_FILTER] +
                sorted(person_data[person_data[PERSON_TYPE] == LAWYER][NAME]),
                key=self.key_ + CAR_INPUT_LAWYER
            )
            self.input_tax_value_ = row4[3].number_input(
                "💵 " + CAR_INPUT_TAX_VALUE + " ( ₡ )",
                step=1,
                value=None,
                key=self.key_ + CAR_INPUT_TAX_VALUE
            )

    def get_data(
            self,
            car_type_data,
            general_options_data,
            car_transmission_data,
            person_data,
            car_data):
        """
        Public method that gets the data from the user.

        Uses the car_type_data, general_options_data, car_transmission_data, person_data
        person_data and car_data datasets to show the options in the selectboxes so the
        user doesn't have to type them manually. If any other option is needed, it needs
        to be added manually to the dataset.

        Uses the  and the  database, to show option in streamlit widgets.

        Args:
            car_type_data(pd):          Pandas variable that contains a dataset with
                                        all the available brands and models of cars.
            general_options_data(pd):   Pandas variable that contains a dataset with
                                        all the general options.
            car_transmission_data(pd):  Pandas variable that contains a dataset with
                                        all the type of car transmissions.
            person_data(pd):            Pandas variable that contains a database with
                                        all the persons from a person-database.
            car_data(pd):               Pandas variable that contains a database with
                                        all the cars from a car-database.
        """
        st.markdown('#### Datos obligatorios')
        self.__get_obligatory_data(
            car_type_data,
            general_options_data,
            car_transmission_data,
            person_data,
            car_data)
        st.markdown('#### Datos no obligatorios')
        self.__get_non_obligatory_data(
            general_options_data,
            person_data)
        self.submit_button_ = st.button(ADD)
        st.markdown("---")

    def add_data(self, current_data, csv_path):
        """
        Method that appends the new_data into the current_data database and saves
        it into the csv-file.

        Args:
            current_data(pd):   Pandas variable that contains the current database.
            csv_path(str):      Path to csv file to be updated.
        """
        return super().add_data(current_data, csv_path)
