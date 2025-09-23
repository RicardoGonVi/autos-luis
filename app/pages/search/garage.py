import streamlit as st
import pandas as pd

from constants.constants import (
    SELECT_FILTER,
    NAME_FILTER,
    ENTERPRISE_ID_FILTER,
    PHONE_FILTER,
    PROVINCE_FILTER,
    CANTON_FILTER,
    DISTRICT_FILTER,
    CONTACT_NAME_FILTER
)


class GarageFilter:
    def __init__(self):
        self.key_ = "GarageFilter_"
        self.name_ = SELECT_FILTER
        self.phone_ = SELECT_FILTER
        self.owner_ = SELECT_FILTER
        self.province_ = SELECT_FILTER
        self.district_ = SELECT_FILTER
        self.canton_ = SELECT_FILTER
        self.contact_name_ = SELECT_FILTER

    def __quick_filter(self, data):
        row1 = st.columns([4, 1, 4, 1, 4])
        self.name_ = row1[0].text_input(
            '🧑🏼‍🔧 ' + NAME_FILTER,
            key=self.key_ + "name"
        )
        self.id_ = row1[2].text_input(
            '🪪 ' + ENTERPRISE_ID_FILTER,
            key=self.key_ + "id"
        )
        self.phone_ = row1[4].text_input(
            '📞 ' + PHONE_FILTER,
            key=self.key_ + "phone"
        )

        row2 = st.columns([4, 1, 4, 1, 4])
        self.province_ = row2[0].selectbox(
            '📍 ' +
            PROVINCE_FILTER,
            [SELECT_FILTER] + sorted(data[PROVINCE_FILTER].unique()),
            key=self.key_ + "province"
        )

        self.canton_ = row2[2].selectbox(
            '🏙️ ' + CANTON_FILTER,
            [SELECT_FILTER] + sorted(data[data[PROVINCE_FILTER]
                                     == self.province_][CANTON_FILTER].unique()),
            key=self.key_ + "canton"
        )
        self.district_ = row2[4].selectbox(
            '🗺️ ' + DISTRICT_FILTER,
            [SELECT_FILTER] + sorted(data[(data[PROVINCE_FILTER] == self.province_) &
                                          (data[CANTON_FILTER]
                                           == self.canton_)
                                          ][DISTRICT_FILTER].unique()),
            key=self.key_ + "district"
        )

        row3 = st.columns([1, 4, 1])
        self.contact_name_ = row3[1].selectbox(
            '👩🏽🧑🏼 ' + CONTACT_NAME_FILTER,
            [SELECT_FILTER] + sorted(data[CONTACT_NAME_FILTER].unique()),
            key=self.key_ + "contact_name"
        )

    def get_filter(self, data):
        st.markdown('#### Filtros')
        self.__quick_filter(data)

    def apply_filter(self, data):
        filtered_data = data.copy()

        if self.name_:
            filtered_data = filtered_data[filtered_data[NAME_FILTER].str.contains(
                self.name_, case=False, na=False)]

        if self.id_:
            filtered_data = filtered_data[filtered_data[ENTERPRISE_ID_FILTER].str.contains(
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

        if self.contact_name_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CONTACT_NAME_FILTER]
                                          == self.contact_name_]

        return filtered_data

    def show_filter(self, data):
        st.markdown("---")
        st.markdown('#### Resultados')
        st.dataframe(data, on_select="rerun")
