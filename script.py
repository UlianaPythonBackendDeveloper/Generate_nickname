import random


def generate_nicknames():
    adgject = ['быстрый', 'сильный', 'умный', 'ловкий', 'храбрый', 'тихий', 'громкий', 'волшебный']
    nouns = ['волк', 'тигр', 'орел', 'дракон', 'воин', 'маг', 'ниндзя','кот']
    numbers = ['777', '123', '888', '666', '999', '404']    
    symbols = ['_', '-', '', '.', 'X', '$','#',')']
    
    adj = random.choice(adgject)
    non = random.choice(nouns)
    num = random.choice(numbers)
    symb = random.choice(symbols)
    
    nickname = adj + non + num + symb
    return nickname

for i in range(10):
    print(generate_nicknames())