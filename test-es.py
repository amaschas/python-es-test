from elasticsearch_dsl import connections, Search
import os

# from memory_profiler import profile

ES_HOST = os.environ.get("ES_HOST", "")
JOBS_INDEX = os.environ.get("JOBS_INDEX", "")

connections.create_connection(hosts=[ES_HOST])

# @profile
def my_func():
    for x in range(1000):
        print(x)
    #     s = Search()
    #     s = s[:100]
    #     r = s.execute()
    # return r

my_func()