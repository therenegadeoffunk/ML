#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

year_data_path = '~/Downloads/japan_trade/year_latest.csv'
country_data_path = '~/Downloads/japan_trade/country_eng.csv'
categories_data_path = '~/Downloads/japan_trade/hs2_eng.csv'

year_df = pd.read_csv(year_data_path)
country_df = pd.read_csv(country_data_path)
comb_df = pd.merge(year_df, country_df, on=['Country'])
usa_df = comb_df[comb_df['Country_name'] == 'United_States_of_America']
cat = pd.read_csv(categories_data_path)
usa_hs2 = usa_df[['Year', 'VY', 'hs2']].groupby(['hs2','Year'], as_index=False)
df = usa_hs2.aggregate(np.sum)
df = pd.merge(df, cat, on=['hs2'])
goods = df[df['VY'] >  0.15 * 1e10]
names = np.unique(goods['hs2_name'].values)

for name in names:
    d = df[df['hs2_name'] == name]
    plt.plot(d['Year'], d['VY'], label=name)

plt.legend(bbox_to_anchor=(1, 1), loc=2) 
plt.show()
