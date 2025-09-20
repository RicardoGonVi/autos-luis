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
)


class LawyerFilter:
    def __init__(self):
        self.name_ = SELECT_FILTER
        self.mail_ = SELECT_FILTER
        self.phone_ = SELECT_FILTER
        self.id_ = SELECT_FILTER
        self.province_ = SELECT_FILTER
        self.district_ = SELECT_FILTER
        self.canton_ = SELECT_FILTER

    def __quick_filter(self, data):
        st.markdown('#### Filtros rápidos')
        row1 = st.columns([4, 1, 4, 1, 4])
        self.province_ = row1[0].selectbox(
            '📍 ' + PROVINCE_FILTER,
            [SELECT_FILTER] + sorted(data[PROVINCE_FILTER].unique())
        )

        self.canton_ = row1[2].selectbox(
            '🏙️ ' + CANTON_FILTER,
            [SELECT_FILTER] + sorted(data[data[PROVINCE_FILTER]
                                     == self.province_][CANTON_FILTER].unique())
        )
        self.district_ = row1[4].selectbox(
            '🗺️ ' + DISTRICT_FILTER,
            [SELECT_FILTER] + sorted(data[(data[PROVINCE_FILTER] == self.province_) &
                                          (data[CANTON_FILTER]
                                           == self.canton_)
                                          ][DISTRICT_FILTER].unique())
        )

    def __specific_filter(self, data):
        with st.form("LawyerSpecificFilters"):
            st.markdown('#### Filtros específicos')
            row1 = st.columns([4, 1, 4, 1, 4])
            self.name_ = row1[0].selectbox(
                '👩🏽‍⚖️ ' + NAME_FILTER,
                [SELECT_FILTER] + sorted(data[NAME_FILTER].unique())
            )
            self.id_ = row1[2].selectbox(
                '🪪 ' + PERSON_ID_FILTER,
                [SELECT_FILTER] + sorted(
                    data[PERSON_ID_FILTER].unique())
            )
            self.phone_ = row1[4].selectbox(
                '📞 ' + PHONE_FILTER,
                [SELECT_FILTER] + sorted(
                    data[PHONE_FILTER].unique())
            )

            row2 = st.columns([2, 4, 2])
            self.mail_ = row2[1].selectbox(
                '📧 ' + MAIL_FILTER,
                [SELECT_FILTER] + sorted(
                    data[MAIL_FILTER].unique())
            )

            st.form_submit_button('Buscar')

    def get_filter(self, data):
        self.__quick_filter(data)

        show_sf = st.checkbox("Más filtros", key="Lawyer Checkbox")
        if show_sf:
            self.__specific_filter(data)

    def apply_filter(self, data):
        filtered_data = data.copy()

        # Quick filters
        if self.province_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[PROVINCE_FILTER]
                                          == self.province_]

        if self.canton_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CANTON_FILTER]
                                          == self.canton_]

        if self.district_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[DISTRICT_FILTER]
                                          == self.district_]

        return filtered_data
