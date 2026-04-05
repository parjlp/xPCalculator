import streamlit as st
import pandas as pd
import numpy as np
import random

st.set_page_config(layout="wide")
st.title(body="National League North Justice Tables")


col1, col2 = st.columns([1,4])


def refresh(data):
    if user_input == "Expected Points Per Game":
        jt = pd.read_csv("justice_table.csv")
        jt = jt[["Team", "Expected Points Per Game"]]
        jt_disp = jt.sort_values(by="Expected Points Per Game", ascending=False)
        jt_disp.insert(0, "Position", list(range(len(jt_disp))))
        jt_disp["Position"] = jt_disp["Position"] + 1
        with col2:
            st.dataframe(data=jt_disp, hide_index=True, height='content')
    elif user_input == "Expected Goals Per Game":
        jt = pd.read_csv("justice_table.csv")
        jt = jt[["Team", "Expected Goals Per Game"]]
        jt_disp = jt.sort_values(by="Expected Goals Per Game", ascending=False)
        jt_disp.insert(0, "Position", list(range(len(jt_disp))))
        jt_disp["Position"] = jt_disp["Position"] + 1
        with col2:
            st.dataframe(data=jt_disp, hide_index=True, height='content')
    elif user_input == "Expected Win %":
        jt = pd.read_csv("justice_table.csv")
        jt = jt[["Team", "Expected Win %"]]
        jt_disp = jt.sort_values(by="Expected Win %", ascending=False)
        jt_disp.insert(0, "Position", list(range(len(jt_disp))))
        jt_disp["Position"] = jt_disp["Position"] + 1
        with col2:
            st.dataframe(data=jt, hide_index=True, height='content')
    elif user_input == "Expected Loss %":
        jt = pd.read_csv("justice_table.csv")
        jt = jt[["Team", "Expected Loss %"]]
        jt_disp = jt.sort_values(by="Expected Loss %", ascending=False)
        jt_disp.insert(0, "Position", list(range(len(jt_disp))))
        jt_disp["Position"] = jt_disp["Position"] + 1
        with col2:
            st.dataframe(data=jt, hide_index=True, height='content')
    elif user_input == "Expected Draw %":
        jt = pd.read_csv("justice_table.csv")
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

for team in teams:
    jt_5_game_Ave = {}
    df3 = pd.read_csv(f"{team}.csv")
    df3 = df3["Team", "xP"]
    df3["xP5GAv"] = df3["xP"].rolling(window=5).mean().dropna()
    df3_disp = df3.sort_values(by="xP5GAv", ascending=False)
    df3_disp.insert(0, "Position", list(range(len(df3_disp))))
    df3_disp["Position"] = df3_disp["Position"] + 1
    jt_5_game_Ave.append(df3_disp)
st.dataframe(data=jt_5_game_Ave, hide_index=True, height=content)





    












