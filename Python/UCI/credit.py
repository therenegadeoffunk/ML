#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = 'training_set.csv'

df = pd.read_csv(data_path)

# Let's start really simple. Lets visualize using just education and age

reduced = df[['X3', 'X5', 'Y']].copy()
viz = reduced.iloc[1:]
viz = viz.head(n=50)
# Convert the strings to numerical type

viz.Y = pd.to_numeric(viz.Y, errors='coerce')
viz.X3 = pd.to_numeric(viz.X3, errors='coerce')
viz.X5 = pd.to_numeric(viz.X5, errors='coerce')

# Separate the positives from negatives (defaults / non-defaults)

pos = viz[viz['Y'].isin([1])]
neg = viz[viz['Y'].isin([0])]

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(pos['X5'], pos['X3'], s=50, c='b', marker='o', label='Defaulted')  
ax.scatter(neg['X5'], neg['X3'], s=50, c='r', marker='x', label='Not_Defaulted')  
ax.legend()  
ax.set_xlabel('Age')  
ax.set_ylabel('Education')
plt.show()
