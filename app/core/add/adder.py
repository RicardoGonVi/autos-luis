import streamlit as st

from constants.constants import (ADD)
from database.database import append_data, load_database
from typing import final


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

    Example:
    --------
        DATABASE = "path/to/database.csv"
        adder = Adder("adder_example", DATABASE)

        adder.get_data()
        adder.add_data()
    """

    def __init__(self, key: str, csv_path: str):
        """
        Initializes the Adder instance.

        Args:
            key (str):        Unique key used in Streamlit components to avoid conflicts.
            csv_path (str):   Path to the CSV file where data will be stored.
        """
        # Streamlit class atributes
        self.key_ = key
        self.submit_button_ = False
        self.csv_path_ = csv_path
        self.data_ = load_database(csv_path)

    def _validate_data(self) -> bool:
        """
        Method that validates that the introduced data is filled as expected.

        Returns:
            successfull(bool):  True if the validation ran successfully.
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
        self.submit_button_ = st.button(ADD, key=self.key_)
        st.markdown("---")

    @final
    def add_data(self):
        """
        Appends the collected data to the existing database and saves it
        to the CSV file.

        This method converts the current input data into a dictionary,
        validates it, and if the submission is confirmed, appends it to
        the database file. The Streamlit cache is cleared after updating
        """
        # TODO: add a check so that get_data() is ran before
        new_data = self._data_to_dict()

        if self.submit_button_:
            if self._validate_data():
                with st.spinner("Añadiendo datos", show_time=True):
                    append_data(self.data_, self.csv_path_, new_data)
                    st.cache_data.clear()
                st.success("!Datos agregados!")
