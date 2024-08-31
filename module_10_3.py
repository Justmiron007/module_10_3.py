import random
import time
import threading


class Bank:
    def __init__(self):
        self.cash = None
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        with self.lock:
            for i in range(100):
                self.cash = random.randint(50, 500)
                self.balance += self.cash
                print(f'Пополнение: {self.cash}. Баланс: {self.balance}')
                time.sleep(0.001)

    def take(self):
        for i in range(100):
            self.cash = random.randint(50, 500)
            print(f'Запрос на {self.cash}')
            if self.cash <= self.balance or self.cash == self.balance:
                self.balance -= self.cash
                print(f'Снятие: {self.cash}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
