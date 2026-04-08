import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

st.set_page_config(layout="wide")


players_df = pd.read_csv("C:/Users/parjl/footballapp/data/without_penalties/master_shots.csv")
players = players_df["Player Name"].unique()


player_select = st.selectbox(label="Select Dataset", options=players, index=False, accept_new_options=False)

selected_df = pd.read_csv("C:/Users/parjl/footballapp/data/player_shots/"+player_select+".csv")
#st.dataframe(selected_df)

summary_data = dict()
summary_data["Player Name"] = selected_df["Player Name"].unique()
summary_data["Total xG"] = selected_df["xG"].sum()
summary_data["Total Post Shot xG"] = selected_df["Post Shot xG"].sum()
summary_data["Post Shot / Pre Shot Difference"] = summary_data["Total Post Shot xG"]-summary_data["Total xG"]
summary_data["Average xG"] = selected_df["xG"].mean()
summary_data["Average Post Shot xG"] = selected_df["Post Shot xG"].mean()
summary_data["Average Post Shot / Pre Shot Difference"] = summary_data["Average Post Shot xG"]-summary_data["Average xG"]
    

st.dataframe(data=summary_data, hide_index=True)

