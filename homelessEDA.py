#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 14:11:56 2018

@author: michaelburak
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Exposing dataframe with pandas
df = pd.read_csv('2007-2016-Homelessnewss-USA.csv')

#Cleaning and prep

#Might drop these columns if only caring about the State
#df = df.drop(columns=['CoC Number', 'CoC Name'])

#Converting count to int type from str

df['Count'] = df['Count'].str.replace(',', '').astype(np.int64)

#Converting year to datetime and setting to years
df['Year'] = pd.to_datetime(df['Year'])

df['Year'] = df['Year'].dt.year

#Examine head of dataset 

df.head()

#Examine tail 

df.tail()

#List all measures 
df.Measures.unique()

#finding occurrences of homeless veterans 

Filter = df.Measures == "Homeless Veterans"

filDf = df[Filter] #2404 rows

#Chronically homeless individuals, seeing total occurrences of something tracked
#through whole data set as measure

Filter2 = df.Measures == "Chronically Homeless Individuals"

filDf2 = df[Filter2]

#First set of tracked values includes 12 measures per state per year, beginning with CHI measure
#then grows to 21 (+9)
#9 measures not included=
initialMeasuresSchema = df.iloc[0:11]
veteransMeasuresSchema = df.iloc[19145:19166]

#entire measures for first examination of veterans
#size 12 - 12 measurements
filDf2007 = df[(df["CoC Number"] == "AK-500") &  (df['Year'] == 2007)]
#jumps to size 21 - 21 measurements
filDf2011 = df[(df["CoC Number"] == "AK-500") &  (df['Year'] == 2011)]
#jumps to size 42- 42 measurements
filDf2015 = df[(df["CoC Number"] == "AK-500") &  (df['Year'] == 2015)]
