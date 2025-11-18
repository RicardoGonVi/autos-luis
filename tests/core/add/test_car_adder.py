from pandas.testing import assert_frame_equal

from app.core.add.cars import CarAdder
from app.constants.constants import *
from app.constants.database import *
from app.database.database import load_database, save_database
from app.utils.errors import assert_frame_not_equal
from app.utils.structs import Car


class TestCarAdder:
    def test_instance(self):
        shared_data = {
            "car_types": load_database(CAR_TYPES_DATABASE),
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "car_transmissions": load_database(CAR_TRANSMISSIONS_DATABASE),
            "persons": load_database(TEST_PERSONS_DATABASE),
        }
        car = CarAdder(
            "car_adder_example",
            TEST_CAR_DATABASE,
            shared_data)

        assert isinstance(car, CarAdder)
        assert car.key_ == "car_adder_example"
        assert car.csv_path_ == TEST_CAR_DATABASE
        assert car.submit_button_ is False

        # Target data assert
        expected_df = load_database(TEST_CAR_DATABASE)
        assert_frame_equal(car.data_, expected_df)

        # Attributes data assert
        assert isinstance(car.car_, Car)

        expected_df = load_database(CAR_TYPES_DATABASE)
        assert_frame_equal(car.types_data_, expected_df)

        expected_df = load_database(GENERAL_OPTIONS_DATABASE)
        assert_frame_equal(car.options_data_, expected_df)

        expected_df = load_database(CAR_TRANSMISSIONS_DATABASE)
        assert_frame_equal(car.transmisions_data_, expected_df)

        expected_df = load_database(TEST_PERSONS_DATABASE)
        assert_frame_equal(car.persons_data_, expected_df)

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

    def test_validate(self):
        shared_data = {
            "car_types": load_database(CAR_TYPES_DATABASE),
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "car_transmissions": load_database(CAR_TRANSMISSIONS_DATABASE),
            "persons": load_database(TEST_PERSONS_DATABASE),
        }
        car = CarAdder("car_adder_example", TEST_CAR_DATABASE, shared_data)

        # Validate that the data hasn't been filled
        car.get_data()
        assert car._validate_data() is False

        # Validates that the data was filled
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
        assert car._validate_data() is True

    def test_data_to_dict(self):
        shared_data = {
            "car_types": load_database(CAR_TYPES_DATABASE),
            "options": load_database(GENERAL_OPTIONS_DATABASE),
            "car_transmissions": load_database(CAR_TRANSMISSIONS_DATABASE),
            "persons": load_database(TEST_PERSONS_DATABASE),
        }
        car = CarAdder("car_adder_example", TEST_CAR_DATABASE, shared_data)

        # Filling data
        car.car_.unique_code = "UUID123"
        car.car_.brand = "Toyota"
        car.car_.model = "Corolla"
        car.car_.year = 2020
        car.car_.color = "Red"
        car.car_.motor = "1.8"
        car.car_.transmission = "Automatic"
        car.car_.id = "ABC-123"
        car.car_.vin_id = "VIN123"
        car.car_.dua_id = "DUA123"
        car.car_.comment = "Nice car"

        car.car_.registration.owner.name = "John Doe"
        car.car_.registration.date = "2024-01-01"
        car.car_.registration.origin = "Purchase"
        car.car_.registration.legal.public_deed_type = "TypeA"
        car.car_.registration.legal.public_deed_number = "1234"
        car.car_.registration.legal.transfer_fee = 2500
        car.car_.registration.legal.public_deed_date = "2024-01-02"
        car.car_.registration.legal.lawyer = "Lawyer A"
        car.car_.registration.legal.tax_value = 1000
        car.car_.registration.rent_unit = "Month"
        car.car_.registration.status = "Active"

        car.car_.purchase.date = "2024-01-01"
        car.car_.purchase.currency = "CRC"
        car.car_.purchase.price = 5000000

        car.car_.sell.base_price = 6000000

        # Check returned type
        result = car._data_to_dict()
        assert isinstance(result, dict)

        # Assertions on returned mapping
        assert result[ID_CODE] == "UUID123"
        assert result[CAR_BRAND] == "Toyota"
        assert result[CAR_MODEL] == "Corolla"
        assert result[CAR_YEAR] == 2020
        assert result[CAR_COLOR] == "Red"
        assert result[CAR_MOTOR_TPYE] == "1.8"
        assert result[CAR_TRANSMISSION_TYPE] == "Automatic"
        assert result[CAR_ID] == "ABC-123"
        assert result[CAR_VIN_ID] == "VIN123"
        assert result[CAR_DUA_ID] == "DUA123"
        assert result[CAR_INPUT_COMMENT] == "Nice car"

        # Registration
        assert result[CAR_OWNER] == "John Doe"
        assert result[CAR_INPUT_DATE] == "2024-01-01"
        assert result[CAR_INPUT_ORIGIN] == "Purchase"

        # Registration legal
        assert result[CAR_INPUT_PUBLIC_DEED_TYPE] == "TypeA"
        assert result[CAR_INPUT_PUBLIC_DEED_NUMBER] == "1234"
        assert result[CAR_INPUT_TRANSFER_FEE] == 2500
        assert result[CAR_INPUT_PUBLIC_DEED_DATE] == "2024-01-02"
        assert result[CAR_INPUT_LAWYER] == "Lawyer A"
        assert result[CAR_INPUT_TAX_VALUE] == 1000

        # Rent / status
        assert result[CAR_RENT_UNIT] == "Month"
        assert result[CAR_STATUS] == "Active"

        # Purchase data
        assert result[CAR_BUY_DATE] == "2024-01-01"
        assert result[CAR_BUY_CURRENCY] == "CRC"
        assert result[CAR_BUY_PRICE] == 5000000

        # Sell base price
        assert result[CAR_SELL_BASE_PRICE] == 6000000
