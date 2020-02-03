from elasticsearch_dsl import connections, Search
# import logging
import os

from memory_profiler import profile

ES_HOST = os.environ.get("ES_HOST", "")
JOBS_INDEX = os.environ.get("JOBS_INDEX", "")

connections.create_connection(
    hosts=[ES_HOST],
    use_ssl=False,
    verify_certs=False
)

# es_logger = logging.getLogger('elasticsearch')
# es_logger.setLevel(logging.INFO)

@profile
def my_func():
    for x in range(1000):
        s = Search(index=JOBS_INDEX)
        s = s[:10]
        r = s.execute()
    return r

for x in range(3):
    my_func()
