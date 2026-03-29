import streamlit as st
import pandas as pd
import numpy as np
import random
st.set_page_config(layout="wide")
st.title(body="National League North Justice Tables")
csv_path = "justice_table.csv"

col1, col2 = st.columns([1,4])


if user_input == "Expected Points Per Game":
    jt = pd.read_csv(csv_path)
    jt = jt[["Team", "Expected Points Per Game"]]
    jt_disp = jt.sort_values(by="Expected Points Per Game", ascending=False)
    jt_disp.insert(0, "Position", list(range(len(jt_disp))))
    jt_disp["Position"] = jt_disp["Position"] + 1
    with col2:
        st.dataframe(data=jt_disp, hide_index=True, height='content')
elif user_input == "Expected Goals Per Game":
    jt = pd.read_csv(csv_path)
    jt = jt[["Team", "Expected Goals Per Game"]]
    jt_disp = jt.sort_values(by="Expected Goals Per Game", ascending=False)
    jt_disp.insert(0, "Position", list(range(len(jt_disp))))
    jt_disp["Position"] = jt_disp["Position"] + 1
    with col2:
        st.dataframe(data=jt_disp, hide_index=True, height='content')
elif user_input == "Expected Win %":
    jt = pd.read_csv(csv_path)
    jt = jt[["Team", "Expected Win %"]]
    jt_disp = jt.sort_values(by="Expected Win %", ascending=False)
    jt_disp.insert(0, "Position", list(range(len(jt_disp))))
    jt_disp["Position"] = jt_disp["Position"] + 1
    with col2:
        st.dataframe(data=jt, hide_index=True, height='content')
elif user_input == "Expected Loss %":
    jt = pd.read_csv(csv_path)
    jt = jt[["Team", "Expected Loss %"]]
    jt_disp = jt.sort_values(by="Expected Loss %", ascending=False)
    jt_disp.insert(0, "Position", list(range(len(jt_disp))))
    jt_disp["Position"] = jt_disp["Position"] + 1
    with col2:
        st.dataframe(data=jt, hide_index=True, height='content')
elif user_input == "Expected Draw %":
    jt = pd.read_csv(csv_path)
    jt = jt[["Team", "Expected Draw %"]]
    jt_disp = jt.sort_values(by="Expected Draw %", ascending=False)
    jt_disp.insert(0, "Position", list(range(len(jt_disp))))
    jt_disp["Position"] = jt_disp["Position"] + 1
    with col2:
        st.dataframe(data=jt_disp, hide_index=True, height='content')


with col1:
    data_options = ["Expected Points Per Game", "Expected Goals Per Game", "Expected Win %", "Expected Loss %", "Expected Draw %"]
    user_input = st.selectbox(label="Select Dataset", options=data_options, index=False, accept_new_options=False)





    












