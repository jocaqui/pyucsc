from ucsc import create_session, tables
from ucsc.model import *

def test_table_query():
    print tables.__dict__
    c = tables.knownGene.count().execute().scalar()
    print c
    assert c == 77614L