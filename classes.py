import random


# Класс Barrel представляет бочонок
class Barrel:
    def __init__(self):
        # Инициализация бочонков числами от 1 до 90
        self.barrels = list(range(1, 91))

    # Метод для извлечения случайного бочонка из списка
    def draw(self):
        # Проверка на наличие бочонков в списке
        if self.barrels:
            # Извлечение случайного бочонка и удаление его из списка
            return self.barrels.pop(random.randint(0, len(self.barrels) - 1))
        else:
            # Возвращение None, если список пуст
            return None


# Класс Card представляет карточку игрока
class Card:
    __rows = 3
    __cols = 9
    __nums_in_row = 5

    def __init__(self):
        # Количество чисел в строке
        # Инициализация пустых строк для карточки
        self.rows = []
        # Создание карточки при инициализации
        for _ in range(self.__rows):
            self.rows.append([])
        self.generate_card()

    # Метод генерации случайной карточки с уникальными числами
    def generate_card(self):
        # Определяем количество чисел в карточке
        total_numbers = len(self.rows) * self.__cols

        # Генерация уникальных чисел для всей карточки
        unique_numbers = set()
        while len(unique_numbers) < total_numbers:
            unique_numbers.add(random.randint(1, 91))

        # Распределение чисел по строкам
        for row in self.rows:
            # Получение двух уникальных чисел для каждой строки
            row_numbers = random.sample(unique_numbers, self.__cols)
            # Удаление выбранных чисел из общего множества уникальных чисел
            unique_numbers -= set(row_numbers)
            # Сортировка чисел по возрастанию
            row.extend(sorted(row_numbers))

    # Метод отображения карточки
    def display(self):
        for row in self.rows:
            print(row)

    # Метод зачеркивания числа на карточке
    def mark_number(self, number):
        for row in self.rows:
            if number in row:
                # Замена числа на "X" в случае совпадения
                row[row.index(number)] = "X"

    # Метод для проверки наличия победителя на карточке
    def check_for_winner(self):
        for row in self.rows:
            # Проверка, что все числа в строке зачеркнуты
            if not all(cell == "X" for cell in row):
                return False
        # Возвращение True, если все числа во всех строках зачеркнуты
        return True


# Класс Game представляет процесс игры
class Game:
    def __init__(self, player_card, computer_card):
        # Инициализация бочонка и карточек для игрока и компьютера
        self.barrel = Barrel()
        self.player_card = player_card
        self.computer_card = computer_card

    def is_valid_choice(self, choice):
        return choice.lower() in ["y", "n"]

    # Метод выполнения хода
    def play_turn(self):
        # Извлечение случайного бочонка
        number = self.barrel.draw()
        print(f"Выпал бочонок с номером: {number}")

        # Вывод карточки игрока
        print("\nВаша карточка:")
        self.player_card.display()
        # Пользователь выбирает зачеркнуть или продолжить
        action = input("Зачеркнуть цифру? (y/n): ").lower()
        while not self.is_valid_choice(action):
            print("Некорректный выбор. Пожалуйста, введите 'y' или 'n'.")
            action = input("Зачеркнуть цифру? (y/n): ")

        # Если пользователь решил зачеркнуть
        if action == "y":
            for row in self.player_card.rows:
                for cell in row:
                    # Зачеркивание числа, если оно присутствует на карточке
                    if number == cell:
                        self.player_card.mark_number(number)
                print("Цифра зачеркнута!\n")

            # Проверка наличия победителя после зачеркивания
            if self.player_card.check_for_winner():
                print("Вы победили!")
                return True
            else:
                return False

        # Если пользователь решил продолжить
        else:
            if number in [cell for row in self.player_card.rows for cell in row]:
                # Если число присутствует на карточке, пользователь проигрывает
                print("Вы не зачеркнули цифру, которая есть на вашей карточке. Вы проиграли!\n")
                return True

        # Вывод карточки компьютера
        print("\nКарточка компьютера:")
        self.computer_card.display()

        # Зачеркивание числа на карточке компьютера
        if number in [cell for row in self.computer_card.rows for cell in row]:
            self.computer_card.mark_number(number)
            print("Цифра зачеркнута!\n")
        else:
            print("Цифры нет на карточке компьютера.\n")

        return False

    # Метод для выполнения всей игры
    def play_game(self):
        while True:
            # Если текущий ход возвращает True, игра завершается
            if self.play_turn():
                print("Игра завершена.")
                break


