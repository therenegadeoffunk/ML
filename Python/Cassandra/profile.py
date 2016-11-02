#!/usr/bin/env python

from cassandra.cluster import Cluster
import sys
import csv

keyspace_name = sys.argv[1]

def setup():
    cluster = Cluster()
    session = cluster.connect()
    return session

def profile_tables(session, keyspace_name):
    query = '''SELECT * FROM system_schema.tables \
            WHERE keyspace_name=%s;'''
    result = session.execute(query, (keyspace_name,))
    dicts = []
    for a in result:
        a = a.__dict__
        dicts.append(a)
    for d in dicts:       
        name = d['table_name'] + ".csv"
        with open(name, 'wb') as f:
            w = csv.writer(f)
            w.writerows(d.items())
        f.close()

# This method for profiling an individual table may be useful later    
def profile_table(session, keyspace_name, table):
    query = '''SELECT * FROM system_schema.tables WHERE \
            keyspace_name=%s AND table_name=%s;'''
    result = session.execute(query, (keyspace_name, table))
    print result[0]

if __name__ == "__main__":
    session = setup()
    profile_tables(session, keyspace_name)
