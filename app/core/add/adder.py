import streamlit as st
from typing import final

from app.constants.constants import (ADD)
from app.database.database import append_data, load_database


class Adder:
    """
    Handles the process of adding user-submitted data into a CSV database.

    The user must create an Adder instance, call `get_data()` to collect input,
    and then call `add_data()` to store the new record in the database.

    Attributes:
        key (str):             Unique key used in Streamlit components to avoid conflicts.
        submit_button (bool):  Indicates whether the submission button has been pressed.
        csv_path (str):        Path to the CSV file where data will be stored.
        data (pd.DataFrame):   DataFrame containing the current contents of the database.
    """

    def __init__(self, key: str, csv_path: str):
        """
        Initializes the Adder instance.

        Args:
            key (str):        Unique key used in Streamlit components to avoid conflicts.
            csv_path (str):   Path to the CSV file where data will be stored.

        Examples:
        --------
        Requirements:
        >>> DATABASE = "path/to/database.csv"

        Usage:
        >>> car_adder = CarAdder(key="car_adder", csv_path=DATABASE)
        >>> car_adder.get_data()
        >>> car_adder.add_data()
        """
        self.key_ = key
        self.submit_button_ = False
        self.csv_path_ = csv_path
        self.data_ = load_database(csv_path)

    def _validate_data(self) -> bool:
        """
        Validates that the provided data is correctly filled.

        Returns:
            successfull (bool): True if the data passes validation, False otherwise.
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

    def _get_obligatory_data(self) -> bool:
        """
        Collects the obligatory information from the user and saves it into
        the corresponding class attributes.
        """
        successfull = True

        # Add logic

        return successfull

    def _get_non_obligatory_data(self) -> bool:
        """
        Collects the optional information from the user and saves it into
        the corresponding class attributes.
        """
        successfull = True

        # Add logic

        return successfull

    def get_data(self) -> bool:
        """
        Gets the data entered by the user.

        Returns:
            bool: True if all required steps succeed, False otherwise.
        """
        successfull = True

        st.markdown('#### Datos obligatorios')
        if self._get_obligatory_data() is False:
            print("Had an error while getting the obligatory data")
            successfull = False

        st.markdown('#### Datos no obligatorios')
        if self._get_non_obligatory_data() is False:
            print("Had an error while getting the non-obligatory data")
            successfull = False

        self.submit_button_ = st.button(ADD, key=self.key_)
        st.markdown("---")

        return successfull

    @final
    def add_data(self) -> None:
        """
        Appends the collected data to the existing database and saves it
        to the CSV file.

        This method converts the current input data into a dictionary,
        validates it, and if the submission is confirmed, appends it to
        the database file. The Streamlit cache is cleared after updating
        """
        new_data = self._data_to_dict()

        if self.submit_button_:
            if self._validate_data():
                with st.spinner("Añadiendo datos", show_time=True):
                    append_data(self.data_, self.csv_path_, new_data)
                    st.cache_data.clear()
                st.success("!Datos agregados!")
