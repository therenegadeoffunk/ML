#!/usr/bin/env python

# Note: This script is for testing against a local cassandra node

# It will behave weirdly if run against a remote endpoint

# TODO: Fix the above...

from cassandra.cluster import Cluster
import random
import sys

if len(sys.argv) < 2:
    print "Gonna need a number of rows to insert chief"
    exit(1)

num = int(sys.argv[1])

words = open('words.txt').read().splitlines()

def setup():
    cluster = Cluster()
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
    title = make_title()
    budget = random.uniform(1, 11)
    score = get_score(budget)
    return [ title, int(score), int(budget) ]

def make_title():
    title_length = random.uniform(1, 7)
    terms = []
    i = 0
    while i <= title_length:
        terms.append(random.choice(words))
        i += 1
    title = ' '.join(terms)
    return title

def generate_data(session):
    params = get_params()
    query = '''INSERT INTO games_by_year ( year, name, score, budget )
            VALUES ( 2015, %s, %s, %s );'''
    session.execute(query, (params[0], params[1], params[2]))

if __name__ == "__main__":
    session = setup()
    a = 1
    while a <= num:
        generate_data(session)
        a += 1
