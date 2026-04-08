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

results = pd.read_csv(DATA_DIR / "with_penalties" / "results.csv")
teams = results["Home Team"].unique()

col1, col2 = st.columns([1, 4])

def load_team(team):
    df = pd.read_csv(DATA_DIR / "team_stats" / f"{team}.csv")
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
    df3 = pd.read_csv(DATA_DIR / "team_stats" / f"{team}.csv")
    df3 = df3[["Team", "xP"]]
    df3["xP5GAv"] = df3["xP"].rolling(window=5).mean()
    df3_disp = df3.sort_values(by="xP5GAv", ascending=False)
    df3_disp.insert(0, "Position", range(1, len(df3_disp) + 1))
    jt_5_game_ave.append(df3_disp)

st.dataframe(data=pd.concat(jt_5_game_ave), hide_index=True)
    
        

