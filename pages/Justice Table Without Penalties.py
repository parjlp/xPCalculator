import streamlit as st
import pandas as pd
import numpy as np
import random
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

jt_in = DATA_DIR / "without_penalties" / "results.csv"

st.set_page_config(layout="wide")
st.title(body="National League North Justice Tables Without Penalties")


col1, col2 = st.columns([1,4])


def refresh(data):
    if user_input == "Expected Points Per Game":
        jt = pd.read_csv("C:/Users/parjl/footballapp/data/without_penalties/justice_table.csv")
        jt = jt[["Team", "Expected Points Per Game"]]
        jt_disp = jt.sort_values(by="Expected Points Per Game", ascending=False)
        jt_disp.insert(0, "Position", list(range(len(jt_disp))))
        jt_disp["Position"] = jt_disp["Position"] + 1
        with col2:
            st.dataframe(data=jt_disp, hide_index=True, height='content')
    elif user_input == "Expected Goals Per Game":
        jt = pd.read_csv("C:/Users/parjl/footballapp/data/without_penalties/justice_table.csv")
        jt = jt[["Team", "Expected Goals Per Game"]]
        jt_disp = jt.sort_values(by="Expected Goals Per Game", ascending=False)
        jt_disp.insert(0, "Position", list(range(len(jt_disp))))
        jt_disp["Position"] = jt_disp["Position"] + 1
        with col2:
            st.dataframe(data=jt_disp, hide_index=True, height='content')
    elif user_input == "Expected Win %":
        jt = pd.read_csv("C:/Users/parjl/footballapp/data/without_penalties/justice_table.csv")
        jt = jt[["Team", "Expected Win %"]]
        jt_disp = jt.sort_values(by="Expected Win %", ascending=False)
        jt_disp.insert(0, "Position", list(range(len(jt_disp))))
        jt_disp["Position"] = jt_disp["Position"] + 1
        with col2:
            st.dataframe(data=jt, hide_index=True, height='content')
    elif user_input == "Expected Loss %":
        jt = pd.read_csv("C:/Users/parjl/footballapp/data/without_penalties/justice_table.csv")
        jt = jt[["Team", "Expected Loss %"]]
        jt_disp = jt.sort_values(by="Expected Loss %", ascending=False)
        jt_disp.insert(0, "Position", list(range(len(jt_disp))))
        jt_disp["Position"] = jt_disp["Position"] + 1
        with col2:
            st.dataframe(data=jt, hide_index=True, height='content')
    elif user_input == "Expected Draw %":
        jt = pd.read_csv("C:/Users/parjl/footballapp/data/without_penalties/justice_table.csv")
        jt = jt[["Team", "Expected Draw %"]]
        jt_disp = jt.sort_values(by="Expected Draw %", ascending=False)
        jt_disp.insert(0, "Position", list(range(len(jt_disp))))
        jt_disp["Position"] = jt_disp["Position"] + 1
        with col2:
            st.dataframe(data=jt_disp, hide_index=True, height='content')



with col1:    
    data_options = ["Expected Points Per Game", "Expected Goals Per Game", "Expected Win %", "Expected Loss %", "Expected Draw %"]
    user_input = st.radio(label="Select Dataset", options=data_options)
    st.button(label="Show Selected Data", on_click=refresh, args=[user_input])





    












