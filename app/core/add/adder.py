import streamlit as st

from constants.constants import (ADD)
from database.database import append_data
from typing import final


class Adder:
    """
    Class that adds the data filled by the user into a database.

    To use it the user must create an Adder object, call the get_data()
    method and then the add_data() method.

    Example:
    --------
    from database.database import load_database
    DATABASE = "path/to/database.csv"

    data = load_database(DATABASE)
    adder = Adder("adder_example")

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
        # Streamlit class atributes
        self.key_ = key
        self.submit_button_ = False

    def _validate_data(self) -> bool:
        """
        Method that validates that the introduced data is filled as expected.

        Returns:
            successfull(bool):  True if the validation runned successfully.
                                False if the validation detected an error.
        """
        successfull = True

        # Add logic

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

    def __get_obligatory_data(self):
        """
        Method that uses streamlit widgets to get the obligatory data from the user
        and saves them into the class atributes.
        """
        # Add logic

    def __get_non_obligatory_data(self):
        """
        Method that uses streamlit widgets to get the non-obligatory data from the user
        and saves them into the class atributes.
        """
        # Add logic

    def get_data(self):
        """
        Public method that gets the data from the user.
        """
        st.markdown('#### Datos obligatorios')
        self.__get_obligatory_data()
        st.markdown('#### Datos no obligatorios')
        self.__get_non_obligatory_data()
        self.submit_button_ = st.button(ADD)
        st.markdown("---")

    @final
    def add_data(self, current_data, csv_path):
        """
        Method that appends the new_data into the current_data database and saves
        it into the csv-file.

        Args:
            current_data(pd):   Pandas variable that contains the current database.
            csv_path(str):      Path to csv file to be updated.
        """
        new_data = self._data_to_dict()

        if self.submit_button_:
            if self._validate_data():
                append_data(current_data, csv_path, new_data)
                st.cache_data.clear()
