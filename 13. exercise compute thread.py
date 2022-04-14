import math
import datetime
import multiprocessing
from threading import Thread

import colorama


def main():
    t0 = datetime.datetime.now()

    # do_math(num=30000000)
    print(f"Doing math on {multiprocessing.cpu_count():,} processors.")

    processor_count = multiprocessing.cpu_count()
    threads = []
    for n in range(1, processor_count + 1):
        threads.append(Thread(target=do_math,
                              args=(30_000_000 * (n-1) / processor_count,
                                    30_000_000 * n / processor_count),
                              daemon=True)
                       )
    [t.start() for t in threads]
    [t.join() for t in threads]

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.GREEN + f"Done in {dt.total_seconds():,.2f} sec.")


def do_math(start=0, num=10):
    print(colorama.Fore.BLUE + f"Starting do_math")
    pos = start
    k_sq = 1000 * 1000
    while pos < num:
        pos += 1
        math.sqrt((pos - k_sq) * (pos - k_sq))
    print(colorama.Fore.CYAN + f"do_math has finished")


if __name__ == '__main__':
    main()
