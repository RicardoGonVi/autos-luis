from pandas.testing import assert_frame_equal

from app.core.add.cars import CarAdder
from app.constants.database import *
from app.database.database import load_database, save_database
from app.utils.utils import Car
from app.utils.errors import assert_frame_not_equal


class TestCarAdder:
    def test_instance(self):
        shared_data = {
            "car_types": load_database(CAR_TYPES_DATABASE),
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "car_transmissions": load_database(CAR_TRANSMISSIONS_DATABASE),
            "persons": load_database(TEST_PERSONS_DATABASE),
        }
        car_adder = CarAdder(
            "car_adder_example",
            TEST_CAR_DATABASE,
            shared_data)

        assert isinstance(car_adder, CarAdder)
        assert car_adder.key_ == "car_adder_example"
        assert car_adder.csv_path_ == TEST_CAR_DATABASE
        assert car_adder.submit_button_ is False

        # Target data assert
        expected_df = load_database(TEST_CAR_DATABASE)
        assert_frame_equal(car_adder.data_, expected_df)

        # Attributes data assert
        assert isinstance(car_adder.car_, Car)

        expected_df = load_database(CAR_TYPES_DATABASE)
        assert_frame_equal(car_adder.types_data_, expected_df)

        expected_df = load_database(GENERAL_OPTIONS_DATABASE)
        assert_frame_equal(car_adder.options_data_, expected_df)

        expected_df = load_database(CAR_TRANSMISSIONS_DATABASE)
        assert_frame_equal(car_adder.transmisions_data_, expected_df)

        expected_df = load_database(TEST_PERSONS_DATABASE)
        assert_frame_equal(car_adder.persons_data_, expected_df)

    def test_get(self):
        shared_data = {
            "car_types": load_database(CAR_TYPES_DATABASE),
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "car_transmissions": load_database(CAR_TRANSMISSIONS_DATABASE),
            "persons": load_database(TEST_PERSONS_DATABASE),
        }
        car = CarAdder("car_adder_example", TEST_CAR_DATABASE, shared_data)

        assert car.get_data()

    def test_add(self):
        shared_data = {
            "car_types": load_database(CAR_TYPES_DATABASE),
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "car_transmissions": load_database(CAR_TRANSMISSIONS_DATABASE),
            "persons": load_database(TEST_PERSONS_DATABASE),
        }
        car = CarAdder("car_adder_example", TEST_CAR_DATABASE, shared_data)
        expected_df = load_database(TEST_CAR_DATABASE)

        # Simulating that the submit button hasn't been pressed
        car.get_data()
        car.add_data()
        assert_frame_equal(car.data_, expected_df)

        # Simulating that the submit button was pressed but the data hasn't
        # been filled
        car.get_data()
        car.submit_button_ = True
        car.add_data()
        car.submit_button_ = False
        assert_frame_equal(car.data_, expected_df)

        # Simulating that new data has been added
        car.get_data()
        # Obligatory fields
        car.car_.id = "BMS043"
        car.car_.brand = "Toyota"
        car.car_.model = "Yaris"
        car.car_.color = "Blue"
        car.car_.year = "2020"
        car.car_.motor = "Gasolina"
        car.car_.transmission = "Automático"
        car.car_.registration.origin = "Comprado"
        car.car_.sell.base_price = "14000000"
        car.car_.registration.status = "Disponible"
        car.submit_button_ = True
        car.add_data()
        car.submit_button_ = False
        # TODO: check that everything is added in the expected order
        assert_frame_not_equal(car.data_, expected_df)

        # Drops the added data
        original_data = car.data_[:-1]
        save_database(data=original_data, database=TEST_CAR_DATABASE)
        assert_frame_not_equal(car.data_, expected_df)
