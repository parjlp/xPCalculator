import streamlit as st
import pandas as pd
import numpy as np
import random
st.set_page_config(layout="wide")
st.title(body="National League North Expected Points By Team")

results = pd.read_csv("results.csv")
teams = results["Home Team"].unique()

col1, col2 = st.columns([1,4])
with col1:
    team_select = st.selectbox(label="Select Dataset", options=teams, index=False, accept_new_options=False)

df_team = results[(results["Home Team"] == team_select) |
                    (results["Away Team"] == team_select)]

df_team.loc[:, "Date"] = pd.to_datetime(df_team["Date"], format="%d/%m/%Y")

df_team_disp = df_team.sort_values(by="Date")
with col2:
    df_final = df_team_disp[["Home Team", "Away Team", "Home Team XP", "Away Team XP", "Home Team XG", "Away Team XG"]]
    # df_final.insert(0, "Link To Game", "View Match")

        
    st.table(df_final, hide_index=True)
