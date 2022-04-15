"""This module contain example of using multiCPU.
This example showed how tu use all CPU cores to work.
"""
import math
import datetime
import colorama
import multiprocessing


def main():
    """Do task using all CPU cores"""
    t0 = datetime.datetime.now()

    print(colorama.Fore.GREEN + f"Doing math on {multiprocessing.cpu_count():,} processors.")

    pool = multiprocessing.Pool()
    processor_count = multiprocessing.cpu_count()
    tasks = []
    for n in range(1, processor_count + 1):
        task = pool.apply_async(do_math, (30_000_000 * (n - 1) / processor_count,
                                          30_000_000 * n / processor_count))
        tasks.append(task)
    pool.close()
    pool.join()

    dt = datetime.datetime.now() - t0

    print(colorama.Fore.GREEN + f"Done in {dt.total_seconds():,.2f} sec.")
    print(colorama.Fore.GREEN + "Our results: ")

    for t in tasks:
        print(t.get())


def do_math(start=0, num=10):
    """
    Perform calculations on the given numbers.
    :param start: int
    :param num: int
    :return: int
    """
    pos = start
    k_sq = 1000 * 1000
    ave = 0

    while pos < num:
        pos += 1
        val = math.sqrt((pos - k_sq) * (pos - k_sq))
        ave += val / num

    return int(ave)


if __name__ == '__main__':
    main()
