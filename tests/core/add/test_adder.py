from pandas.testing import assert_frame_equal

from app.core.add.adder import *
from app.constants.database import *


class TestAdder:
    def test_instance(self):
        object = Adder("adder_example", TEST_CAR_DATABASE)
        expected_df = load_database(TEST_CAR_DATABASE)

        assert isinstance(object, Adder)
        assert object.key_ == "adder_example"
        assert object.csv_path_ == TEST_CAR_DATABASE
        assert object.submit_button_ is False
        assert_frame_equal(object.data_, expected_df)

    def test_get(self):
        object = Adder("adder_example2", TEST_PERSONS_DATABASE)

        assert object.get_data()

    def test_add(self):
        object = Adder("adder_example3", TEST_GARAGE_DATABASE)
        expected_df = load_database(TEST_GARAGE_DATABASE)

        object.get_data()
        object.add_data()

        assert_frame_equal(object.data_, expected_df)

    def test_validate(self):
        object = Adder("adder_example3", TEST_GARAGE_DATABASE)

        object.get_data()
        assert object._validate_data()
