from random import random, randint, uniform
print("=======Old format========")
team1_num = 5
team2_num = 6
print("В команде Мастера кода участников: %d !" % team1_num)
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

print("========New format=======")

score1 = randint(20, 50)
score2 = randint(20, 50)
team1_time = uniform(15000.0, 20000.0)
team2_time = uniform(15000.0, 20000.0)
tasks_total = score1 + score2
time_avg = (team1_time + team2_time)/tasks_total

print("Команда Волшебники данных решила задач: {0:d} !".format(score1))
print("Волшебники данных решили задачи за {0:5.1f} с !".format(team1_time))

print("=======Very new format=======")

if score1 > score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = "Победа команды Мастера кода!"
elif score1 < score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = "Победа команды Волшебники данных!"
else:
    challenge_result = "Ничья!"

print(f"Команды решили {score1} и {score2} задач")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решенно {tasks_total} задач, в среднем по {time_avg:5.1f} секунды на задачу!")
