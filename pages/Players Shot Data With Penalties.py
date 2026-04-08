import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent  # goes up from pages/ to project root
DATA_DIR = BASE_DIR / "data"

st.set_page_config(layout="wide")

players_df = pd.read_csv(DATA_DIR / "with_penalties" / "master_shots.csv")
players = players_df["Player Name"].unique()

player_select = st.selectbox(label="Select Player", options=players, index=0)

if player_select:
    selected_df = pd.read_csv(DATA_DIR / "player_shots" / f"{player_select}.csv")

    summary_data = {
        "Player Name": selected_df["Player Name"].iloc[0],
        "Total xG": selected_df["xG"].sum(),
        "Total Post Shot xG": selected_df["Post Shot xG"].sum(),
        "Post Shot / Pre Shot Difference": selected_df["Post Shot xG"].sum() - selected_df["xG"].sum(),
        "Average xG": selected_df["xG"].mean(),
        "Average Post Shot xG": selected_df["Post Shot xG"].mean(),
        "Average Post Shot / Pre Shot Difference": selected_df["Post Shot xG"].mean() - selected_df["xG"].mean(),
    }

    st.dataframe(data=pd.DataFrame([summary_data]), hide_index=True)

