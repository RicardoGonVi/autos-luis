from pandas.testing import assert_frame_equal

from app.core.add.persons import PersonAdder
from app.constants.constants import *
from app.constants.database import *
from app.database.database import load_database, save_database
from app.utils.errors import assert_frame_not_equal
from app.utils.structs import Person


class TestPersonAdder:
    def test_instance(self):
        shared_data = {
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "locations": load_database(LOCATIONS_DATABASE),
        }
        person_adder = PersonAdder(
            "person_adder_example",
            TEST_PERSONS_DATABASE,
            shared_data
        )

        assert isinstance(person_adder, PersonAdder)
        assert person_adder.key_ == "person_adder_example"
        assert person_adder.csv_path_ == TEST_PERSONS_DATABASE
        assert person_adder.submit_button_ is False

        # Target data assert
        expected_df = load_database(TEST_PERSONS_DATABASE)
        assert_frame_equal(person_adder.data_, expected_df)

        # Attributes data assert
        assert isinstance(person_adder.person_, Person)

        expected_df = load_database(GENERAL_OPTIONS_DATABASE)
        assert_frame_equal(person_adder.options_data_, expected_df)

        expected_df = load_database(LOCATIONS_DATABASE)
        assert_frame_equal(person_adder.locations_data_, expected_df)

    def test_get(self):
        shared_data = {
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "locations": load_database(LOCATIONS_DATABASE),
        }
        person_adder = PersonAdder(
            "person_adder_example",
            TEST_PERSONS_DATABASE,
            shared_data
        )

        assert person_adder.get_data()

    def test_add(self):
        shared_data = {
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "locations": load_database(LOCATIONS_DATABASE),
        }
        person_adder = PersonAdder(
            "person_adder_example",
            TEST_PERSONS_DATABASE,
            shared_data
        )
        expected_df = load_database(TEST_PERSONS_DATABASE)

        # Simulating that the submit button hasn't been pressed
        person_adder.get_data()
        person_adder.add_data()
        assert_frame_equal(person_adder.data_, expected_df)

        # Simulating that the submit button was pressed but the data hasn't
        # been filled
        person_adder.get_data()
        person_adder.submit_button_ = True
        person_adder.add_data()
        person_adder.submit_button_ = False
        assert_frame_equal(person_adder.data_, expected_df)

        # Simulating that new data has been added
        person_adder.get_data()
        # Obligatory fields
        person_adder.person_.name = "Ricardo González Víquez"
        person_adder.person_.id = "901180848"
        person_adder.person_.phone = 84657186
        person_adder.person_.mail = "ragv.1999@outlook.com"
        person_adder.person_.location.province = "Heredia"
        person_adder.person_.location.canton = "Santa Bárbara"
        person_adder.person_.location.district = "Purabá"
        person_adder.submit_button_ = True
        person_adder.add_data()
        person_adder.submit_button_ = False
        # TODO: check that everything is added in the expected order
        assert_frame_not_equal(person_adder.data_, expected_df)

        # Drops the added data
        original_data = person_adder.data_[:-1]
        save_database(data=original_data, database=TEST_PERSONS_DATABASE)
        assert_frame_not_equal(person_adder.data_, expected_df)

    def test_validate(self):
        shared_data = {
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "locations": load_database(LOCATIONS_DATABASE),
        }
        person_adder = PersonAdder(
            "person_adder_example",
            TEST_PERSONS_DATABASE,
            shared_data
        )

        # Validate that the data hasn't been filled
        person_adder.get_data()
        assert person_adder._validate_data() is False

        # Validates that the data was filled
        person_adder.person_.name = "Ricardo González Víquez"
        person_adder.person_.id = "901180848"
        person_adder.person_.phone = 84657186
        person_adder.person_.mail = "ragv.1999@outlook.com"
        person_adder.person_.location.province = "Heredia"
        person_adder.person_.location.canton = "Santa Bárbara"
        person_adder.person_.location.district = "Purabá"
        person_adder.submit_button_ = True
        assert person_adder._validate_data() is True

    def test_data_to_dict(self):
        shared_data = {
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "locations": load_database(LOCATIONS_DATABASE),
        }
        person_adder = PersonAdder(
            "person_adder_example",
            TEST_PERSONS_DATABASE,
            shared_data
        )

        # Filling data
        person_adder.person_.name = "Ricardo González Víquez"
        person_adder.person_.id_type = "Física"
        person_adder.person_.id = "901180848"
        person_adder.person_.phone = 84657186
        person_adder.person_.mail = "ragv.1999@outlook.com"
        person_adder.person_.location.province = "Heredia"
        person_adder.person_.location.canton = "Santa Bárbara"
        person_adder.person_.location.district = "Purabá"
        person_adder.person_.contact_media = "Facebook"
        person_adder.person_.type = "Abogado"

        # Check returned type
        result = person_adder._data_to_dict()
        assert isinstance(result, dict)

        # Assertions on returned mapping
        assert result[NAME] == "Ricardo González Víquez"
        assert result[ID_TYPE] == "Física"
        assert result[ID] == "901180848"
        assert result[PHONE] == 84657186
        assert result[MAIL] == "ragv.1999@outlook.com"
        assert result[PROVINCE] == "Heredia"
        assert result[CANTON] == "Santa Bárbara"
        assert result[DISTRICT] == "Purabá"
        assert result[CONTACT_MEDIA] == "Facebook"
        assert result[PERSON_TYPE] == "Abogado"
