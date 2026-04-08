import streamlit as st
import pandas as pd
import numpy as np
import random
from pathlib import Path

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent  # goes up from pages/ to project root
DATA_DIR = BASE_DIR / "data"

csv_in = DATA_DIR / "without_penalties" / "other_data" / "justice_table.csv"

st.set_page_config(layout="wide")
st.title(body="National League North Justice Tables Without Penalties")

col1, col2 = st.columns([1, 4])

def refresh(data):
    jt = pd.read_csv(csv_in)
    jt = jt[["Team", data]]
    jt_disp = jt.sort_values(by=data, ascending=False)
    jt_disp.insert(0, "Position", range(1, len(jt_disp) + 1))
    with col2:
        st.dataframe(data=jt_disp, hide_index=True)

with col1:
    data_options = ["Expected Points Per Game", "Expected Goals Per Game", "Expected Win %", "Expected Loss %", "Expected Draw %"]
    user_input = st.radio(label="Select Dataset", options=data_options)
    st.button(label="Show Selected Data", on_click=refresh, args=[user_input])

refresh(user_input)  # shows table immediately on load






    












