import streamlit as st

from constants.constants import (
    BLANK,
    SELECT_FILTER,
    ADD,
    NAME,
    ID_TYPE,
    ID,
    PHYSICAL_ID,
    PHONE,
    MAX_PHONE_LEN,
    MAIL,
    PERSON_TYPE,
    PROVINCE,
    CANTON,
    DISTRICT,
    CONTACT_MEDIA,
)
from core.add.adder import Adder


class PersonAdder(Adder):
    """
    Class that adds the data filled by the user into a database.

    To use it the user must create an Adder object, call the get_data()
    method and then the add_data() method.

    Example:
    --------
    from database.database import load_database
    DATABASE = "path/to/database.csv"

    data = load_database(DATABASE)
    adder = PersonAdder("adder_example")

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

        self.name_ = BLANK
        self.id_type_ = BLANK
        self.id_ = BLANK
        self.phone_ = BLANK
        self.mail_ = BLANK
        self.type_ = BLANK
        self.province_ = BLANK
        self.canton_ = BLANK
        self.district_ = BLANK
        self.contact_media_ = BLANK

    def _validate_data(self) -> bool:
        """
        Method that validates that the introduced data is filled as expected.

        Returns:
            successfull(bool):  True if the validation runned successfully.
                                False if the validation detected an error.
        """
        successfull = True

        # TODO: validate phone number len

        return successfull

    def _data_to_dict(self) -> dict:
        """
        Method that saves the class atributes in a dictionary variable.

        Returns:
            data(dict): Dictionary that contains all the class atributes data. Used
                        to save the data into a csv-database.
        """
        # Add logic

        return {}

    def __get_obligatory_data(self, general_options_data, locations_data):
        """
        Method that uses streamlit widgets to get the obligatory data from the user
        and saves them into the class atributes.

        Uses the general_options_data and locations_data datasets to show the options in the
        selectboxes, so the user doesn't have to type them manually. If any other option is
        needed, it needs to be added manually to the datasets.

        Args:
            general_options_data(pd):   Pandas variable that contains a dataset with
                                        all the general options.
            locations_data(pd):         Pandas variable that contains a dataset with
                                        all the type of locations available in Costa Rica.
        """
        with st.container(border=True):
            # First row
            row0 = st.columns([4, 1, 4, 1, 4])
            self.name_ = row0[0].text_input(
                "👩🏽🧑🏼 " + NAME,
                key=self.key_ + NAME
            )
            self.id_type_ = row0[2].selectbox(
                "🪪 " + ID_TYPE,
                sorted(general_options_data[ID_TYPE].dropna()),
                key=self.key_ + ID_TYPE
            )
            if self.id_type_ == PHYSICAL_ID:
                id_size = 9
            else:
                id_size = 10
            self.id_ = row0[4].text_input(
                "🔢 " + ID,
                max_chars=id_size,
                key=self.key_ + ID
            )

            # Second row
            row1 = st.columns([4, 1, 4, 1, 4])
            self.phone_ = row1[0].number_input(
                "📱 " + PHONE,
                step=1,
                value=None,
                key=self.key_ + PHONE
            )
            self.mail_ = row1[2].text_input(
                "📧 " + MAIL,
                key=self.key_ + MAIL
            )
            self.type_ = row1[4].selectbox(
                "👩🏻‍⚖️🤵🏻 " + PERSON_TYPE,
                general_options_data[PERSON_TYPE].dropna(),
                key=self.key_ + PERSON_TYPE
            )

            # Third row
            row2 = st.columns([4, 1, 4, 1, 4])
            self.province_ = row2[0].selectbox(
                "📍 " + PROVINCE,
                [SELECT_FILTER] + sorted(locations_data[PROVINCE].unique()),
                key=self.key_ + PROVINCE
            )
            self.canton_ = row2[2].selectbox(
                "🏙️ " + CANTON,
                [SELECT_FILTER] + sorted(locations_data[locations_data[PROVINCE]
                                         == self.province_][CANTON].unique()),
                key=self.key_ + CANTON
            )
            self.district_ = row2[4].selectbox(
                "🗺️ " + DISTRICT,
                [SELECT_FILTER] + sorted(locations_data[locations_data[CANTON]
                                         == self.canton_][DISTRICT].unique()),
                key=self.key_ + DISTRICT
            )

            # Fourth row
            row3 = st.columns([4, 1, 4, 1, 4])
            self.contact_media_ = row3[2].selectbox(
                "📧📱🌐 " + CONTACT_MEDIA,
                general_options_data[CONTACT_MEDIA].dropna(),
                key=self.key_ + CONTACT_MEDIA
            )

    def get_data(self, general_options_data, locations_data):
        """
        Public method that gets the data from the user.
        """
        st.markdown('#### Datos obligatorios')
        self.__get_obligatory_data(general_options_data, locations_data)
        self.submit_button_ = st.button(ADD, key=self.key_)
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
