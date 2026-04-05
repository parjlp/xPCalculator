import pandas as pd
import glob
import os
import streamlit as st
from csv import DictReader
import numpy as np
import plotly.express as px

results = pd.read_csv("results.csv")
teams = results["Home Team"].unique()

col1, col2 = st.columns([1, 4])

with col1:
    team1_select = st.selectbox(label="Select Team", key="team1", options=teams, index=0)
    team2_select = st.selectbox(label="Select Team", key="team2", options=teams, index=0)

with col2:
    if team1_select and team2_select:
        def load_team(team):
            df = pd.read_csv(f"{team}.csv")
            df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
            df = df.sort_values(by="Date").reset_index(drop=True)
            df["xP5GAv"] = df["xP"].rolling(window=5).mean().dropna()
            return df

        df1 = load_team(team1_select)
        df2 = load_team(team2_select)
        
        fig = px.line(df1, x="Date", y="xP5GAv", labels={"xP5GAv": "xP 5 Game Avg"},title="Rolling xP Comparison")

        fig.update_traces(name=team1_select, showlegend=True, line=dict(color="blue", width=3))

        fig.add_scatter(x=df2["Date"], y=df2["xP5GAv"], mode="lines", name=team2_select, showlegend=True, line=dict(color="red", width=3))

        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)

st.divider()
st.subheader("Rolling Five Average Expected Points")
st.text("""A rolling five game average expected points (xP) graph shows how a team's underlying performance has trended over the course of a season, smoothed out over every five game window.

  What the rolling average does:
Instead of plotting each game individually (which is noisy), it takes the average xP across the last 5 games at each point in the season. This smooths out one-off outliers — a freak result or an easy fixture — and reveals the underlying trend more clearly.
How to read it:

Rising line — the team is performing better over recent games
Falling line — form is declining
Consistently high — the team is regularly creating and suppressing good chances
Consistently low — the team is being outplayed most weeks regardless of results

Why it's useful:
Actual points can be misleading over short spells — a team can win three games while playing poorly, or lose three while playing well. The rolling xP graph cuts through that noise and gives a truer picture of form and trajectory.
When comparing two teams (as above) it highlights which team has been the better performing side over time, even if the league table tells a different story.""")
