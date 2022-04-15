"""Module contain a example threading module."""
import time
import random
import datetime
from typing import List
from threading import Thread, RLock


class Account:
    """Class account allow to create bank account with balance. """
    def __init__(self, balance=0) -> None:
        self.balance = balance
        """RLock is a class using for reentrant lock objects."""
        self.lock = RLock()


transfer_lock = RLock()


def main():
    """Creating a list of accounts."""
    accounts = create_accounts()

    """Calculate sum of accounts balance"""
    total = sum(a.balance for a in accounts)
    print("Starting transfers...")

    """Validate if total bank accounts balance is equal total balance on accounts."""
    validate_bank(accounts, total)
    print("Starting transfers...")

    """Create accounts in different threads."""
    jobs = [
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
    ]

    t0 = datetime.datetime.now()

    """Start all threads"""
    [j.start() for j in jobs]

    """Wait till all threads finish work."""
    [j.join() for j in jobs]

    dt = datetime.datetime.now() - t0

    print(f"Transfers complete ({dt.total_seconds():,.2f}) sec")

    """Check if total bank accounts balance is equal total balance on accounts after work"""
    validate_bank(accounts, total)


def create_accounts() -> List[Account]:
    """
    Creating a list of accounts.
    :return:
        List[Account]: a list contain account objects.
    """
    return [
        Account(balance=5000),
        Account(balance=10000),
        Account(balance=7500),
        Account(balance=7000),
        Account(balance=6000),
        Account(balance=9000),
    ]


def validate_bank(accounts: List[Account], total: int, quiet=False) -> None:
    """Validate if total bank accounts balance is equal total balance on accounts.

    :param accounts: List[Account]
    :param total: int
    :param quiet: bool
    :return:
        None: print information about validation result.
    """
    # with transfer_lock:
    #     current = sum(a.balance for a in accounts)

    """acquire() - acquire a lock
    Reason for using sort on locked things is to be sure always
    taking things in the same order, or there's a good chance 
    for deadlock application. 
    """
    [a.lock.acquire() for a in sorted(accounts, key=lambda x: id(x))]

    current = sum(a.balance for a in accounts)

    """release() - release a lock"""
    [a.lock.release() for a in accounts]

    if current != total:
        print(f"ERROR: Inconsistent account balance: ${current}:, vs ${total:,}", flush=True)
    elif not quiet:
        print(f"All good: Consistent account balance: ${total:,}", flush=True)


def get_two_accounts(accounts: List[Account]):
    """Take two random and different accounts.
    :param
        accounts: List[Account]: a list contain account objects.
    :return:
        a1 : account object - instance Account class
        a2 : account object - instance Account class
    """
    a_1 = random.choice(accounts)
    a_2 = a_1
    while a_2 == a_1:
        a_2 = random.choice(accounts)
        a_2 = random.sample(accounts)
    return a_1, a_2


def do_transfer(from_account: Account, to_account: Account, amount: int):
    """Make a transfer between two accounts.

    :param
        from_account : account object - instance Account class
    :param
        to_account: account object - instance Account class
    :param
        amount: int: The amount of funds on the account
    :return:
        None: operations on the account are performed
    """
    if from_account.balance < amount:
        return
    with transfer_lock:
        from_account.balance -= amount
        time.sleep(.000)
        to_account.balance += amount


def do_bank_stuff(accounts: List[Account], total: int) -> None:
    """Take two accounts and

    :param accounts:
        List[Account]: a list contain account objects.
    :param total:
        int: sum of accounts balance
    :return:
        None: operations on the account are performed
    """
    for _ in range(1, 10_000):
        a_1, a_2 = get_two_accounts(accounts)
        amount = random.randint(500, 5000)
        do_transfer(a_1, a_2, amount)
        validate_bank(accounts, total, quiet=True)


if __name__ == '__main__':
    main()
