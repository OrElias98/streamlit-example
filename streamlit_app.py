from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st
import json
import streamlit_survey as ss



"""
# The Best wedding of the year!
"""


survey = ss.StreamlitSurvey("Survey Example")


survey.radio("Are you comming to the weeding?", options=["Yes", "No", "Maybe"], horizontal=False)
