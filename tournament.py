# coding: utf-8
# license: GPLv3
from enemies import *
from hero_classes import *
from shop import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list,class_name):
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')
        hero._experience+=10*hero._importance
        hero._money += 100 / hero._importance

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
        print('Ваши накопленные деньги:', hero._money)
        shop(hero,class_name)
    else:
        print('К сожалению, Вы проиграли...')

def game_trollnament(hero, troll_list, class_name):
    for troll in troll_list:
        print('Вышел', troll._color, 'тролль!')
        while troll.is_alive() and hero.is_alive():
            print('Вопрос:', troll.question())
            answer = input('Ответ:')

            if troll.check_answer(answer):
                hero.attack(troll)
                print('Верно! \n** троллю неприятно **')
            else:
                troll.attack(hero)
                print('Ошибка! \n** от вас откусили кусочек... **')
        if troll.is_alive():
            break
        print('Тролль', troll._color, 'затроллен!\n')
        hero._experience+=20*hero._importance
        hero._money+=100/hero._importance

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
        print('Ваши накопленные деньги:', hero._money)
        shop(hero,class_name)
    else:
        print('К сожалению, Вас сожрали...')

def rod_dragon(number):
    if number%100 in [11,12,13,14]:return 'драконов'
    if number%10 in [2,3,4]:return 'дракона'
    if number%10==1:return 'дракон'
    else:return 'драконов'

def rod_troll(number):
    if number%100 in [11,12,13,14]:return 'троллей'
    if number%10 in [2,3,4]:return 'тролля'
    if number%10==1:return 'тролль'
    else:return 'троллей'

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        name = input()
        print('Выберете класс(Wizard(75,120), Healer(50,50), Jagernaut(120,60), Imba(1000,1000)): ', end='')
        class_name = input()
        if class_name == 'Wizard':
            hero = Wizard(name)
            hero._health = 75
            hero._attack = 120
            hero._importance = 1.5
        if class_name == 'Jagernaut':
            hero = Jagernaut(name)
            hero._health = 125
            hero._attack = 60
            hero._importance = 1.15
        if class_name == 'Healer':
            hero = Healer(name)
            hero._health = 50
            hero._attack = 50
            hero._importance = 10
        if class_name == 'Imba':
            hero = Imba(name)
            hero._health = 1000
            hero._attack = 1000
            hero._importance = 5
        hero._money = 100
        hero._experience = 0

        print('Приветствую тебя, ',class_name, hero._name,'!')
        if randint(1,2)==1:
            dragon_number = randint(2,15)
            dragon_list = generate_dragon_list(dragon_number)
            print('У Вас на пути', dragon_number, rod_dragon(dragon_number)+'!')
            game_tournament(hero, dragon_list,class_name)
        else:
            troll_number = randint(2,15)
            troll_list = generate_troll_list(troll_number)
            print('Вам не дают пройти', troll_number, rod_troll(troll_number)+'!')
            game_trollnament(hero, troll_list,class_name)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
