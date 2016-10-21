#!/usr/bin/env/python

import numpy as np
import pandas as pd

train_path = '~/Downloads/integer_recognition_competition/train.csv'
train_df = pd.read_csv(train_path)
Y = train_df['label']
X = train_df.ix[:,1:]

print Y[1]
