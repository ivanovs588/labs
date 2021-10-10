from random import randint
from datetime import datetime
from time import sleep

class Attacker:
    _health = None
    _attack = None

    def attack(self, target):
        target._health -= self._attack * (randint(5, 20) / 10)

    def is_alive(self):
        return self._health > 0
 from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def RandomEnemyType():
    a = GreenDragon()
    b = RedDragon()
    c = BlackDragon()
    return choice([a, b, c])

def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def __init__(self):
        self._health = randint(100, 200)
        self._attack = randint(10, 20)

    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        super().__init__()
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        super().__init__()
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        super().__init__()
        self._color = 'черный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
enemy_types = [GreenDragon, RedDragon, BlackDragon]
class Hero(Attacker):
    def __init__(self, name):
        self._health = 100
        self._attack = 50
        self._experience = 0
        self._name = name

    def add_experience(self, experience):
        self._experience += experience
def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Были введены недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print("\033[H\033[J")
        print('Вышел', dragon._color, 'дракон!')
        start_dragon_time = datetime.now()
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли ** \n ** вы оставили дракону {} здоровья **'.format(dragon._health))
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... ** \n ** дракон оставил вам {} здоровья **'.format(hero._health))
        if dragon.is_alive():
            break
        experience = round(100 / (datetime.now() - start_dragon_time).seconds)
        print('Дракон', dragon._color, 'повержен! Вам начисленно {} опыта\n'.format(experience))
        hero.add_experience(experience)
        sleep(3)

    if hero.is_alive():
        print('Поздравляем! Вы победили! GG')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('YOU DIED')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 3)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился, ответы больше не принимаются.')
if __name__ == '__main__':
    start_game()
 
