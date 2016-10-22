#!/usr/bin/env python

from cassandra.cluster import Cluster
import sys

keyspace_name = sys.argv[1]

def setup():
    cluster = Cluster()
    session = cluster.connect()
    return session

def get_table_names(session, keyspace_name):
    query = '''SELECT table_name FROM system_schema.tables \
            WHERE keyspace_name=%s;'''
    result = session.execute(query, (keyspace_name,))
    name_list = []
    for item in result:
        name_list.append(item.table_name)
    return name_list

def profile_tables(session, keyspace_name):
    name_list = get_table_names(session, keyspace_name)
    for name in name_list:
        profile_table(session, keyspace_name, name)

def profile_table(session, keyspace_name, table):
    query = '''SELECT * FROM system_schema.tables WHERE \
            keyspace_name=%s AND table_name=%s;'''
    result = session.execute(query, (keyspace_name, table))
    # Just printing for now. We'll do cooler things later
    print result[0]

if __name__ == "__main__":
    session = setup()
    profile_tables(session, keyspace_name)
