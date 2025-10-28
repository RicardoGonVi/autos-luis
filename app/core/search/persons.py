import streamlit as st
import pandas as pd

from constants.constants import (
    SELECT_FILTER,
    NAME,
    MAIL,
    PHONE,
    PERSON_ID,
    PROVINCE,
    CANTON,
    DISTRICT,
    PERSON_TYPE,
    CONTACT_MEDIA,
    CUSTOMER
)


class PersonFilter:
    def __init__(self):
        self.person_type_ = CUSTOMER
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
                sorted(data[PERSON_TYPE].unique(), reverse=True))
        )

        row1 = st.columns([4, 1, 4, 1, 4])
        self.name_ = row1[0].text_input(
            '👩🏽🧑🏼 ' + NAME
        )
        self.id_ = row1[2].text_input(
            '🪪 ' + PERSON_ID
        )
        self.phone_ = row1[4].text_input(
            '📞 ' + PHONE
        )

        row2 = st.columns([4, 1, 4, 1, 4])
        self.province_ = row2[0].selectbox(
            '📍 ' + PROVINCE,
            [SELECT_FILTER] + sorted(data[PROVINCE].unique())
        )

        self.canton_ = row2[2].selectbox(
            '🏙️ ' + CANTON,
            [SELECT_FILTER] + sorted(data[data[PROVINCE]
                                     == self.province_][CANTON].unique())
        )
        self.district_ = row2[4].selectbox(
            '🗺️ ' + DISTRICT,
            [SELECT_FILTER] + sorted(data[(data[PROVINCE] == self.province_) &
                                          (data[CANTON]
                                           == self.canton_)
                                          ][DISTRICT].unique())
        )

        row3 = st.columns([1, 6, 1, 6, 1])
        self.mail_ = row3[1].selectbox(
            '📧 ' + MAIL,
            [SELECT_FILTER] + sorted(
                data[MAIL].unique())
        )
        self.contact_media_ = row3[3].selectbox(
            '📲 ' + CONTACT_MEDIA,
            [SELECT_FILTER] + sorted(
                data[CONTACT_MEDIA].unique())
        )

    def get_filter(self, data):
        st.markdown('#### Filtros')
        self.__quick_filter(data)

    def apply_filter(self, data):
        filtered_data = data.copy()

        filtered_data = filtered_data[filtered_data[PERSON_TYPE]
                                      == self.person_type_]

        # Filters
        if self.name_:
            filtered_data = filtered_data[filtered_data[NAME].str.contains(
                self.name_, case=False, na=False)]

        if self.id_:
            filtered_data = filtered_data[filtered_data[PERSON_ID].str.contains(
                self.id_, case=False, na=False)]

        if self.phone_:
            filtered_data = filtered_data[filtered_data[PHONE].str.contains(
                self.phone_, case=False, na=False)]

        if self.province_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[PROVINCE]
                                          == self.province_]

        if self.canton_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CANTON]
                                          == self.canton_]

        if self.district_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[DISTRICT]
                                          == self.district_]

        if self.mail_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[MAIL]
                                          == self.mail_]

        if self.contact_media_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CONTACT_MEDIA]
                                          == self.contact_media_]

        return filtered_data

    def show_filter(self, data):
        st.markdown("---")
        st.markdown('#### Resultados')
        st.dataframe(
            data,
            on_select='rerun',
            hide_index=True,
            selection_mode='single-row')
