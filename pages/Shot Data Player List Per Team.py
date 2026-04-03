import pandas as pd
import random
import glob
import os
from csv import DictReader
import streamlit as st

df = pd.read_csv("master_shots.csv")
df["Post Shot xG"] = df["Post Shot xG"].fillna(0)

teams = players = df["Attacking Team"].unique()
team = st.selectbox(label="Select Data", options=sorted(teams), index=False, accept_new_options=False)

df = df[(df["Attacking Team"]==team)]
players = df["Player Name"].unique()
player_total_summary = []

for player in players:
    player_total_stats = {}
    player_total_xg = df.apply(lambda x: x["xG"]
                                if x["Player Name"] == player
                                else 0, axis=1).sum()
    player_total_ps_xg = df.apply(lambda x: x["Post Shot xG"]
                                if x["Player Name"] == player
                                else 0, axis=1).sum()
    player_total_stats["Player"] = player
    player_total_stats["Player Total xG"] = player_total_xg
    player_total_stats["Player Total Post Shot xG"] = player_total_ps_xg
    player_total_stats["Player Total Impact on Post Shot xG"] = player_total_ps_xg - player_total_xg
    player_total_summary.append(player_total_stats)

player_shots_df = pd.DataFrame(player_total_summary)
player_disp = player_shots_df.sort_values(by="Player Total Impact on Post Shot xG", ascending=False)
player_disp.insert(0, "League Rank", list(range(len(player_disp))))
player_disp["League Rank"] = player_disp["League Rank"] + 1

st.dataframe(player_disp, hide_index=True)
