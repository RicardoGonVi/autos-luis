import streamlit as st

from constants.constants import (ADD)
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
        # TODO: if person id len = 9, if juridica len = 10

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
