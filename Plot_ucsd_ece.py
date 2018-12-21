# -*- coding: utf-8 -*-
#
# Ploting graphs using matplotlib and plotly
# Trend of the ECE department at UCSD
#
# Nov 22, 2018 by Renjie Zhu
#

"""ucsd_ece_plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cwTUqhwisEjNnQHy8TXDVHDeiD48ppBR
"""

# %matplotlib inline

"""# Question:

How has the ECE departement evolved during the past 18 years.

What new words emerged? (Machine Learning)

What words died? (magnetic recording, field effect)

What remains its importance? (signal processing, integrated circuit)

# Use Matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
import os

# !pip install xlrd

ucsd_ece = pd.read_excel(os.path.join('processed_data','ucsd_ece.xlsx'))

field = ucsd_ece.loc['field effect']
magnetic = ucsd_ece.loc['magnetic recording']
signal = ucsd_ece.loc['signal processing']
integrated = ucsd_ece.loc['integrated circuit']
machine = ucsd_ece.loc['machine learning']

years = np.linspace(2001,2018, 18, dtype=np.int64)

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.plot(years, field,'bo-')
ax.plot(years, magnetic,'go-')
ax.plot(years, signal,'ro-')
ax.plot(years, integrated,'yo-')
ax.plot(years, machine, 'ko-')
ax.set_ylabel('word freqency')
ax.set_xlabel('catalog year')
ax.set_title('UCSD ECE')
ax.legend()

fig.savefig(os.path.join('processed_data','all.jpg'))

fig2, ax2 = plt.subplots()
ax2.xaxis.set_major_locator(MaxNLocator(integer=True))
ax2.plot(years, field,'bo-')
ax2.plot(years, magnetic,'go-')
# ax.plot(years, signal,'ro-')
# ax.plot(years, integrated,'yo-')
# ax.plot(years, machine, 'ko-')
ax2.set_ylabel('word freqency')
ax2.set_xlabel('catalog year')
ax2.set_title('UCSD ECE')
ax2.legend()

fig2.savefig(os.path.join('processed_data','drop.jpg'))

fig3, ax3 = plt.subplots()
ax3.xaxis.set_major_locator(MaxNLocator(integer=True))
# ax3.plot(years, field,'bo-')
# ax3.plot(years, magnetic,'go-')
# ax3.plot(years, signal,'ro-')
# ax3.plot(years, integrated,'yo-')
ax3.plot(years, machine, 'ko-')
ax3.set_ylabel('word freqency')
ax3.set_xlabel('catalog year')
ax3.set_title('UCSD ECE')
ax3.legend()

fig3.savefig(os.path.join('processed_data','incre.jpg'))

fig4, ax4 = plt.subplots()
ax4.xaxis.set_major_locator(MaxNLocator(integer=True))
# ax4.plot(years, field,'bo-')
# ax4.plot(years, magnetic,'go-')
ax4.plot(years, signal,'ro-')
ax4.plot(years, integrated,'yo-')
# ax4.plot(years, machine, 'ko-')
ax4.set_ylabel('word freqency')
ax4.set_xlabel('catalog year')
ax4.set_title('UCSD ECE')
ax4.legend()

fig4.savefig(os.path.join('processed_data','flat.jpg'))

"""# Additional Question:

Connection to the industry data.
"""
"""
# Using plotly

Using plotly may be another solution if visuals are more important.
"""

field_array = field.get_values()
magnetic_array = magnetic.get_values()
signal_array = signal.get_values()
integrated_array = signal.get_values()
machine_array = machine.get_values()

import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('johnsonlumia','Di2ueeMg6PKBCmw57HKn')

ma_tr = go.Scatter(
    x = years,
    y = machine_array,
    name = 'machine learning',
    mode = 'lines+markers',
)

fi_tr = go.Scatter(
    x = years,
    y = field_array,
    name = 'field effect',
    mode = 'lines+markers',
)

mg_tr = go.Scatter(
    x = years,
    y = magnetic_array,
    name = 'magnetic recording',
    mode = 'lines+markers',
)

si_tr = go.Scatter(
    x = years,
    y = signal_array,
    name = 'signal processing',
    mode = 'lines+markers',
)

in_tr = go.Scatter(
    x = years,
    y = integrated_array,
    name = 'integrated circuits',
    mode = 'lines+markers',
)

data = [ma_tr, fi_tr, mg_tr, si_tr, in_tr]
layout = {
  "title": "UCSD ECE Departmental Evolution", 
  "xaxis": {
    "autorange": False, 
    "range": [2000, 2019], 
    "title": "Year of Catalog", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": False, 
    "range": [-0.5, 15], 
    "title": "Occurance", 
    "type": "linear"
  }
}
fig = go.Figure(data=data, layout=layout)
py.plot(fig)
