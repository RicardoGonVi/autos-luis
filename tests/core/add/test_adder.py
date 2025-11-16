from pandas.testing import assert_frame_equal

from app.core.add.adder import *
from app.constants.database import *


class TestAdder:
    def test_instance(self):
        adder = Adder("adder_example", CAR_DATABASE)
        expected_df = load_database(CAR_DATABASE)

        assert isinstance(adder, Adder)
        assert adder.key_ == "adder_example"
        assert adder.csv_path_ == CAR_DATABASE
        assert adder.submit_button_ == False
        assert_frame_equal(adder.data_, expected_df)

    def test_get(self):
        adder = Adder("adder_example2", PERSONS_DATABASE)

        assert adder.get_data()
        assert adder.submit_button_ == False

    def test_add(self):
        adder = Adder("adder_example3", GARAGE_DATABASE)
        expected_df = load_database(GARAGE_DATABASE)

        adder.get_data()
        adder.add_data()

        assert_frame_equal(adder.data_, expected_df)

    def test_validate(self):
        adder = Adder("adder_example3", GARAGE_DATABASE)

        adder.get_data()
        assert adder._validate_data()
