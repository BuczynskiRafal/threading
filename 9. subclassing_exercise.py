import time
import threading


class OverrideThread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        super(OverrideThread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style

    def run(self, *args, **kwargs):
        print('Start threading')
        super(OverrideThread, self).run(*args, **kwargs)
        print('Thread has ended')


def sleeper(num, style):
    print(f"Sleap for {num} second as {style}.")
    time.sleep(num)


t = OverrideThread(number=3, style='blue', target=sleeper, args=[3, 'blue'])
t.start()
