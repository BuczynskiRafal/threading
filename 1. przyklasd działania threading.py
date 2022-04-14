import time
from threading import Thread


def show_time(name, delay, repeat):
    print(name, 'start working.')
    for _ in range(repeat):
        time.sleep(delay)
        print(name, ' ', str(time.ctime(time.time())))
    print(name, 'end working.')


threads = []
for i in range(4):
    threads.append(Thread(target=show_time, args=('Timer' + str(i + 1), i+1, (i+1) ** 2)))


for thread in threads:
    thread.start()


