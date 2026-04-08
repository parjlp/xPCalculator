import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent  # goes up from pages/ to project root
DATA_DIR = BASE_DIR / "data"

csv_in = DATA_DIR / "without_penalties" / "player_stats" / "player_total.csv"
ave_df = pd.read_csv(csv_in)
ave_df = ave_df[["Player Name", "Player Team", "Player Total Impact on Post Shot xG"]]
ave_disp = ave_df.sort_values(by="Player Total Impact on Post Shot xG", ascending=False)
ave_disp.insert(0, "League Rank", range(1, len(ave_disp) + 1))

st.dataframe(ave_disp, hide_index=True)
