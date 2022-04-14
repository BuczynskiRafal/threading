"""Podstawy wielowątkowości"""
import threading


def sample_function():
    print('Start threading')


my_thread = threading.Thread(target=sample_function)

# aby rozpocząć należy wywołać start() na Thread
my_thread.start() #to ma printować 'Start threading' ponieważ sample_function zostało przekazane do target=

