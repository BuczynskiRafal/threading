import datetime
import random
import time
from threading import Thread, RLock
from typing import List


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def __repr__(self):
        return f"Balance: ${self.balance}"


def main():
    accounts = create_accounts()
    total = sum(a.balance for a in accounts)

    validate_bank(accounts, total)
    print("Starting transfers...")

    jobs = [
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
    ]

    t0 = datetime.datetime.now()

    [j.start() for j in jobs]
    [j.join() for j in jobs]

    dt = datetime.datetime.now() - t0

    print(f"Transfers complete ({dt.total_seconds():,.2f}) sec")
    validate_bank(accounts, total)


def do_bank_stuff(accounts, total):
    for _ in range(1, 10_000):
        a1, a2 = get_two_accounts(accounts)
        amount = random.randint(1000, 5000)
        do_transfer(a1, a2, amount)
        validate_bank(accounts, total, quiet=True)


def do_transfer(from_account: Account, to_account: Account, amount: int):
    if from_account.balance < amount:
        return
    # Not so good:
    # transfer_lock.acquire()
    #
    # from_account.balance -= amount
    # time.sleep(.000)
    # to_account.balance += amount
    #
    # transfer_lock.release()

    # good!
    with transfer_lock:
        from_account.balance -= amount
        time.sleep(.000)
        to_account.balance += amount


def get_two_accounts(accounts):
    a1 = random.choice(accounts)
    a2 = a1
    while a2 == a1:
        a2 = random.choice(accounts)
    return a1, a2


def validate_bank(accounts: List[Account], total: int, quiet=False):
    with transfer_lock:
        current = sum(a.balance for a in accounts)

    if current != total:
        print(f"ERROR: Inconsistent account balance: ${current:,} vs {total:,}", flush=True)
    elif not quiet:
        print(f"All good: Consistent account balance: ${total:,}", flush=True)


transfer_lock = RLock()


def create_accounts() -> List[Account]:
    return [
        Account(balance=5000),
        Account(balance=10000),
        Account(balance=7500),
        Account(balance=7000),
        Account(balance=6000),
        Account(balance=9000),
    ]


if __name__ == '__main__':
    main()
