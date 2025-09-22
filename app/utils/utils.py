import streamlit as st


def make_tabs(*names):
    """Wrapper around st.tabs returning the created tab objects."""
    if len(names) == 1 and isinstance(names[0], (list, tuple)):
        names = names[0]
    return st.tabs(list(names))
