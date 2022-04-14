"""Komunikacja między wątkami"""
from queue import Queue
from threading import Thread

"""
Aby bezpiecznie komunikować się między wątkami 
można użyć klasy Queue
"""


def data_computation():
    return "test_data"


def producer(output_queue):
    """Create a data producer"""
    while True:
        data = data_computation()

        output_queue.put(data)


def consumer(input_queue):
    """create a consumer"""
    while True:
        # retrieve data (blocking)
        data = input_queue.get()

        # do something with the data

        # indicate data has been consumed
        input_queue.task_done()


"""Tworzenie wątków producenta i konsumenta za pomocą wspólnej kolejki"""
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
