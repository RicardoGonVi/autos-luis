import streamlit as st

from app.constants.constants import (
    BLANK,
    SELECT_FILTER,
    ADD,
    NAME,
    ID_TYPE,
    ID,
    PHYSICAL_ID,
    PHONE,
    MIN_PHONE_LEN,
    MAX_PHONE_LEN,
    MAIL,
    PERSON_TYPE,
    PROVINCE,
    CANTON,
    DISTRICT,
    CONTACT_MEDIA,
    ZERO,
)
from app.core.add.adder import Adder
from app.utils.structs import Person


class PersonAdder(Adder):
    """
    Handles the process of adding person-related data into a CSV database.

    This class extends the Adder base class to manage information specific
    to people. It uses a `Person` object to store and process the data
    before saving it into the CSV database.

    Attributes:
        person (Person):  Instance used to store and manage person-related information.
    """

    def __init__(self, key: str, csv_path: str, shared_data: dict):
        """
        Initializes the PersonAdder instance.

        Extends the Adder class initialization by adding a Person object to handle
        individual person data. It also loads shared datasets to populate Streamlit
        widgets and manage selectable options.

        Args:
            key (str):        Unique key used in Streamlit components to avoid conflicts.
            csv_path (str):   Path to the CSV file where data will be stored.
            shared_data (dict): Dictionary containing datasets shared across multiple adders.
                                Each dataset provides the options displayed in Streamlit widgets
                                or supports validation logic. Expected keys include:

                                "options": General configuration options used to populate
                                dropdowns and other Streamlit widgets.
                                "locations": List with available locations in Costa Rica.

                                Extra keys are safely ignored if not required by this class.

        Examples:
        --------
        Requirements:
        >>> from app.database.database import load_database
        >>> DATABASE = "path/to/database.csv"
        >>> GENERAL_OPTIONS_DATABASE = "path/to/database.csv"
        >>> LOCATIONS_DATABASE = "path/to/database.csv"
        >>> shared_data = {
        >>>     "options": load_database(GENERAL_OPTIONS_DATABASE),
        >>>     "locations": load_database(LOCATIONS_DATABASE),
        >>> }

        Usage:
        >>> person_adder = PersonAdder(key="person_adder", csv_path=DATABASE, shared_data=shared_data)
        >>> person_adder.get_data()
        >>> person_adder.add_data()
        """
        super().__init__(key, csv_path)

        self.person_ = Person()

        self.options_data_ = shared_data.get("options")
        self.locations_data_ = shared_data.get("locations")

    def _validate_data(self) -> bool:
        """
        Method that validates that the introduced data is filled as expected.

        Returns:
            successfull(bool):  True if the validation ran successfully.
                                False if the validation detected an error.
        """
        successfull = True

        if self.person_.id_type == PHYSICAL_ID:
            id_size = 9
        else:
            id_size = 10

        if self.person_.name == BLANK:
            st.error(f"Digite el nombre de la persona a agregar")
            successfull = False

        elif self.person_.id == BLANK:
            st.error("Debe de introducir un número de identificación")
            successfull = False

        elif self.person_.id == ZERO:
            st.error(f"El número de identificación no puede ser {ZERO}")
            successfull = False

        elif len(self.person_.id) != id_size:
            st.error(f"La identificación debe de tener {id_size} dígitos")
            successfull = False

        elif self.person_.phone is None:
            st.error("Introduzca un número de télefono")
            successfull = False

        elif len(str(self.person_.phone)) < MIN_PHONE_LEN:
            st.error(
                f"El télefono debe de tener {MIN_PHONE_LEN} o más dígitos")
            successfull = False

        elif len(str(self.person_.phone)) > MAX_PHONE_LEN:
            st.error(
                f"El télefono no puede tener más de {MAX_PHONE_LEN} dígitos")
            successfull = False

        elif self.person_.mail == BLANK:
            st.error("Introduzca un correo electrónico")
            successfull = False

        elif self.person_.location.province == SELECT_FILTER:
            st.error("Seleccione la provincia")
            successfull = False

        elif self.person_.location.canton == SELECT_FILTER:
            st.error("Seleccione el cantón")
            successfull = False

        elif self.person_.location.district == SELECT_FILTER:
            st.error("Seleccione el distrito")
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
            NAME: self.person_.name,
            ID_TYPE: self.person_.id_type,
            ID: self.person_.id,
            PHONE: self.person_.phone,
            MAIL: self.person_.mail,
            PROVINCE: self.person_.location.province,
            CANTON: self.person_.location.canton,
            DISTRICT: self.person_.location.district,
            CONTACT_MEDIA: self.person_.contact_media,
            PERSON_TYPE: self.person_.type,
        }

    def _get_obligatory_data(self) -> bool:
        """
        Collects the mandatory person information from the user through Streamlit widgets
        and saves it into the corresponding class attributes.

        This method builds a Streamlit form that lets the user input essential person data,
        such as name, ID type, phone number, email, and location. It automatically loads
        available options from the provided datasets so the user can select from predefined
        lists instead of typing manually.
        If a needed option is missing, it must be added manually to the corresponding dataset.

        Uses:
            - `locations_data_`:   Provides Costa Rican available locations.
            - `options_data_`: Supplies general configuration options (e.g., colors, status).

        Notes:
            Updates the internal `Person` instance (`self.persons_`) with the collected data.
        """
        successfull = True

        with st.container(border=True):
            # First row
            row0 = st.columns([4, 1, 4, 1, 4])
            self.person_.name = row0[0].text_input(
                "👩🏽🧑🏼 " + NAME,
                key=self.key_ + NAME
            )
            self.person_.id_type = row0[2].selectbox(
                "🪪 " + ID_TYPE,
                sorted(self.options_data_[ID_TYPE].dropna()),
                key=self.key_ + ID_TYPE
            )
            if self.person_.id_type == PHYSICAL_ID:
                id_size = 9
            else:
                id_size = 10
            self.person_.id = row0[4].text_input(
                "🔢 " + ID,
                max_chars=id_size,
                key=self.key_ + ID
            )

            # Second row
            row1 = st.columns([4, 1, 4, 1, 4])
            self.person_.phone = row1[0].number_input(
                "📱 " + PHONE,
                step=1,
                value=None,
                key=self.key_ + PHONE
            )
            self.person_.mail = row1[2].text_input(
                "📧 " + MAIL,
                key=self.key_ + MAIL
            )
            self.person_.type = row1[4].selectbox(
                "👩🏻‍⚖️🤵🏻 " + PERSON_TYPE,
                self.options_data_[PERSON_TYPE].dropna(),
                key=self.key_ + PERSON_TYPE
            )

            # Third row
            row2 = st.columns([4, 1, 4, 1, 4])
            self.person_.location.province = row2[0].selectbox(
                "📍 " +
                PROVINCE,
                [SELECT_FILTER] +
                sorted(
                    self.locations_data_[PROVINCE].unique()),
                key=self.key_ +
                PROVINCE)
            self.person_.location.canton = row2[2].selectbox(
                "🏙️ " + CANTON,
                [SELECT_FILTER] + sorted(self.locations_data_[self.locations_data_[PROVINCE]
                                         == self.person_.location.province][CANTON].unique()),
                key=self.key_ + CANTON
            )
            self.person_.location.district = row2[4].selectbox(
                "🗺️ " +
                DISTRICT,
                [SELECT_FILTER] +
                sorted(
                    self.locations_data_[
                        self.locations_data_[CANTON] == self.person_.location.canton][DISTRICT].unique()),
                key=self.key_ +
                DISTRICT)

            # Fourth row
            row3 = st.columns([4, 1, 4, 1, 4])
            self.person_.contact_media = row3[2].selectbox(
                "📧📱🌐 " + CONTACT_MEDIA,
                self.options_data_[CONTACT_MEDIA].dropna(),
                key=self.key_ + CONTACT_MEDIA
            )

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

        self.submit_button_ = st.button(ADD, key=self.key_)
        st.markdown("---")

        return successfull
