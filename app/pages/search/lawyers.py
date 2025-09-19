import streamlit as st
import pandas as pd

from constants.constants import *


class LawyerFilter:
    def __init__(self):
        self.name = SELECT_FILTER
