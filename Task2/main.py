#!/usr/bin/env python

import logging

log = logging.getLogger()
log.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

KEYSPACE = "mykeyspace"


def main():
    cluster = Cluster(['172.31.73.66'])
    session = cluster.connect()

    log.info("setting keyspace...")
    session.set_keyspace(KEYSPACE)

    log.info("creating table...")
    session.execute("""
        CREATE TABLE IF NOT EXISTS test (
            id int,
            PRIMARY KEY (id),
            name text
        )
        """)

    query = """
        INSERT INTO test (id, name)
        VALUES (%(key)s, %(a)s)
        """

    for i in range(1000000):
        log.info("inserting row %d" % i)
        session.execute(query, {'key':i, 'a':"a"})


main()
