from queue import Queue
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = True


class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = Queue(3)

    def customer_arrival(self):
        for i in range(1, 20):
            print(f"Посетитель номер{i} прибыл")
            sleep(1)
            self.queue.put(i)

    def serve_customer(self, customer):
        while True:
            item = self.queue.get()
            if item is None:
                break
        print(f"Посетитель{item} сел за стол {self.tables}")
        print(f"Посетитель{item} покушал и ушёл")
        sleep(5)
