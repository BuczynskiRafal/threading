import time
import threading


def main():
    """Create threads"""
    threads = [
        threading.Thread(target=greeter, args=("Michael", 10), daemon=True),
        threading.Thread(target=greeter, args=("Sarah", 5), daemon=True),
        threading.Thread(target=greeter, args=("Zoe", 2), daemon=True),
        threading.Thread(target=greeter, args=("Mark", 11), daemon=True),
    ]
    """Start each thread"""
    [t.start() for t in threads]

    print("This is other work.")

    """Wait till all threads finish work"""
    [t.join(timeout=1) for t in threads]

    print('Done')


def greeter(name: str, times: int):
    for n in range(times):
        print(f"{n} thread_{name}")
        time.sleep(1)


if __name__=='__main__':
    main()
