# coding: utf-8
# license: GPLv3
from tournament import *
from hero_classes import *
from artifacts import *

def shop(hero, class_name):
    money = hero._money
    print('Приветствую, могучий',class_name, hero._name, 'Вы посетили магазин. На вашем счету {} денег'.format(money))
    print('Ваш инвентарь:')
    artifacts= generate_artifacts()
    for artifact in artifacts:
        print(artifact._name, artifact._amount)
    while True:
        print('Если хотите что-то продать, то введите 1, если хотите перейти к покупкам, нажмите 0')
        number = check_number_1()
        if number==0:
            break
        else:
            print('Выберите номер артефакта, который хотите продать')
            number = check_number_2()
            if artifacts[number - 1]._amount !=0:
                hero._money+=artifacts[number-1]._cost
                artifacts[number - 1]._amount -= 1
                hero._beauty -=artifacts[number-1]._valueb
                hero._speed -=artifacts[number-1]._values
                hero._health -=artifacts[number-1]._valueh
                hero._attack -=artifacts[number-1]._valuea
                print('Вы продали {}. Теперь на вашем счету {} денег'.format(artifacts[number - 1]._name,hero._money))
                print('Теперь ваши характеристики : Красота ->', hero._beauty, 'Скорость ->', hero._speed,'Здоровье ->', hero._health,'Атака ->', hero._attack )
            else:
                print('Вы не можете продать этот предмет, так как у вас его нет')

    print('Вы можете купить:')
    for nomer, artifact in enumerate(artifacts):
        print('{}.{} за {}'.format(nomer + 1, artifact._name, artifact._cost))
    while True:
        print('Выберите номер артефакта, который хотите приобрести, чтобы продать, или 0, если хотите покинуть магазин.')
        number=check_number_3()
        if number==0:
            print('Выхожу из магазина')
            break


        else:
            if hero._money>=artifacts[number-1]._cost:
                artifacts[number - 1]._amount+=1
                hero._money-=artifacts[number-1]._cost
                hero._beauty += artifacts[number - 1]._valueb
                hero._speed += artifacts[number - 1]._values
                hero._health += artifacts[number - 1]._valueh
                hero._attack += artifacts[number - 1]._valuea
                print('Вы купили {}'.format(artifacts[number-1]._name))
                print('Теперь ваши характеристики : Красота ->',hero._beauty,'Скорость ->',hero._speed,'Здоровье ->',hero._health ,'Атака ->', hero._attack )
            else:
                print('У вас не хватает денег на этот артефакт')

def check_number_1():
    number = None
    correct_numbers = [0, 1]
    while number == None:
        try:
            number = int(input())
            for i in correct_numbers:
                if i==number:
                    return number
            print('Артефакта с таким номером нет')
            number = None
        except ValueError:
            print('Вы ввели недопустимые символы')



def check_number_2():
    number = None
    correct_numbers = [1, 2, 3, 4, 5]
    while number == None:
        try:
            number = int(input())
            for i in correct_numbers:
                if i == number:
                    return number
            print('Артефакта с таким номером нет')
            number = None
        except ValueError:
            print('Вы ввели недопустимые символы')
    return number



def check_number_3():
    number = None
    correct_numbers = [0, 1, 2, 3, 4, 5,9]
    while number == None:
        try:
            number = int(input())
            for i in correct_numbers:
                if i == number:
                    return number
            print('Артефакта с таким номером нет')
            number = None
        except ValueError:
            print('Вы ввели недопустимые символы')
    return number
