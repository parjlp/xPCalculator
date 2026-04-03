import streamlit as st
import pandas as pd
import numpy as np
import random

teams_df = pd.read_csv("team_total.csv")

teams_disp = teams_df.sort_values(by="Team Total Impact on Post Shot xG", ascending=False)
teams_disp.insert(0, "League Rank", list(range(len(teams_disp))))
teams_disp["League Rank"] = teams_disp["League Rank"] + 1
st.dataframe(teams_disp, hide_index=True, height="content")



