import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(layout="wide")
st.title(body="National League North All Shot Data")
st.write("This is all of the raw data, I'm working on analysing it and visualising it in a useful way")

shots = pd.read_csv(master_shots.csv")
shots.insert(0, "Position", list(range(len(shots))))
shots["Position"] = shots["Position"] + 1
st.dataframe(data=shots, hide_index=True, height='content')

