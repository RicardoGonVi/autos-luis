import streamlit as st
from datetime import date as d
from dataclasses import dataclass, field

from constants.constants import INCLUDE_LAST


@st.cache_data(ttl=600)
def get_years_range(init: int, end: int):
    """
    Gets a list containing all the years between the initial and final year
    of a given range, inclusive.

    This function is cached for 10 minutes (600 seconds) to improve performance
    when repeatedly accessed.

    Args:
        init (int):     The initial year of the range.
        end (int):      The final year of the range.

    Returns:
        years (list):   A list of years from the initial year to the final year.
    """
    years: list = list(range(init, end + INCLUDE_LAST))

    return years


@st.cache_data(ttl=600)
def get_current_year():
    """
    Gets the current year based on the system date.

    This function is cached for 10 minutes (600 seconds) to improve performance
    when repeatedly accessed.

    Returns:
        current_year (int):  The current year.
    """
    today = d.today()
    current_year: int = today.year

    return current_year


def make_tabs(*names):
    """Wrapper around st.tabs returning the created tab objects."""
    if len(names) == 1 and isinstance(names[0], (list, tuple)):
        names = names[0]
    return st.tabs(list(names))


@dataclass
class Location:
    """
    Represents the geographical location of an entity.

    Attributes:
        province (str):         Name of the province.
        canton (str):           Name of the canton.
        district (str):         Name of the district.
        exact_location (str):   Specific address.
    """
    province: str = ""
    canton: str = ""
    district: str = ""
    exact_location: str = ""


@dataclass
class Person:
    """
    Represents a person's identification and contact information.

    Attributes:
        contact_media (str):  Preferred method of contact (e.g., email, phone).
        id (str):             Identification number of the person.
        id_type (str):        Type of identification (person ID, enterprise ID).
        name (str):           Full name of the person.
        mail (str):           Email address of the person.
        type (str):           Type of person (individual or legal entity).
        phone (int):          Contact phone number.
        location (Location):  Geographical location details associated with the person.
    """
    contact_media: str = ""
    id: str = ""
    id_type: str = ""
    name: str = ""
    mail: str = ""
    type: str = ""
    phone: int = 0
    location: Location = field(default_factory=Location)


@dataclass
class TransactionInfo:
    """
    Represents basic information about a financial transaction.

    Attributes:
        date (date):       Date when the transaction occurred.
        price (int):       Monetary amount of the transaction.
        currency (str):    Currency used in the transaction ("USD", "CRC").
    """
    date: d = None
    price: int = 0
    currency: str = 0


@dataclass
class PaymentInfo:
    """
    Represents payment details related to a vehicle transaction.

    Attributes:
        payment_type (str):     Method of payment (e.g., cash, financing, trade-in).
        currency (str):         Currency used for the payment.
        vehicle_received (str): Identifier of the traded-in vehicle, if any.
        cash_amount (float):    Amount paid in cash.
        trade_in_value (float): Value assigned to the traded-in vehicle.
        financing (bool):       Indicates whether financing was used.
        pawn_number (str):      Identifier or reference number of the pawn, if applicable.
        pawn_amount (float):    Amount covered by the pawn, if applicable.
    """
    payment_type: str = ""
    currency: str = ""
    vehicle_received: str = ""
    cash_amount: float = 0.0
    trade_in_value: float = 0.0
    financing: bool = False
    pawn_number: str = ""
    pawn_amount: float = 0.0


@dataclass
class LegalInfo:
    """
    Represents legal information associated with a vehicle transfer or transaction.

    Attributes:
        public_deed_type (str):    Type of public deed (sale, pawn).
        public_deed_number (str):  Official number of the public deed.
        public_deed_date (date):   Date when the public deed was issued.
        transfer_fee (float):      Fee paid for the ownership transfer.
        tax_value (float):         Declared tax value for the transaction.
        lawyer (Person):           Lawyer responsible for handling the legal process.
    """
    public_deed_type: str = ""
    public_deed_number: str = ""
    public_deed_date: d = None
    transfer_fee: float = 0.0
    tax_value: float = 0.0
    lawyer: Person = field(default_factory=Person)


@dataclass
class CarRegistration:
    """
    Represents the registration details of a vehicle, including ownership and legal information.

    Attributes:
        owner (Person):        Current owner of the vehicle.
        date (date):           Date when the vehicle was registered.
        origin (str):          Origin of the vehicle (bought, imported, received, ANC).
        rent_unit (str):       Unit or entity associated with the vehicle rental, if applicable.
        status (str):          Current registration status of the vehicle (Available, reserved,
                               sold, reparation, returned, borrowed).
        legal (LegalInfo):     Legal details related to the registration process.
    """
    owner: Person = field(default_factory=Person)
    date: d = None
    origin: str = ""
    rent_unit: str = ""
    status: str = ""

    # Legal info
    legal: LegalInfo = field(default_factory=LegalInfo)


@dataclass
class CarSell:
    """
    Represents detailed information about a vehicle sale transaction.

    Attributes:
        base_price (float):           Base price of the vehicle to be used as a base when selling a car.
        seller_commission (float):    Commission amount earned by the seller.
        facturation_price (float):    Final invoiced price of the vehicle.
        facturation_status (str):     Current status of the invoice (e.g., pending, issued, paid).

        transaction (TransactionInfo):  General transaction details such as date, price, and currency.
        legal (LegalInfo):              Legal information related to the sale.
        payment (PaymentInfo):          Payment details, including method and amounts.

        enterprise_seller (Person):     Business entity responsible for the sale, if applicable.
        seller (Person):                Individual or agent who conducted the sale.
        buyer (Person):                 Person or entity purchasing the vehicle.
    """
    base_price: float = 0.0
    seller_commission: float = 0.0
    facturation_price: float = 0.0
    facturation_status: str = ""

    transaction: TransactionInfo = field(default_factory=TransactionInfo)
    legal: LegalInfo = field(default_factory=LegalInfo)
    payment: PaymentInfo = field(default_factory=PaymentInfo)

    enterprise_seller: Person = field(default_factory=Person)
    seller: Person = field(default_factory=Person)
    buyer: Person = field(default_factory=Person)


@dataclass
class Car:
    """
    Represents a vehicle and its related identification, characteristics,
    registration, purchase, and sale information.

    Attributes:
        unique_code (str):        Internal system-generated unique code for the vehicle.
        id (int):                 Costa Rican vehicle identification.
        vin_id (int):             Vehicle Identification Number (VIN) or related identifier.
        dua_id (int):             Customs declaration identifier (DUA), if applicable.

        brand (str):              Manufacturer or brand of the vehicle.
        model (str):              Model name.
        year (int):               Manufacturing year of the vehicle.
        color (str):              Vehicle color.
        comment (str):            Additional notes or remarks about the vehicle.

        registration (CarRegistration):  Registration details including ownership and legal data.
        purchase (TransactionInfo):      Information about the vehicle’s purchase transaction.
        sell (CarSell):                  Information about the vehicle’s sale transaction.
    """
    unique_code: str = ""
    id: int = 0
    vin_id: int = 0
    dua_id: int = 0
    brand: str = ""
    model: str = ""
    year: int = 0
    color: str = ""
    comment: str = ""

    registration: CarRegistration = field(default_factory=CarRegistration)
    purchase: TransactionInfo = field(default_factory=TransactionInfo)
    sell: CarSell = field(default_factory=CarSell)
