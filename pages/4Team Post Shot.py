from pathlib import Path
import streamlit as st
import pandas as pd

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

st.set_page_config(layout="wide")
st.title("National League North Team Shot Stats")

data_path = DATA_DIR / "team_total.csv"

teams_df = pd.read_csv(data_path)
teams_disp = teams_df.sort_values(by="Team Total Impact on Post Shot xG", ascending=False)
teams_disp.insert(0, "League Rank", range(1, len(teams_disp) + 1))

st.dataframe(teams_disp, hide_index=True)



