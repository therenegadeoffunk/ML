#!/usr/bin/env python

from cassandra.cluster import Cluster
import random

words = open('words.txt').read().splitlines()

def setup():
    cluster = Cluster()
    session = cluster.connect('games')
    return session

def get_score(budget):
    if budget < 25:
        score = random.randrange(10, 101)
    elif budget <= 50:
        score = random.randrange(25, 101)
    elif budget <= 75:
        score = random.randrange (45, 101)
    else:
        score = random.randrange (60, 101)
    return score
def get_params():
    title = make_title()
    budget = random.randrange(1, 101)
    score = get_score(budget)
    return [ title, score, budget ]

def make_title():
    title_length = random.randrange(1, 7)
    terms = []
    i = 0
    while i <= title_length:
        terms.append(random.choice(words))
        i += 1
    title = ' '.join(terms)
    return title

def generate_data(session):
    params = get_params()
    query = '''INSERT INTO game_by_name ( name, score, budget )
            VALUES ( %s, %s, %s );'''
    session.execute(query, (params[0], params[1], params[2]))

if __name__ == "__main__":
    session = setup()
    generate_data(session)
