#!/usr/bin/env python

from cassandra.cluster import Cluster

cluster = Cluster()

session = cluster.connect('games')

output = session.execute('SELECT * FROM game_by_name')

print  output[0]
