"""Dołączanie do wątku."""
import requests
from threading import Thread
from queue import Queue

q = Queue(maxsize=20)


def put_page_to_q(page_num):
    """get page by number page"""
    q.put(requests.get(f'http://some-website.com/page_{page_num}.html'))


def compile_page(q):
    """Waiting for all pages by full() method."""
    # magic function that needs all pages before being able to be executed
    if not q.full():
        raise ValueError
    else:
        print("Done compiling!")


threads = []
for page_num in range(20):
    """Create 20 threads for download 20 pages.
    All pages is downloading in parallel."""
    t = Thread(target=requests.get, args=(page_num,))
    t.start()
    threads.append(t)

"""
Next, join all threads to make sure all threads are done running before
we continue. join() is a blocking call (unless specified otherwise using
the kwarg blocking=False when calling join)
"""
for t in threads:
    t.join()

# Call compile_page() now, since all threads have completed
compile_page(q)
