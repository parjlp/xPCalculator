import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

teams_df = pd.read_csv("C:/Users/parjl/footballapp/data/without_penalties/team_total.csv")

teams_disp = teams_df.sort_values(by="Team Total Impact on Post Shot xG", ascending=False)
teams_disp.insert(0, "League Rank", list(range(len(teams_disp))))
teams_disp["League Rank"] = teams_disp["League Rank"] + 1
st.dataframe(teams_disp, hide_index=True, height="content")



