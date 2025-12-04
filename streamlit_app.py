import streamlit as st
import pandas as pd
import random

st.title('Expected Points Calculator')


st.write("It's very basic right now, just have a play!!")
st.write("Can't believe you bet on Liverpool to lose, you're dead to me")
st.write("")
st.write("")

team1shots = []
team2shots = []

team1name = ""
team2name = ""

team1name = st.text_input("Enter Team 1 Name", key="Team 1 Name")

team1numberOfChances = st.number_input(f"Enter the number of chances for {team1name}", key="Team 1 Chances")
for l in range(int(team1numberOfChances)):
  team1shots.append(st.number_input("Shot xG value?: ", key=f"Team1 chance {l}"))
  
            
team2name = st.text_input("Enter Team 2 Name", key="Team 2 Name")
team2numberOfChances = st.number_input(f"Enter the number of chances for {team2name}", key="Team 2 Chances")


for m in range(int(team2numberOfChances)):
  team2shots.append(st.number_input("Shot xG value?: ", key=f"Team2 chance {m}"))
    

team1wins = 0
draws = 0
team2wins = 0

for i in range(100000):
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

result = pd.DataFrame({f'{team1name} xPts' : [team1points/100000],
                       f'{team2name} xPts' : [team2points/100000],
                       f'{team1name} Win %' : [team1wins/1000],
                       f'{team2name} Win %' : [team2wins/1000],
                       'Draw %' : [draws/1000]})

st.write(result)


