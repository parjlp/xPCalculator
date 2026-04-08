import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

teams_df = pd.read_csv(DATA_DIR / "with_penalties" / "team_total.csv")
teams_disp = teams_df.sort_values(by="Team Total Impact on Post Shot xG", ascending=False)
teams_disp.insert(0, "League Rank", range(1, len(teams_disp) + 1))

st.dataframe(teams_disp, hide_index=True)


