from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, skil, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skil = skil

    def run(self):
        enemies = 100
        count = 0
        print(f"{self.name} на нас напали!")
        while enemies > 0:
            sleep(1)
            enemies = enemies - self.skil
            count += 1
            print(f"{self.name} сражается {count} дней, осталось {enemies} братков")
        print(f"{self.name} одержал победу спустя {count} дней!")


epic_hero_1 = Knight("Илья Ростовский", 20)
epic_hero_2 = Knight("Добрыня Питерский", 10)

epic_hero_2.start()
epic_hero_1.start()

epic_hero_1.join()
epic_hero_2.join()

print("Все битвы закончились!")
