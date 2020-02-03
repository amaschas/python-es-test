from elasticsearch_dsl import connections, Search

from memory_profiler import profile

connections.create_connection()

@profile
def my_func():
    for x in range(1000):
        s = Search()
        s = s[:100]
        r = s.execute()
    return r

my_func()