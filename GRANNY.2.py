import random

a = 0
print("ДЕНЬ ДОБРЫЙ, Я РАДА ТЕБЯ ВИДЕТЬ!")
while True:
    user = input("")
    if user == "ПОКА!":
        a = a + 1
        if a == 3:
            print("УДАЧИ, ДОРОГОЙ!")
            break  # это останавливает цикл while
        else:
            year = random.randint(1930, 1950)
            print("А? ПОМНЮ, ТЕБЯ МАЛЕНЬКОГО С " + str(year) + " ГОДА!")
    elif user.isupper():
        year = random.randint(1930, 1950)
        print("А? ПОМНЮ, ТЕБЯ МАЛЕНЬКОГО С " + str(year) + " ГОДА!")
    else:
        print("АСЬ?! Я ОЧЕНЬ СЛАБО СЛЫШУ ТЕБЯ!")
