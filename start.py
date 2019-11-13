'''
CTRL + /
обвести код, который надо закоментировать и далее горячие клавиши контрол-слеш
раскоментировать также
'''


# написать игру, в которую играет бот и стреляет в мешень.
#у бота есть N-кол-во выстрелов. когда выстрелы кончаются - показывается результат.

import random as rnd
import time as tm

# бот Вася
bot = {
    'name':'Вася',                  # имя бота
    'pistol_model':'desrt eagle',   # пистолет бота
    'number of rounds':10,          # кол-во патронов
    'miss':0,  # промахи
    'hit':0,   # попадания
    'specs':0   # очки

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

# мишень / 0 - мимо
target = (0,1,2,3,4,5)

# общая таблица рейтинга | имя | промахи | попадания | очков
table_result = []




# ПРОЦЕСС ИГРЫ
while (True):
    tm.sleep(1)

    # боты стреляют в мишень
    bot_shot = target[rnd.randrange(0,6)]   # Бот Вася
    bot_2_shot = target[rnd.randrange(0,6)] # Бот Петя
    tm.sleep(1)

    # проверяем, куда попал Вася
    if bot_shot != 0:
        bot['hit'] = bot['hit'] + 1
        bot['specs'] = bot['specs'] + bot_shot
        print("Бот " + bot['name'] + " попал! Получает - " + str(bot_shot) + " очк.!")
    else:
        bot['miss'] = bot['miss'] + 1  # запись промахов в ОБЩИЙ результат за игры.
        print("Бот " + bot['name'] + " промазал...")
        tm.sleep(1)

    print()

    # проверяем, куда попал Петя
    if bot_2_shot != 0:
        bot_2['hit'] = bot_2['hit'] + 1
        bot_2['specs'] = bot_2['specs'] + bot_2_shot
        print("Бот " + bot_2['name'] + " попал! Получает - " + str(bot_2_shot) +" очк.!")
    else:
        bot_2['miss'] = bot_2['miss'] + 1  # запись промахов в ОБЩИЙ результат за игры.
        print("Бот " + bot_2['name'] + " промазал...")
        tm.sleep(1)


    # Кол-во патронов у ботов равно нулю / всего их 10
    if bot['number of rounds'] == 0 & bot_2['number of rounds'] == 0:
        print('у ботов закончились патроны, игра окончена...')
        break


# результаты
tm.sleep(1)
print('Результат - ')
print('имя' + "\t" + "промахи"  + "\t" + "попадения"  + "\t" + "очки" )
#print(result[0] + "\t\t" + str(result[1])  + "\t\t" + str(result[2])  + "\t\t" + str(result[3]) )