import threading


class OverrideThread(threading.Thread):
    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func
        self.args = args

    def run(self):
        print(f"thread_{self.number} has started.\n")
        self.func(*self.args)
        print(f"thread_{self.number} has finished.\n")


def double(number, cycles):
    for cycle in range(cycles):
        number += number
        print(number)


thread_list = []
for i in range(1, 4):
    t = OverrideThread(number=i + 1, func=double, args=[i, 2])
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()

