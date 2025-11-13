from pandas.testing import assert_frame_equal

from app.core.add.cars import CarAdder
from app.constants.database import *
from app.database.database import load_database
from app.utils.utils import Car


class TestCarAdder:
    def test_instance(self):
        shared_data = {
            "car_types": load_database(CAR_TYPES_DATABASE),
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "car_transmissions": load_database(CAR_TRANSMISSIONS_DATABASE),
            "persons": load_database(PERSONS_DATABASE),
        }
        car_adder = CarAdder("car_adder_example", CAR_DATABASE, shared_data)

        assert isinstance(car_adder, CarAdder)
        assert car_adder.key_ == "car_adder_example"
        assert car_adder.csv_path_ == CAR_DATABASE
        assert car_adder.submit_button_ == False

        # Target data assert
        expected_df = load_database(CAR_DATABASE)
        assert_frame_equal(car_adder.data_, expected_df)

        # Attributes data assert
        assert isinstance(car_adder.car_, Car)

        expected_df = load_database(CAR_TYPES_DATABASE)
        assert_frame_equal(car_adder.types_data_, expected_df)

        expected_df = load_database(GENERAL_OPTIONS_DATABASE)
        assert_frame_equal(car_adder.options_data_, expected_df)

        expected_df = load_database(CAR_TRANSMISSIONS_DATABASE)
        assert_frame_equal(car_adder.transmisions_data_, expected_df)

        expected_df = load_database(PERSONS_DATABASE)
        assert_frame_equal(car_adder.persons_data_, expected_df)
