# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:13:32 2023

@author: Taylor Sprang
"""
import numpy as np
import pandas as pd
import matplotlib as mpl 
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define method to read in the data files of snowfall info in the 6 cities
def read_file(file):
    table = pd.read_csv(file)
    table['DATE'] = pd.to_datetime(table['DATE'])
    return table

# Define a method extracting all warm ENSO midwinters between 1950-1995 from the original Pandas frame
# Midwinter is between Dec 1st and before (but not including) March 1st
# After exrtacting these values, sum the total midwinter snowfall for each year
def warm_ENSO(table):
    warm = table.loc[((table['DATE'] >= '1951-12-01') & (table['DATE'] < '1952-03-01'))]
    sum_1 = (warm['SNOW'].sum()) / 10
    warm = table.loc[((table['DATE'] >= '1957-12-01') & (table['DATE'] < '1958-03-01'))]
    sum_2 = (warm['SNOW'].sum()) / 10
    warm = table.loc[((table['DATE'] >= '1963-12-01') & (table['DATE'] < '1964-03-01'))]
    sum_3 = (warm['SNOW'].sum()) / 10
    warm = table.loc[((table['DATE'] >= '1965-12-01') & (table['DATE'] < '1966-03-01'))]
    sum_4 = (warm['SNOW'].sum()) / 10
    warm = table.loc[((table['DATE'] >= '1969-12-01') & (table['DATE'] < '1970-03-01'))]
    sum_5 = (warm['SNOW'].sum()) / 10
    warm = table.loc[((table['DATE'] >= '1972-12-01') & (table['DATE'] < '1973-03-01'))]
    sum_6 = (warm['SNOW'].sum()) / 10
    warm = table.loc[((table['DATE'] >= '1976-12-01') & (table['DATE'] < '1977-03-01'))]
    sum_7 = (warm['SNOW'].sum()) / 10
    warm = table.loc[((table['DATE'] >= '1982-12-01') & (table['DATE'] < '1983-03-01'))]
    sum_8 = (warm['SNOW'].sum()) / 10
    warm = table.loc[((table['DATE'] >= '1986-12-01') & (table['DATE'] < '1987-03-01'))]
    sum_9 = (warm['SNOW'].sum()) / 10
    warm = table.loc[((table['DATE'] >= '1987-12-01') & (table['DATE'] < '1988-03-01'))]
    sum_10 = (warm['SNOW'].sum()) / 10
    warm = table.loc[((table['DATE'] >= '1991-12-01') & (table['DATE'] < '1992-03-01'))]
    sum_11 = (warm['SNOW'].sum()) / 10
    data = {'Warm': [sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7, sum_8, sum_9, sum_10, sum_11]}
    Warm_Table = pd.DataFrame(data)
    # Return a table with the yearly midwinter snowfall totals
    return Warm_Table

# Define a method extracting all cold ENSO midwinters between 1950-1995 from the original Pandas frame
# Midwinter is between Dec 1st and before (but not including) March 1st
# After exrtacting these values, sum the total midwinter snowfall for each year
def cold_ENSO(table):
    cold = table.loc[((table['DATE'] >= '1954-12-01') & (table['DATE'] < '1955-03-01'))]
    sum_1 = (cold['SNOW'].sum()) / 10
    cold = table.loc[((table['DATE'] >= '1955-12-01') & (table['DATE'] < '1956-03-01'))]
    sum_2 = (cold['SNOW'].sum()) / 10
    cold = table.loc[((table['DATE'] >= '1956-12-01') & (table['DATE'] < '1957-03-01'))]
    sum_3 = (cold['SNOW'].sum()) / 10
    cold = table.loc[((table['DATE'] >= '1964-12-01') & (table['DATE'] < '1965-03-01'))]
    sum_4 = (cold['SNOW'].sum()) / 10
    cold = table.loc[((table['DATE'] >= '1967-12-01') & (table['DATE'] < '1968-03-01'))]
    sum_5 = (cold['SNOW'].sum()) / 10
    cold = table.loc[((table['DATE'] >= '1970-12-01') & (table['DATE'] < '1971-03-01'))]
    sum_6 = (cold['SNOW'].sum()) / 10
    cold = table.loc[((table['DATE'] >= '1971-12-01') & (table['DATE'] < '1972-03-01'))]
    sum_7 = (cold['SNOW'].sum()) / 10
    cold = table.loc[((table['DATE'] >= '1973-12-01') & (table['DATE'] < '1974-03-01'))]
    sum_8 = (cold['SNOW'].sum()) / 10
    cold = table.loc[((table['DATE'] >= '1975-12-01') & (table['DATE'] < '1976-03-01'))]
    sum_9 = (cold['SNOW'].sum()) / 10
    cold = table.loc[((table['DATE'] >= '1988-12-01') & (table['DATE'] < '1989-03-01'))]
    sum_10 = (cold['SNOW'].sum()) / 10
    data = {'Cold': [sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7, sum_8, sum_9, sum_10]}
    Cold_Table = pd.DataFrame(data)
    # Return a table with the yearly midwinter snowfall totals
    return Cold_Table

# Define a method extracting all neutral ENSO midwinters between 1950-1995 from the original Pandas frame
# Midwinter is between Dec 1st and before (but not including) March 1st
# After exrtacting these values, sum the total midwinter snowfall for each year
def neutral_ENSO(table):
    n = table.loc[((table['DATE'] >= '1950-12-01') & (table['DATE'] < '1951-03-01'))]
    sum_1 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1952-12-01') & (table['DATE'] < '1953-03-01'))]
    sum_2 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1953-12-01') & (table['DATE'] < '1954-03-01'))]
    sum_3 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1958-12-01') & (table['DATE'] < '1959-03-01'))]
    sum_4 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1959-12-01') & (table['DATE'] < '1960-03-01'))]
    sum_5 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1960-12-01') & (table['DATE'] < '1961-03-01'))]
    sum_6 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1961-12-01') & (table['DATE'] < '1962-03-01'))]
    sum_7 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1962-12-01') & (table['DATE'] < '1963-03-01'))]
    sum_8 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1966-12-01') & (table['DATE'] < '1967-03-01'))]
    sum_9 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1968-12-01') & (table['DATE'] < '1969-03-01'))]
    sum_10 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1974-12-01') & (table['DATE'] < '1975-03-01'))]
    sum_11 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1977-12-01') & (table['DATE'] < '1978-03-01'))]
    sum_12 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1978-12-01') & (table['DATE'] < '1979-03-01'))]
    sum_13 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1979-12-01') & (table['DATE'] < '1980-03-01'))]
    sum_14 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1980-12-01') & (table['DATE'] < '1981-03-01'))]
    sum_15 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1981-12-01') & (table['DATE'] < '1982-03-01'))]
    sum_16 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1982-12-01') & (table['DATE'] < '1983-03-01'))]
    sum_17 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1984-12-01') & (table['DATE'] < '1985-03-01'))]
    sum_18 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1985-12-01') & (table['DATE'] < '1986-03-01'))]
    sum_19 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1989-12-01') & (table['DATE'] < '1990-03-01'))]
    sum_20 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1990-12-01') & (table['DATE'] < '1991-03-01'))]
    sum_21 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1992-12-01') & (table['DATE'] < '1993-03-01'))]
    sum_22 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1993-12-01') & (table['DATE'] < '1994-03-01'))]
    sum_23 = (n['SNOW'].sum()) / 10
    n = table.loc[((table['DATE'] >= '1994-12-01') & (table['DATE'] < '1995-03-01'))]
    sum_24 = (n['SNOW'].sum()) / 10
    data = {'Neutral': [sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7, sum_8, sum_9, sum_10, 
                         sum_11, sum_12, sum_13, sum_14, sum_15, sum_16, sum_17, sum_18, sum_19, 
                         sum_20, sum_21, sum_22, sum_23, sum_24]}
    Neutral_Table = pd.DataFrame(data)
    # Return a table with the yearly midwinter snowfall totals
    return Neutral_Table

# Read in snowfall info for each city by calling read_file
Bellingham = read_file(".\Bellingham.csv")
Olympia = read_file(".\Olympia.csv")
Seattle = read_file(".\Seattle.csv")
Yakima = read_file(".\Yakima.csv")
Portland = read_file(".\Portland.csv")
Pendleton = read_file(".\Pendleton.csv")

# Create dataframes with yearly warm phase ENSO snowfall totals for each city
Warm_Bellingham = warm_ENSO(Bellingham)
Warm_Olympia = warm_ENSO(Olympia)
Warm_Seattle = warm_ENSO(Seattle)
Warm_Yakima = warm_ENSO(Yakima)
Warm_Portland = warm_ENSO(Portland)
Warm_Pendleton = warm_ENSO(Pendleton)

# Create dataframes with yearly cold phase ENSO snowfall totals for each city
Cold_Bellingham = cold_ENSO(Bellingham)
Cold_Olympia = cold_ENSO(Olympia)
Cold_Seattle = cold_ENSO(Seattle)
Cold_Yakima = cold_ENSO(Yakima)
Cold_Portland = cold_ENSO(Portland)
Cold_Pendleton = cold_ENSO(Pendleton)

# Create dataframes with yearly neutral phase ENSO snowfall totals for each city
N_Bellingham = neutral_ENSO(Bellingham)
N_Olympia = neutral_ENSO(Olympia)
N_Seattle = neutral_ENSO(Seattle)
N_Yakima = neutral_ENSO(Yakima)
N_Portland = neutral_ENSO(Portland)
N_Pendleton = neutral_ENSO(Pendleton)

# Prep figure creation; set all colors to black and font size to 12
medianprops=dict(color='black')
plt.rcParams.update({'font.size' : 12})

# Create the figure with 6 subplots (1 for each city)
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2,3)
# Create the first subplot: 3 boxplots included per subplot (1 for warm, cold, and neutral ENSO snowfall totals)
# This subplot is for Bellingham warm, cold, and neutral midwinter snowfall totals
bp1 = ax1.boxplot(Warm_Bellingham, whis=(0,100), positions = [1], labels=['Warm'], medianprops=medianprops)
bp12 = ax1.boxplot(N_Bellingham, whis=(0,100), positions = [2], labels=['Neut'], medianprops=medianprops)
bp13 = ax1.boxplot(Cold_Bellingham, whis=(0,100), positions = [3], labels=['Cold'], medianprops=medianprops)
ax1.set_title('Bellingham, WA', fontsize=18)
ax1.set_ylim([0, 100])
ax1.set_ylabel('Snowfall (cm)', fontsize=18)
ax1.yaxis.set_ticks_position('both')
ax1.xaxis.set_ticks_position('both')
# Create the 2nd subplot: 3 boxplots included per subplot (1 for warm, cold, and neutral ENSO snowfall totals)
# This subplot is for Seattle warm, cold, and neutral midwinter snowfall totals
bp1 = ax2.boxplot(Warm_Seattle, whis=(0,100), positions = [1], labels=['Warm'], medianprops=medianprops)
bp12 = ax2.boxplot(N_Seattle, whis=(0,100), positions = [2], labels=['Neut'], medianprops=medianprops)
bp13 = ax2.boxplot(Cold_Seattle, whis=(0,100), positions = [3], labels=['Cold'], medianprops=medianprops)
ax2.set_title('Seattle-Tacoma, WA', fontsize=18)
ax2.set_ylim([0, 200])
ax2.set_ylabel('Snowfall (cm)', fontsize=18)
ax2.yaxis.set_ticks_position('both')
ax2.xaxis.set_ticks_position('both')
# Create the 3rd subplot: 3 boxplots included per subplot (1 for warm, cold, and neutral ENSO snowfall totals)
# This subplot is for Olympia warm, cold, and neutral midwinter snowfall totals
bp1 = ax3.boxplot(Warm_Olympia, whis=(0,100), positions = [1], labels=['Warm'], medianprops=medianprops)
bp12 = ax3.boxplot(N_Olympia, whis=(0,100), positions = [2], labels=['Neut'], medianprops=medianprops)
bp13 = ax3.boxplot(Cold_Olympia, whis=(0,100), positions = [3], labels=['Cold'], medianprops=medianprops)
ax3.set_title('Olympia, WA', fontsize=18)
ax3.set_ylim([0, 250])
ax3.set_ylabel('Snowfall (cm)', fontsize=18)
ax3.yaxis.set_ticks_position('both')
ax3.xaxis.set_ticks_position('both')
# Create the 4th subplot: 3 boxplots included per subplot (1 for warm, cold, and neutral ENSO snowfall totals)
# This subplot is for Yakima warm, cold, and neutral midwinter snowfall totals
bp1 = ax4.boxplot(Warm_Yakima, whis=(0,100), positions = [1], labels=['Warm'], medianprops=medianprops)
bp12 = ax4.boxplot(N_Yakima, whis=(0,100), positions = [2], labels=['Neut'], medianprops=medianprops)
bp13 = ax4.boxplot(Cold_Yakima, whis=(0,100), positions = [3], labels=['Cold'], medianprops=medianprops)
ax4.set_title('Yakima, WA', fontsize=18)
ax4.set_ylim([0, 150])
ax4.set_ylabel('Snowfall (cm)', fontsize=18)
ax4.yaxis.set_ticks_position('both')
ax4.xaxis.set_ticks_position('both')
# Create the 5th subplot: 3 boxplots included per subplot (1 for warm, cold, and neutral ENSO snowfall totals)
# This subplot is for Portland warm, cold, and neutral midwinter snowfall totals
bp1 = ax5.boxplot(Warm_Portland, whis=(0,100), positions = [1], labels=['Warm'], medianprops=medianprops)
bp12 = ax5.boxplot(N_Portland, whis=(0,100), positions = [2], labels=['Neut'], medianprops=medianprops)
bp13 = ax5.boxplot(Cold_Portland, whis=(0,100), positions = [3], labels=['Cold'], medianprops=medianprops)
ax5.set_title('Portland, OR', fontsize=18)
ax5.set_ylim([0, 100])
ax5.set_ylabel('Snowfall (cm)', fontsize=18)
ax5.yaxis.set_ticks_position('both')
ax5.xaxis.set_ticks_position('both')
# Create the last subplot: 3 boxplots included per subplot (1 for warm, cold, and neutral ENSO snowfall totals)
# This subplot is for Pendleton warm, cold, and neutral midwinter snowfall totals
bp1 = ax6.boxplot(Warm_Pendleton, whis=(0,100), positions = [1], labels=['Warm'], medianprops=medianprops)
bp12 = ax6.boxplot(N_Pendleton, whis=(0,100), positions = [2], labels=['Neut'], medianprops=medianprops)
bp13 = ax6.boxplot(Cold_Pendleton, whis=(0,100), positions = [3], labels=['Cold'], medianprops=medianprops)
ax6.set_title('Pendleton, OR', fontsize=18)
ax6.set_ylim([0, 140])
ax6.set_ylabel('Snowfall (cm)', fontsize=18)
ax6.yaxis.set_ticks_position('both')
ax6.xaxis.set_ticks_position('both')

# Set figure size, then save it
fig.set_size_inches(18.5, 10.5)
plt.show()
fig.savefig(".\Box_Plot")
