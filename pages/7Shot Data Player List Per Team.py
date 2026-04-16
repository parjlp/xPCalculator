import pandas as pd
import glob
import os
from csv import DictReader
import streamlit as st

from pathlib import Path

from pathlib import Path
import streamlit as st
import pandas as pd

BASE_DIR = Path(__file__).parent.parent  # goes up from pages/ to project root
DATA_DIR = BASE_DIR / "data"

st.set_page_config(layout="wide")
st.title("National League North Player Shot Stats")

data_path = DATA_DIR / "data" / "master_shots.csv"

df = pd.read_csv(data_path)
df["Post Shot xG"] = df["Post Shot xG"].fillna(0)

teams = df["Attacking Team"].unique()
team = st.selectbox(label="Select Team", options=sorted(teams), index=0)

if team:
    df_team = df[df["Attacking Team"] == team]
    players = df_team["Player Name"].unique()

    player_total_summary = []
    for player in players:
        player_df = df_team[df_team["Player Name"] == player]
        player_total_xg = player_df["xG"].sum()
        player_total_ps_xg = player_df["Post Shot xG"].sum()

        player_total_summary.append({
            "Player": player,
            "Player Total xG": player_total_xg,
            "Player Total Post Shot xG": player_total_ps_xg,
            "Player Total Impact on Post Shot xG": player_total_ps_xg - player_total_xg,
        })

    player_shots_df = pd.DataFrame(player_total_summary)
    player_disp = player_shots_df.sort_values(by="Player Total Impact on Post Shot xG", ascending=False)
    player_disp.insert(0, "Rank", range(1, len(player_disp) + 1))

    st.dataframe(player_disp, hide_index=True)
