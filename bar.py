import plotly.graph_objs as go

def calcolatore_netto(ral, verbose=False):

  imponibile = ral - (ral * 0.0919)

  if not isinstance(ral, int):
    raise Exception("RAL must be an integer")

  if ral < 0:
    raise Exception("RAL non può essere negativa")

  elif imponibile <= 5000:
    raise Exception("RAL è troppo bassa")

  elif imponibile > 5000 and imponibile <= 28000:
    irpef = imponibile * 0.23

  elif imponibile > 28000 and imponibile <= 50000:
    irpef = 6440 + (imponibile - 28000) * 0.35

  else:
    irpef = 14140 + (imponibile - 50000) * 0.43

  if verbose:

    print("Reddito annuale netto: ", imponibile - irpef)
    print("Reddito annuale mensile: ", (imponibile - irpef) / 12)

  # mancano detrazioni (tipo figli a carico, ma poca roba)

  return (imponibile - irpef) / 12


calcolatore_netto(60000)

import matplotlib.pyplot as plt
import numpy as np

#! pip install streamlit
import streamlit as st

x = np.arange(10000, 80000, 200)

y = [calcolatore_netto(int(i)) for i in x]

trace = go.Scatter(
    x = x,
    y = y,
    mode = 'lines+markers',  # Use lines and markers to show the points on the line
    name = 'sin(x)',
    hoverinfo = 'x+y'  # Customize hover text, this shows both x and y values
)

# Define the layout for the plot
layout = go.Layout(
    title = 'Quanto prendo di netto al mese con questa RAL?',
    xaxis = dict(title = 'RAL'),
    yaxis = dict(title = 'Netto mensile'),
    hovermode = 'closest'  # Highlight the closest point on hover
)

# Create a Figure and plot it
fig = go.Figure(data=[trace], layout=layout)
fig.show()

st.plotly_chart(fig)


