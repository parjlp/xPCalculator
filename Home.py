import streamlit as st
import pandas as pd
import numpy as np
import random

st.set_page_config(layout="wide")
st.title("National League North Data")
st.subheader("Notes About The Data")
st.divider()
st.subheader("Expected Points Table / Justice Table")
st.text("""Expected Points (xPts) Table
An xPts table reorders the league standings based on how many points teams should have earned given the quality of chances they created and conceded — rather than actual results.

What it reveals

- Overperforming teams — actual points significantly higher than xPts, suggesting lucky results, late goals, or strong finishing
- Underperforming teams — actual points lower than xPts, suggesting bad luck, poor finishing, or weak goalkeeping
- Sustainable form — teams whose actual table mirrors their xPts table are performing consistently with their underlying quality

Key uses

- Predicting future performance — xPts is generally a better predictor of where a team will finish than their current actual points
- Identifying regression candidates — teams high in actual pts but low in xPts may drop off
- Transfer & scouting context — understanding if a team's success is built on solid foundations or variance
- Manager evaluation — separating tactical quality from luck

Limitations

- Heavily dependent on xG model quality — garbage in, garbage out
- Doesn't account for game management — a team may intentionally sit deep after going ahead, suppressing their own xG deliberately
- Penalties can distort xG totals significantly
- Ignores squad depth, injuries, and fixture difficulty
- Some teams consistently over or underperform xG due to player quality, meaning the model may structurally miss price them

The xPts table is best thought of as a form guide for the underlying game rather than a replacement for the actual standings — it answers the question "who has been playing well?" rather than "who has been winning?" 
""")
st.divider()
st.subheader("Expected Goals (xG)")
st.text("""xG is a statistical metric that measures the quality of a chance — specifically, the probability that a given chance will result in a goal, expressed as a value between 0 and 1.

Each shot is assigned an xG value based on historical data from thousands of similar shots. A value of 0.9 xG means shots from that situation result in a goal 90% of the time, while 0.05 xG means only 5% of the time.
Factors that influence xG

- Distance from goal — closer shots have higher xG
- Angle — central positions score more than wide angles
- Shot type — header vs. foot, which foot
- Assist type — through ball, cross, direct play
- Game state — open play vs. set piece vs. penalty
- Defensive pressure — whether the shooter was contested

What it's used for

- Evaluating attackers — is a player over/underperforming their xG?
- Evaluating goalkeepers — are they saving shots they "should" concede?
- Team performance — a team winning but with low xG may be getting lucky
- Predicting results — xG is a better predictor of future results than actual goals""")
st.divider()

st.subheader("Post Shot xG (PSxG)")
st.text("""PSxG is a refinement of xG that is measured after the shot is taken, incorporating additional information about the shot's placement and trajectory — not just the situation it came from.

How it differs from xG 
- xG is measured before/at moment of shot and takes in to account the quality of the chance.
- PSxG is measured after a shot is struck and takes in to account the quality of the actual shot.

What PSxG adds
Regular xG only knows where the shot came from. PSxG also knows:

- Where the ball is heading within the frame of the goal
- Height and placement — top corner vs. straight at keeper
- Power and trajectory — driven shot vs. weak effort

A shot from the edge of the box aimed at the top corner will have a much higher PSxG than the same shot aimed straight at the keeper, even though the pre-shot xG is identical.

Limitations

- Still doesn't fully account for keeper positioning before the shot
- Deflections and rebounds are hard to model accurately
- Requires more granular tracking data to compute, so less widely available

PSxG is essentially the bridge between chance quality and execution quality — it tells you not just where a shot came from, but how dangerous it truly was once struck.""")
st.divider()
