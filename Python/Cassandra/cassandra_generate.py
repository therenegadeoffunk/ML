#!/usr/bin/env python

from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
import random
import sys

if len(sys.argv) < 3:
    print "first argument is number of rows, second is host"
    exit(1)

num = int(sys.argv[1])

HOST = [sys.argv[2]]

words = open('words.txt').read().splitlines()

def setup():
    cluster = Cluster(HOST)
    session = cluster.connect('games')
    return session

def get_score(budget):
    if budget < 5.0:
        score = random.uniform(1, 7)
    else:
        score = random.uniform(6, 11) + budget/5.0
        if score > 10:
            score = random.uniform(8, 11)
    return score

def get_params():
    year = random.randint(1970, 2018)
    title = make_title()
    budget = random.uniform(1, 11)
    score = get_score(budget)
    return [ year, title, int(score), int(budget) ]

def make_title():
    title_length = random.uniform(1, 7)
    terms = []
    i = 0
    while i <= title_length:
        terms.append(random.choice(words))
        i += 1
    title = ' '.join(terms)
    return title

if __name__ == "__main__":
    session = setup()
    query = session.prepare('''INSERT INTO games_by_year ( year, name, score, budget ) VALUES ( ?, ?, ?, ? );''')
    a = 1
    batch = BatchStatement()
    while a <= num:
	params = get_params()
	batch.add(query, (params[0], params[1], params[2], params[3]))
        a += 1
    print "Executing batch query"
    session.execute(batch)
