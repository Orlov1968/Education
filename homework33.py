import threading
import time

import queue


class Table:

    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(threading.Thread):

    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        cafe.serve_customer()


class Cafe:

    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 20:
            print(f"Посетитель номер {customer_number} прибыл")
            customer = Customer(customer_number)
            customer.start()
            time.sleep(1)
            customer_number += 1

    def serve_customer(self, customer):
        table_found = True
        for t in tables:
            if t == table_found:
                print(f"Посетитель {customer} сел за стол {tables[t]}.")
                time.sleep(5)
                print(f"Посетитель номер {customer} покушал и ушёл.")
            else:
                print(f"Посетитель {customer} ожидает свободный стол")


table_1 = Table(1)
table_2 = Table(2)
table_3 = Table(3)
tables = [table_1, table_2, table_3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival())
customer_arrival_thread.start()

customer_arrival_thread.join()
