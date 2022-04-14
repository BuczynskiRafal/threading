"""Utwórz niestandardową klasę wątków"""
import time
from threading import Thread


class Sleepy(Thread):
    """
    Za pomocą klasy threading.Thread możemy podklasować nową niestandardową
    klasę Thread. musimy zastąpić metodę run w podklasie.
    """
    def run(self):
        time.sleep(2)
        print('Threading')

# if __name__ == '__main__':
#     t = Sleepy()
#     t.start()   # start method automatic call Thread class run method.
#     # print 'The main program continues to run in foreground.'
#     t.join()
#     print("The main program continues to run in the foreground.")


if __name__ == '__main__':
    threads = []
    for i in range(10):
        t = Sleepy()
        t.start()   # start method automatic call Thread class run method.
    # print 'The main program continues to run in foreground.'
    for _ in threads:
        t.join()
    print("The main program continues to run in the foreground.")

