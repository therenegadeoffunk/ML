#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt

data_path = 'training_set.csv'

df = pd.read_csv(data_path)

# Let's start really simple. Lets visualize using just education and age

reduced = df[['X3', 'X5', 'Y']].copy()
viz = reduced.iloc[1:]
viz = viz.head(n=500)
# Convert the strings to numerical type

viz.Y = pd.to_numeric(viz.Y, errors='coerce')
viz.X3 = pd.to_numeric(viz.X3, errors='coerce')
viz.X5 = pd.to_numeric(viz.X5, errors='coerce')

# Separate the positives from negatives (defaults / non-defaults)

pos = viz[viz['Y'].isin([1])]
neg = viz[viz['Y'].isin([0])]

# Make a scatter plot

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(pos['X5'], pos['X3'], s=50, c='b', marker='o', label='Defaulted')  
ax.scatter(neg['X5'], neg['X3'], s=50, c='r', marker='x', label='Not_Defaulted')  
ax.legend()  
ax.set_xlabel('Age')  
ax.set_ylabel('Education')
plt.show()

# Make a sigmoid function

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Make a logistic regression cost function

def cost(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    start = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    stop = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    return np.sum(start - stop) / len(X)

# Shape the X and y data and convert to np arrays

viz.insert(0, 'Ones', 1)
columns = viz.shape[1]
X = viz.iloc[:,0:columns-1]
y = viz.iloc[:,columns-1:columns]
X = np.array(X.values)
y = np.array(y.values)
theta = np.zeros(3)

# Function for computing gradient

def gradient(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    param = int(theta.ravel().shape[1])
    grad = np.zeros(param)

    err = sigmoid(X * theta.T) - y

    for i in range(param):
        val = np.multiply(err, X[:,i])
        grad[i] = np.sum(val) / len(X)

    return grad

out = opt.fmin_tnc(func=cost, x0=theta, fprime=gradient, args=(X, y))
final = cost(out[0], X, y)

print final
