from queue import Queue, Empty
from threading import Thread
from time import sleep


def customer_arrival(queue):
    for i in range(1, 21):
        print(f"Посетитель номер {i} прибыл")
        sleep(1)
        queue.put(i)


def serve_customer(queue):
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f"Посетитель {item} сел за стол")
            print(f"Посетитель {item} покушал и ушёл")
            sleep(5)
            queue.task_done()


def main():
    queue = Queue()
    arrival = Thread(target=customer_arrival, args=(queue,))
    arrival.start()
    serve = Thread(target=serve_customer, args=(queue,), daemon=True)
    serve.start()
    arrival.join()
    queue.join()


if __name__ == '__main__':
    main()
