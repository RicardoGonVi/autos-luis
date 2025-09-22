import streamlit as st
import pandas as pd

from constants.constants import (
    SELECT_FILTER,
    NAME_FILTER,
    MAIL_FILTER,
    PHONE_FILTER,
    PERSON_ID_FILTER,
    PROVINCE_FILTER,
    CANTON_FILTER,
    DISTRICT_FILTER,
    PERSON_TYPE_FILTER,
    CONTACT_MEDIA_FILTER,
    MAIN_PERSON_FILTER
)


class PersonFilter:
    def __init__(self):
        self.person_type_ = MAIN_PERSON_FILTER
        self.name_ = SELECT_FILTER
        self.mail_ = SELECT_FILTER
        self.phone_ = SELECT_FILTER
        self.id_ = SELECT_FILTER
        self.province_ = SELECT_FILTER
        self.district_ = SELECT_FILTER
        self.canton_ = SELECT_FILTER
        self.contact_media_ = SELECT_FILTER

    def __quick_filter(self, data):

        row0 = st.columns([2, 4, 2])
        self.person_type_ = row0[1].selectbox(
            'Selecionar: Clientes👩🏻‍⚖️ o abogados🧑🏼‍💼 ', (
                sorted(data[PERSON_TYPE_FILTER].unique(), reverse=True))
        )

        st.markdown('#### Filtros')

        row1 = st.columns([4, 1, 4, 1, 4])
        self.name_ = row1[0].text_input(
            '👩🏽🧑🏼 ' + NAME_FILTER
        )
        self.id_ = row1[2].text_input(
            '🪪 ' + PERSON_ID_FILTER
        )
        self.phone_ = row1[4].text_input(
            '📞 ' + PHONE_FILTER
        )

        row2 = st.columns([4, 1, 4, 1, 4])
        self.province_ = row2[0].selectbox(
            '📍 ' + PROVINCE_FILTER,
            [SELECT_FILTER] + sorted(data[PROVINCE_FILTER].unique())
        )

        self.canton_ = row2[2].selectbox(
            '🏙️ ' + CANTON_FILTER,
            [SELECT_FILTER] + sorted(data[data[PROVINCE_FILTER]
                                     == self.province_][CANTON_FILTER].unique())
        )
        self.district_ = row2[4].selectbox(
            '🗺️ ' + DISTRICT_FILTER,
            [SELECT_FILTER] + sorted(data[(data[PROVINCE_FILTER] == self.province_) &
                                          (data[CANTON_FILTER]
                                           == self.canton_)
                                          ][DISTRICT_FILTER].unique())
        )

        row3 = st.columns([1, 6, 1, 6, 1])
        self.mail_ = row3[1].selectbox(
            '📧 ' + MAIL_FILTER,
            [SELECT_FILTER] + sorted(
                data[MAIL_FILTER].unique())
        )
        self.contact_media_ = row3[3].selectbox(
            '📲 ' + CONTACT_MEDIA_FILTER,
            [SELECT_FILTER] + sorted(
                data[CONTACT_MEDIA_FILTER].unique())
        )

    def get_filter(self, data):
        self.__quick_filter(data)

    def apply_filter(self, data):
        filtered_data = data.copy()

        filtered_data = filtered_data[filtered_data[PERSON_TYPE_FILTER]
                                      == self.person_type_]

        # Filters
        if self.name_:
            filtered_data = filtered_data[filtered_data[NAME_FILTER].str.contains(
                self.name_, case=False, na=False)]

        if self.id_:
            filtered_data = filtered_data[filtered_data[PERSON_ID_FILTER].str.contains(
                self.id_, case=False, na=False)]

        if self.phone_:
            filtered_data = filtered_data[filtered_data[PHONE_FILTER].str.contains(
                self.phone_, case=False, na=False)]

        if self.province_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[PROVINCE_FILTER]
                                          == self.province_]

        if self.canton_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CANTON_FILTER]
                                          == self.canton_]

        if self.district_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[DISTRICT_FILTER]
                                          == self.district_]

        if self.mail_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[MAIL_FILTER]
                                          == self.mail_]

        if self.contact_media_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CONTACT_MEDIA_FILTER]
                                          == self.contact_media_]

        return filtered_data
