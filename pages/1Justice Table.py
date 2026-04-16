import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

st.set_page_config(layout="wide")
st.title("National League North Justice Tables")

csv_in = DATA_DIR / "results.csv"

def calc_xp(csv):
    df = pd.read_csv(csv)

    def team_col(df_team, team, home_col, away_col):
        return df_team.apply(
            lambda x: x[home_col] if x["Home Team"] == team else x[away_col], axis=1
        )

    all_team_stats = []
    for team in df["Home Team"].unique():
        df_team = df[(df["Home Team"] == team) | (df["Away Team"] == team)]
        all_team_stats.append({
            "Team":                     team,
            "Expected Points Per Game": team_col(df_team, team, "Home Team xP",  "Away Team xP").mean(),
            "Expected Goals Per Game":  team_col(df_team, team, "Home Team xG",  "Away Team xG").mean(),
            "Expected Win %":           team_col(df_team, team, "Home Team %",   "Away Team %").mean(),
            "Expected Loss %":          team_col(df_team, team, "Away Team %",   "Home Team %").mean(),
            "Expected Draw %":          df_team["Draw %"].mean(),
        })

    return pd.DataFrame(all_team_stats)

def display_table(df, metric):
    df_disp = df[["Team", metric]].sort_values(by=metric, ascending=False).reset_index(drop=True)
    df_disp.insert(0, "Position", range(1, len(df_disp) + 1))
    col2.dataframe(data=df_disp, hide_index=True, use_container_width=True)

col1, col2 = st.columns([1, 4])

df_jt = calc_xp(csv_in)

data_options = [
    "Expected Points Per Game",
    "Expected Goals Per Game",
    "Expected Win %",
    "Expected Loss %",
    "Expected Draw %"
]

with col1:
    user_input = st.radio(label="Select Dataset", options=data_options)

display_table(df_jt, user_input)
