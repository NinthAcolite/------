import random

a = 0
print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")
while True:
    user = input("")
    if user == "ПОКА!":
        a = a + 1
        if a == 3:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
            break  # это останавливает цикл while
        else:
            year = random.randint(1930, 1950)
            print("НЕТ, НИ РАЗУ С " + str(year) + " ГОДА!")
    elif user.isupper():
        year = random.randint(1930, 1950)
        print("НЕТ, НИ РАЗУ С " + str(year) + " ГОДА!")
    else:
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
