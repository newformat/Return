# написать игру, в которую играет бот и стреляет в мешень.
#у бота есть N-кол-во выстрелов. когда выстрелы кончаются - показывается результат.

import random as rnd
import time as tm

# бот Вася
bot = {
    'name':'Вася',                  # имя бота
    'pistol_model':'desrt eagle',   # пистолет бота
    'number of rounds':10,          # кол-во патронов
    'miss':0,                       # промахи
    'hit':0,                        # попадания
    'specs':0                       # очки
}

# бот Петя
bot_2 = {
    'name': 'Петя',
    'pistol_model': 'Glock',
    'number of rounds':10,
    'miss': 0,
    'hit': 0,
    'specs':0
}

target = (0,1,2,3,4,5)  # мишень / 0 - мимо

# проверяем, куда попал бот
def where_to_hit(bot):
    bot_shot = target[rnd.randrange(0, 6)]
    print("Бот " + bot['name'] + " стрельнул...  ( 1 ( 2 ( 3 ) 4 ) 5 )")
    tm.sleep(3)
    if bot_shot != 0:
        bot['hit'] = bot['hit'] + 1
        bot['specs'] = bot['specs'] + bot_shot
        print("Бот " + bot['name'] + " попал! Получает - " + str(bot_shot) + " очк.!")
    else:
        bot['miss'] = bot['miss'] + 1  # запись промахов в ОБЩИЙ результат за игры.
        print("Бот " + bot['name'] + " промазал...")
        tm.sleep(1)
    bot['number of rounds'] -= 1

# ПРОЦЕСС ИГРЫ
while (True):
    tm.sleep(1)
    where_to_hit(bot)   # выстрел Васи
    print()
    where_to_hit(bot_2) # выстрел Пети

    # Кол-во патронов у ботов равно нулю / всего их 10
    if bot['number of rounds'] == 0 & bot_2['number of rounds'] == 0:
        print('\nу ботов закончились патроны, игра окончена...\n')
        break
    else:
        print("\nБот " + bot['name'] + "; кол-во патронов - " + str(bot['number of rounds']))
        print("Бот " + bot_2['name'] + "; кол-во патронов - " + str(bot_2['number of rounds']) + '\n')

# результаты
tm.sleep(1)
print('Результат - ')
print("имя\t\tпромахи\tпопадения\tочки" )
tm.sleep(1)
print(bot['name'] + "\t\t" + str(bot['miss']) + "\t\t" + str(bot['hit'])  + "\t\t" + str(bot['specs']))
print(bot_2['name'] + "\t\t" + str(bot_2['miss']) + "\t\t" + str(bot_2['hit'])  + "\t\t" + str(bot_2['specs']))
tm.sleep(1)

# кто выйиграл?
if bot['specs'] > bot_2['specs']:
    print("Бот " + bot['name'] + " выиграл!")
elif bot['specs'] < bot_2['specs']:
    print("Бот " + bot_2['name'] + " выиграл!")
else:
    print('ничья...')