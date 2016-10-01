import numpy as np
import matplotlib.pyplot as pplot
import os
import pandas as pd
from cassandra.cluster import Cluster

# Basically we're just copying what we did with the text file version

# First we get our Cassandra session

def setup():
    cluster = Cluster()
    session = cluster.connect('games')
    return session

# Cost function J

def J(X, y, theta):
    inn = np.power(((X * theta.T) - y), 2)
    return np.sum(inn) / (2 * len(X))

# TODO: Need to define a method for gradient descent
# TODO: Need to plot linear regression

# Method for getting dataframe

def get_data(session):
    query = 'SELECT budget, score FROM games_by_year ;'
    result = session.execute(query)
    datalist = [['Budget', 'Score']]
    for item in result:
        budget = item.budget
        score = item.score
        datalist.append([budget, score])
    headers = datalist.pop(0)
    data = pd.DataFrame(datalist, columns=headers)
    return data

# Make a scatter plot!

def scatter(data):
    r, k = pplot.subplots(figsize=(12,10))
    k.scatter(data.Budget, data.Score, label='Training Set')
    k.set_xlabel('Budget')
    k.set_ylabel('Score')
    pplot.show()

if __name__ == "__main__":
    session = setup()
    data = get_data(session)
    scatter(data)
