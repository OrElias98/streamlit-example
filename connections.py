import os

import pandas as pd
import pygsheets
import streamlit as st
from google.oauth2 import service_account

dir_path = os.path.dirname(__file__)


@st.experimental_singleton
def _get_connection(mode: str):
    service_name = "gcp_service_account"
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets[service_name],
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ],
    )
    connection = pygsheets.authorize(custom_credentials=credentials)
    return connection


conn2write = _get_connection("write")
sheet_url2write = st.secrets["private_gsheets_url2"]


def write_to_grades_sheet(df: pd.DataFrame):
    sh = conn2write.open("bemyguest_grades")
    # Define which sheet to open in the file
    wk1 = sh[1]
    cells = wk1.get_all_values(include_tailing_empty_rows=None, include_tailing_empty=False, returnas="matrix")
    last_row = len(cells)
    if last_row > 1:
        wk1.set_dataframe(df, (last_row + 1, 1))
        wk1.delete_rows(last_row + 1)
    else:
        wk1.set_dataframe(df, (1, 1))