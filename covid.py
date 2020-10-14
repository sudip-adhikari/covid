# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:25:12 2020

@author: Admin
Here the administrative boundaries of Nepal are used.
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

covid_cases = pd.read_csv('H:\mausam\python  ex\covid-19\csv data\province\sep17_active.csv')


covid_cases = covid_cases[['Province','Active']]
print(covid_cases)

map_nep = gpd.read_file(r'H:\mausam\python  ex\covid-19\nepal administ\Province of Nepal\Nepal_Province.shp')

map_nep = map_nep[['STATE_CODE','geometry']]
map_nep.rename(columns={'STATE_CODE':'Province'}, inplace=True)
map_nep.to_crs(epsg=32645, inplace=True)

'''
for index, row in map_nep['Province'].iteritems():
    if row in covid_cases['Province'].tolist():
        pass
    else:
        print(row)
'''

map_nep = map_nep.merge(covid_cases, on='Province')

print(map_nep)
#title='Province Level Distribution of Corona Cases: Data of September 15, 2020 '
map_nep.plot(column='Active',figsize=(10,5),cmap='Spectral',legend=True)

