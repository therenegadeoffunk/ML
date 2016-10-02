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

# Gradient descent method

def gradient_descent(X, y, theta, a, i):
    cost = np.zeros(i)
    ini = np.matrix(np.zeros(theta.shape))
    d = int(theta.ravel().shape[1])
    for val in range(i):
        e = (X * theta.T) - y
        for c in range(d):
            k = np.multiply(e, X[:,c])
            ini[0,c] = theta[0,c] - ((a / len(X)) * np.sum(k))
        theta = ini
        cost[val] = J(X, y, theta)
    return theta, cost

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
    # Add our ones column
    data.insert(0, 'Ones', 1)
    return data

def graph_it(f, data):
    r, k = pplot.subplots(figsize=(12,10))
    k.scatter(data.Budget, data.Score, label='Training Set')
    l = np.linspace(1, 11, 11)
    b = f[0, 0] + (f[0, 1] * l)
    k.plot(l, b, 'r', label='Prediction')
    k.set_title('Predicted Score')
    k.set_xlabel('Budget')
    k.set_ylabel('Score')
    pplot.show()

if __name__ == "__main__":
    session = setup()
    data = get_data(session)
    X = np.matrix(data.iloc[:,0:2].values)
    y = np.matrix(data.iloc[:,2:3].values)
    theta = np.matrix(np.array([0,0]))
    f, j = gradient_descent(X, y, theta, a=.01, i=200)
    graph_it(f, data)
