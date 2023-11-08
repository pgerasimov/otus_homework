import random


class Barrel:
    def __init__(self):
        self.barrels = list(range(1, 90))

    def draw(self):
        if self.barrels:
            return self.barrels.pop(random.randint(0, len(self.barrels)))
        else:
            return None


class Card:
    def __init__(self):
        self.generate_card()

    def generate_card(self):
        # Генерация карточку
        pass

    def display(self):
        # Отображение карточки
        pass

    def mark_number(self, number):
        # Зачеркивание числа
        pass

    def is_winner(self):
        # Проверка победы
        pass


class Player:
    def __init__(self, name, type):
        self.name = name
        self.player_type = type
        self.card = Card()

    def make_move(self, number):
        # Ход игрока
        pass


class Game:
    def __init__(self, players):
        self.players = players
        self.barrel = Barrel()
        self.current_player = players[0]

    def start(self):
        # Цикл игры
        pass
