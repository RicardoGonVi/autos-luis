import streamlit as st
import pandas as pd

from constants.constants import (
    SELECT_FILTER,
    NAME,
    ENTERPRISE_ID,
    PHONE,
    PROVINCE,
    CANTON,
    DISTRICT,
    CONTACT_NAME
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
            '🧑🏼‍🔧 ' + NAME,
            key=self.key_ + "name"
        )
        self.id_ = row1[2].text_input(
            '🪪 ' + ENTERPRISE_ID,
            key=self.key_ + "id"
        )
        self.phone_ = row1[4].text_input(
            '📞 ' + PHONE,
            key=self.key_ + "phone"
        )

        row2 = st.columns([4, 1, 4, 1, 4])
        self.province_ = row2[0].selectbox(
            '📍 ' + PROVINCE,
            [SELECT_FILTER] + sorted(data[PROVINCE].unique()),
            key=self.key_ + "province"
        )

        self.canton_ = row2[2].selectbox(
            '🏙️ ' + CANTON,
            [SELECT_FILTER] + sorted(data[data[PROVINCE]
                                     == self.province_][CANTON].unique()),
            key=self.key_ + "canton"
        )
        self.district_ = row2[4].selectbox(
            '🗺️ ' + DISTRICT,
            [SELECT_FILTER] + sorted(data[(data[PROVINCE] == self.province_) &
                                          (data[CANTON]
                                           == self.canton_)
                                          ][DISTRICT].unique()),
            key=self.key_ + "district"
        )

        row3 = st.columns([1, 4, 1])
        self.contact_name_ = row3[1].selectbox(
            '👩🏽🧑🏼 ' + CONTACT_NAME,
            [SELECT_FILTER] + sorted(data[CONTACT_NAME].unique()),
            key=self.key_ + "contact_name"
        )

    def get_filter(self, data):
        st.markdown('#### Filtros')
        self.__quick_filter(data)

    def apply_filter(self, data):
        filtered_data = data.copy()

        if self.name_:
            filtered_data = filtered_data[filtered_data[NAME].str.contains(
                self.name_, case=False, na=False)]

        if self.id_:
            filtered_data = filtered_data[filtered_data[ENTERPRISE_ID].str.contains(
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

        if self.contact_name_ != SELECT_FILTER:
            filtered_data = filtered_data[filtered_data[CONTACT_NAME]
                                          == self.contact_name_]

        return filtered_data

    def show_filter(self, data):
        st.markdown("---")
        st.markdown('#### Resultados')
        st.dataframe(
            data,
            on_select='rerun',
            hide_index=True,
            selection_mode='single-row')
