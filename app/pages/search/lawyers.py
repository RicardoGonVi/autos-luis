import streamlit as st
import pandas as pd

from constants.constants import (
    SELECT_FILTER,
    NAME_FILTER,
    MAIL_FILTER,
    PHONE_FILTER,
    PERSON_ID_FILTER,
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

    def specific_filter(self, data):
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
        show_sf = st.checkbox("Más filtros", key="Lawyer Checkbox")

        if show_sf:
            self.specific_filter(data)
