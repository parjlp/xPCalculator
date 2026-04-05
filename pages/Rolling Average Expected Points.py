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
        

