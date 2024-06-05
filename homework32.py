import threading

lock = threading.Lock()


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def plus(self, amount):
        for i in range(5):
            with lock:
                self.balance = self.balance + amount
                print(f"Deposited {amount}, new balance is {self.balance}")

    def minus(self, amount):
        for i in range(5):
            with lock:
                self.balance = self.balance - amount
                print(f"Withdrew  {amount}, new balance is {self.balance}")


bank_account = BankAccount(1000)

plus_threading = threading.Thread(bank_account.plus(100))
minus_threading = threading.Thread(bank_account.minus(150))

plus_threading.start()
minus_threading.start()

plus_threading.join()
minus_threading.join()