import streamlit as st

from app.constants.constants import (
    BLANK,
    SELECT_FILTER,
)
from app.core.add.adder import Adder
from app.utils.structs import Company


class CompanyAdder(Adder):
    """
    Handles the process of adding company-related data into a CSV database.

    This class extends the Adder base class to manage information specific
    to companies. It uses a `Company` object to store and process the data
    before saving it into the CSV database.

    Attributes:
        company (Company):  Instance used to store and manage company-related information.
    """

    def __init__(self, key: str, csv_path: str, shared_data: dict):
        """
        Initializes the CompanyAdder instance.

        Extends the Adder class initialization by adding a Company object to handle
        companies data. It also loads shared datasets to populate Streamlit widgets
        and manage selectable options.

        Args:
            key (str):        Unique key used in Streamlit components to avoid conflicts.
            csv_path (str):   Path to the CSV file where data will be stored.
            shared_data (dict): Dictionary containing datasets shared across multiple adders.
                                Each dataset provides the options displayed in Streamlit widgets
                                or supports validation logic. Expected keys include:

                                # TODO: update datasets
                                "options": General configuration options used to populate
                                dropdowns and other Streamlit widgets.
                                "locations": List with available locations in Costa Rica.

                                Extra keys are safely ignored if not required by this class.

        Examples:
        --------
        Requirements:
        >>> from app.database.database import load_database
        >>> DATABASE = "path/to/database.csv"
        # TODO: update databases example
        >>> GENERAL_OPTIONS_DATABASE = "path/to/database.csv"
        >>> LOCATIONS_DATABASE = "path/to/database.csv"
        >>> shared_data = {
        >>>     "options": load_database(GENERAL_OPTIONS_DATABASE),
        >>>     "locations": load_database(LOCATIONS_DATABASE),
        >>> }

        Usage:
        >>> company_adder = CompanyAdder(key="person_adder", csv_path=DATABASE, shared_data=shared_data)
        >>> company_adder.get_data()
        >>> company_adder.add_data()
        """
        super().__init__(key, csv_path)

        self.person_ = Company()

        # TODO: update databases
        self.options_data_ = shared_data.get("options")
        self.locations_data_ = shared_data.get("locations")
