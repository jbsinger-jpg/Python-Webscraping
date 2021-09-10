# pandas is a software library written for the Python programming language for data manipulation and analysis
# In particular, it offers data structures and operations for manipulating numerical tables and time series
# It is free software released under the three-clause BSD license
import pandas as pd
import numpy as np

# pyplot is a collection of functions that make matplotlib work like MATLAB
# Documentation Link: https://matplotlib.org/stable/api/pyplot_summary.html?highlight=pyplot
from matplotlib import pyplot as plt
# xCoords = [1, 2, 3]
# yCoords = [1, 4, 5]
# zCoords = [10, 5, 0]
#
# # connects points given in coords arrays into lines
# plt.plot(xCoords, yCoords, label= "This is the xy line")
# plt.plot(xCoords, zCoords, label= "This is the xz line")
#
# plt.title("Title for Data Visualization")
#
# plt.xlabel("Horizontal Data Label")
# plt.ylabel("Vertical Data Label")
#
# # legend shows what the plots represent (key for mapping)
# plt.legend()
#
# # generates visualization of plot
# plt.show()

# command used to generate data from CSV source instead of hard-coding array values
sample_data = pd.read_csv("SampleDataExample.csv")
# ------------------------------------------------------------
# Messing with values of CSV in Python
# ------------------------------------------------------------
# print(sample_data)
# print("\n")
# print("Individual columns")
# print(sample_data.column_a)
#
# print("\n")
# print("Individual column value")
# print(sample_data.column_a.iloc[1])
# ------------------------------------------------------------
# ------------------------------------------------------------
# plot() Documentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
# plt.plot(sample_data.column_a, sample_data.column_b, fmt='.--k', label="This is the AB line")
# plt.plot(sample_data.column_b, sample_data.column_c, fmt='x:b', label="This is the BC line")
# plt.legend()
#
# plt.title("Exported CSV")
# plt.xlabel("Column A Coordinates")
# plt.ylabel("Column B and C Coordinates")
# plt.show()
# ------------------------------------------------------------
# Bar Charts
# ------------------------------------------------------------
labels = ['Jellyfish', 'Squeaky Boots', 'Panty Raids']
values = [8, 2, 15]
plt.bar(labels, values)
plt.show()
# ------------------------------------------------------------
# ------------------------------------------------------------
