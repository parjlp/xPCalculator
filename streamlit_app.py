import streamlit as st
import pandas as pd
import numpy as np
import random

st.title('Expected Points Calculator')


st.write("")
st.write("")

team1shots = []
team2shots = []

team1name = ""
team2name = ""

col1, col2 = st.columns(2)
with col1:
  team1name = st.text_input("Enter Team 1 Name", value=None, key="Team 1 Name")
  if team1name is not None:
    team1numberOfChances = st.number_input(f"Enter the number of chances for {team1name}", value=0, placeholder=None, key="Team 1 Chances")
    if team1numberOfChances >0:
      for l in range(int(team1numberOfChances)):
        team1shots.append(st.number_input("Shot xG value?: ", key=f"Team1 chance {l}"))
with col2:
  team2name = st.text_input("Enter Team 2 Name", value=None, key="Team 2 Name")
  if team2name is not None:
    team2numberOfChances = st.number_input(f"Enter the number of chances for {team2name}", value=0, placeholder=None, key="Team 2 Chances")
    if team2numberOfChances >0:
      for m in range(int(team2numberOfChances)):
        team2shots.append(st.number_input("Shot xG value?: ", key=f"Team2 chance {m}"))
  

team1wins = 0
draws = 0
team2wins = 0


with st.form("xP calc", enter_to_submit=False):
  submitted = st.form_submit_button("Submit")
  if submitted:
    for i in range(10000000):
        team1goals = 0
        team2goals = 0
        for j in range(len(team1shots)):
          x = random.random()
          if x < team1shots[j]:
            team1goals += 1
          for k in range(len(team2shots)):
            y = random.random()
            if y < team2shots[k]:
              team2goals += 1
        if team1goals > team2goals:
          team1wins +=1
        elif team1goals < team2goals:
          team2wins += 1
        else:
          draws += 1


team1points = team1wins *3 + draws
team2points = team2wins *3 + draws

result = pd.DataFrame({f'{team1name} xPts' : [team1points/10000000],
                       f'{team2name} xPts' : [team2points/10000000],
                       f'{team1name} Win %' : [team1wins/100000],
                       f'{team2name} Win %' : [team2wins/100000],
                       'Draw %' : [draws/100000]})


styled_df = result.style.set_properties(**{
  "text-align": "center"
})
                       
result.set_index(f'{team1name} xPts')



if submitted:
  st.write(styled_df.to_html(), unsafe_allow_html=True)





