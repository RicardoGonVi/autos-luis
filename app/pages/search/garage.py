import streamlit as st
import pandas as pd

from constants.constants import (
    SELECT_FILTER,
    NAME_FILTER,
    ENTERPRISE_ID_FILTER,
    PHONE_FILTER,
    PROVINCE_FILTER,
    CANTON_FILTER,
    DISTRICT_FILTER
)


class GarageFilter:
    def __init__(self):
        self.name_ = SELECT_FILTER
        self.phone_ = SELECT_FILTER
        self.owner_ = SELECT_FILTER
        self.province_ = SELECT_FILTER
        self.district_ = SELECT_FILTER
        self.canton_ = SELECT_FILTER

    def __quick_filter(self, data):
        st.markdown('#### Filtros')

        row1 = st.columns([4, 1, 4, 1, 4])
        self.name_ = row1[0].text_input(
            '🧑🏼‍🔧 ' + NAME_FILTER
        )
        self.id_ = row1[2].text_input(
            '🪪 ' + ENTERPRISE_ID_FILTER
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

    def get_filter(self, data):
        self.__quick_filter(data)
