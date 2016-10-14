import numpy as np
import matplotlib.pyplot as pplot
import os
import pandas as pd

# Some starter code just to get a scatter plot of the data

data = pd.read_csv(os.getcwd()+'/ex1data1.txt', header=None, names=['Population', 'Profit'])
r, k = pplot.subplots(figsize=(12,10))
k.scatter(data.Population, data.Profit, label='Training Set')
pplot.show()
