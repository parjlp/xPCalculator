import pandas as pd
import glob
import os
import streamlit as st
from csv import DictReader
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import style
import plotly.express as px
from pathlib import Path
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent  # goes up from pages/ to project root
DATA_DIR = BASE_DIR / "data"

results = pd.read_csv(DATA_DIR / "results.csv")
teams = results["Home Team"].unique()

col1, col2 = st.columns([1, 4])

def load_team(team):
    df = pd.read_csv(DATA_DIR / "team_data" / f"{team}.csv")
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
    df = df.sort_values(by="Date").reset_index(drop=True)
    df["xP5GAv"] = df["xP"].rolling(window=5).mean()
    return df

with col1:
    team1_select = st.selectbox(label="Select Team 1", key="team1", options=teams, index=0)
    team2_select = st.selectbox(label="Select Team 2", key="team2", options=teams, index=0)

with col2:
    if team1_select and team2_select:
        df1 = load_team(team1_select)
        df2 = load_team(team2_select)

        fig = px.line(df1, x="Date", y="xP5GAv", labels={"xP5GAv": "xP 5 Game Avg"}, title="Rolling xP Comparison")
        fig.update_traces(name=team1_select, showlegend=True, line=dict(color="blue", width=3))
        fig.add_scatter(x=df2["Date"], y=df2["xP5GAv"], mode="lines", name=team2_select, showlegend=True, line=dict(color="red", width=3))
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)

jt_5_game_ave = []
for team in teams:
    df3 = pd.read_csv(DATA_DIR / "team_data" / f"{team}.csv")
    df3["Team"] = team
    df3["xP5GAv"] = df3["xP"].rolling(window=5).mean()
    latest = df3[["Team", "xP5GAv"]].dropna().iloc[-1]
    jt_5_game_ave.append(latest)

jt_final = pd.DataFrame(jt_5_game_ave).sort_values(by="xP5GAv", ascending=False)
jt_final.insert(0, "Position", range(1, len(jt_final) + 1))
st.dataframe(data=jt_final, hide_index=True)
    
        

