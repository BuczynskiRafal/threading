"""Subclassing"""

import time
import threading


class OverrideThread(threading.Thread):
    def run(self):
        """Method representing the thread's activity.
        You may override the method in a subclass.
        The stantard run() mehod
        invokes the callable object passed to
        the object's constructor as
        the target argument, if any, with sequential and
        keyword arguments taken
        from the args and kwargs arguments, respectively.
        """
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a recycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs


class MyThread(threading.Thread):
    """Test overriding run method."""
    def run(self):
        print(f"{self.getName()} has started.")
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a recycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs
            print(f"{self.getName()} has finished.")


def slepper(n, name):
    print(f"{name}, start working.")
    time.sleep(n)

    print(f"{name}, finish working.")


for i in range(4):
    t = MyThread(target=slepper, name=f'thread_{i+1}', args=(10, f'thread_{i+1}'))
    t.start()
