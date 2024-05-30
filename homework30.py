
from threading import Thread
from time import sleep


def numbers_print():
    for i in range(10):
        print(i + 1)
        sleep(1)


def letter_print():
    alphabet = [chr(i) for i in range(97, 107)]
    for i in alphabet:
        print(i)
        sleep(1)


thread_number = Thread(target=numbers_print)
thread_letter = Thread(target=letter_print)


thread_letter.start()
thread_number.start()

thread_number.join()
thread_letter.join()
