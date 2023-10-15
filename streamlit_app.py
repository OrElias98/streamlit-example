import os
import sys

import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils import convert_to_rtl, enter, get_grade, write_grades



"""
# The Best wedding of the year!
"""

host_name = st.selectbox("מי המארחים?", options=["yes", "no", "maybe"])

with st.form("submission"):
    submitted = st.form_submit_button(label="Submit")
    if submitted:
        write_grades(
            host_name=host_name,
        )
