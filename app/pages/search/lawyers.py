import streamlit as st
import pandas as pd

from constants.constants import *


class LawyerFilter:
    def __init__(self):
        self.name_ = SELECT_FILTER
        self.mail_ = SELECT_FILTER
        self.phone_ = SELECT_FILTER
        self.id_ = SELECT_FILTER
        self.province_ = SELECT_FILTER
        self.district_ = SELECT_FILTER
        self.canton_ = SELECT_FILTER
