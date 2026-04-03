import streamlit as st
import pandas as pd
import numpy as np
import random

#st.set_page_config(layout="wide")


ave_df = pd.read_csv("player_ave.csv")

ave_df = ave_df[["Player Name", "Player Team", "Player Ave Impact on Post Shot xG"]]


ave_disp = ave_df.sort_values(by="Player Ave Impact on Post Shot xG", ascending=False)
ave_disp.insert(0, "League Rank", list(range(len(ave_disp))))
ave_disp["League Rank"] = ave_disp["League Rank"] + 1
st.dataframe(ave_disp, hide_index=True, height="content")
