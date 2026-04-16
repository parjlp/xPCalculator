import streamlit as st
import pandas as pd
import numpy as np
import random
from pathlib import Path

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent  # goes up from pages/ to project root
DATA_DIR = BASE_DIR / "data"

st.set_page_config(layout="wide")
st.title(body="National League North Expected Points By Team")

results = pd.read_csv(DATA_DIR /"results.csv")
teams = results["Home Team"].unique()

col1, col2 = st.columns([1, 4])

with col1:
    team_select = st.selectbox(label="Select Team", options=teams, index=0)

if team_select:
    df_team = results[(results["Home Team"] == team_select) |
                      (results["Away Team"] == team_select)].copy()
    df_team["Date"] = pd.to_datetime(df_team["Date"], format="%d/%m/%Y")
    df_team_disp = df_team.sort_values(by="Date")

    with col2:
        df_final = df_team_disp[["Home Team", "Away Team", "Home Team xP", "Away Team xP", "Home Team xG", "Away Team xG"]]
        st.dataframe(df_final, hide_index=True)
