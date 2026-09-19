import random
backpack=[]
winrate=0.5
print("добро пожаловать на арену смерти тебе нужно выбрать оружие для сражения и предметы")
sword=int(input("что ты выберешь 1.тяжелое оружие или 2.легкое оружие или 3.дальнобойное:"))
probability=random.random()
if sword==1:
    sword1=int(input("1.двуручный меч 2.тяжелый топор:"))
    if sword1==1:
        backpack.append("двуручный меч")
    if sword1==2:
        backpack.append("тяжелый топор")
if sword==2:
    sword3=int(input("1.кинжал 2.катана:"))
    if sword3==1:
        backpack.append("кинжал")
    if sword3==2:
        backpack.append("катана")
if sword==3:
    sword4=int(input("1.лук 2.сюрикены:"))
    if sword4==1:
        backpack.append("лук")
    if sword4==2:
        backpack.append("сюрикены")
potion=int(input("какое зелье ты выберешь 1.зелье здоровья 2.зелье увеличивающее неуязвимость 3.зелье увеличивающее урон:"))
if potion==1:
    backpack.append("зелье здоровья")
if potion==2:
    backpack.append("зелье увеличивающее неуязвимость ")
if potion==3:
    backpack.append("зелье увеличивающее урон")
print(backpack)
print("против тебя выходят зомби ")
if backpack==['двуручный меч', 'зелье здоровья']:
    winrate=0.3
    if probability<winrate:
        print("тебе нанесли смертельный урон")
        if probability<winrate:
            print("ты проиграл")
            exit()
        else:
            print("ты победил")
            exit()
    else:
        print("ты победил")
        exit()
  
if backpack==['двуручный меч', 'зелье увеличивающее неуязвимость ']:
    winrate=0.3
    if probability>winrate:
        print("ты победил")
        exit()
    else:
        print("ты проиграл")
        exit()
if backpack==['двуручный меч', 'зелье увеличивающее урон']:
    winrater=0.2
    if probability>winrate:
        print("ты победил")
        exit()
    else:
        print("ты проиграл")
        exit()
if backpack==['тяжелый топор', 'зелье здоровья']:
    winrate=0.3
    if probability<winrate:
        print("тебе нанесли смертельный урон но ты вылечился")
        if probability>winrate:
            print("ты победил")
            exit()
        else:
            print("ты проиграл")
            exit()
    else:
        print("ты победил")
if backpack==['тяжелый топор', 'зелье увеличивающее неуязвимость ']:
    winrate=0.2
    if probability<winrate:
        print("ты проиграл")
        exit()
    else:
        print("ты победил")
        exit()
if backpack==['тяжелый топор', 'зелье увеличивающее урон']:
    winrate=0.1
    if probability<winrate:
        print("ты проиграл")
        exit()
    else:
        print("ты победил")
        exit()
if backpack==['кинжал', '']:
    winrate=0.6
    if probability<winrate:
        print("тебе нанесли смертельный удар но ты воспользовался зельем")
        if probability>winrate:
            print("ты победил")
            exit()
        else:
            print("ты проиграл")
            exit()
    else:
        print("ты победил")
        exit()
if backpack==['кинжал', 'зелье увеличивающее неуязвимость ']:
    winrate=0.6
    if probability<winrate:
        print("ты проиграл")
        exit()
    else:
        print("ты победил")
        exit()
if backpack==['кинжал', 'зелье увеличивающее урон']:
    winrate=0.5
    if probability<winrate:
        print("ты проиграл")
        exit()
    else:
        print("ты победил")
        exit()
if backpack==['катана', 'зелье здоровья']:
    winrate=0.4
    if probability<winrate:
        print("тебе нанесли смертельный удар")
        if probability<winrate:
            print("ты проиграл")
            exit()
        else:
            print("ты победил")
            exit()
    else:
        print("ты победил")
        exit()
if backpack==['катана', 'зелье увеличивающее неуязвимость ']:
    winrate=0.3
    if probability<winrate:
        print("ты проиграл")
        exit()
    else:
        print("ты победил")
        exit()
if backpack==['катана', 'зелье увеличивающее урон']:
    winrate=0.2
    if probability<winrate:
        print("ты проиграл")
        exit()
    else:
        print("ты победил")
        exit()
if backpack==['лук', 'зелье здоровья']:
    winrate=0.7
    if probability<winrate:
        print("тебе нанесли смертельный урон ты выжил из за зелья")
        if probability<winrate:
            print("ты проиграл")
            exit()
        else:
            print("ты победил")
            exit()
    else:
        print("ты победил")
        exit()
if backpack==['лук', 'зелье увеличивающее неуязвимость ']:
    winrate=0.6
    if probability<winrate:
        print("ты проиграл")
        exit()
    else:
        print("ты победил")
        exit()
if backpack==['лук', 'зелье увеличивающее урон']:
    winrate=0.5
    if probability<winrate:
        print("ты проиграл")
        exit()
    else:
        print("ты победил")
        exit()
if backpack==['сюрикены', 'зелье здоровья']:
    winrate=0.5
    if probability<winrate:
        print("ты проиграл и воспользовался зельем")
        if probability<winrate:
            print("ты проиграл")
            exit()
        else:
            print("ты победил")
            exit()
    else:
        print("ты победил")
        exit()
if backpack==['сюрикены', 'зелье увеличивающее неуязвимость ']:
    winrate=0.4
    if probability<winrate:
        print("ты проиграл")
        exit()
    else:
        print("ты победил")
        exit()
if backpack==['сюрикены', 'зелье увеличивающее урон']:
    winrate=0.3
    if probability<winrate:
        print("ты проиграл")
        exit()
    else:
        print("ты победил")
        exit()
