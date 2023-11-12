import random


# Класс Barrel представляет бочонок
class Barrel:

    def __init__(self):
        # Инициализация бочонков числами
        self.barrels = list(range(1, 90))

    # Метод получения случайного бочонка
    def draw(self):
        # Проверка на наличие бочонков
        if self.barrels:
            # Получение случайного бочонка и удаление его из списка
            return self.barrels.pop(random.randint(0, len(self.barrels) - 1))
        else:
            # Возвращение None, если список пуст
            return None


# Класс Card представляет карточку игрока
class Card:
    # Параметры карточки
    __rows = 3
    __cols = 9
    __nums_in_row = 5

    def __init__(self):
        # Создание пустой карточки
        self.rows = []
        for _ in range(self.__rows):
            self.rows.append([])
        self.generate_card()

    # Метод генерации карточки
    def generate_card(self):
        # Генерация уникальных чисел для всей карточки
        unique_numbers = set(range(1, 90))
        random.shuffle(list(unique_numbers))

        # Распределение чисел по строкам
        for row in self.rows:
            # Генерация уникальных чисел для каждой строки
            row_numbers = sorted(random.sample(unique_numbers, self.__nums_in_row))

            # Удаление выбранных чисел из общего множества уникальных чисел
            unique_numbers -= set(row_numbers)

            # Заполнение строки карточки
            row_symbols = []
            for num in row_numbers:
                row_symbols.append(str(num))

            # Добавление пробелов в случайных местах
            for _ in range(self.__cols - self.__nums_in_row):
                row_symbols.insert(random.randint(0, len(row_symbols)), " ")

            # Заполнение строки карточки
            row.extend(row_symbols)

    # Метод отображения карточки
    def display(self):
        # Вывод разделителя в начале карточки
        print("-" * 28)
        for row in self.rows:
            # Вывод строки карточки
            print(" ".join(row))
        # Вывод разделителя в конце карточки
        print("-" * 28)

    # Метод зачеркивания числа на карточке
    def mark_number(self, number):
        for row in self.rows:
            if number in row:
                # Замена числа на "X" в случае совпадения
                index = row.index(number)
                row[index] = "X"

    # Проверка наличия чисел в строке
    @staticmethod
    def has_numbers(row):
        for cell in row:
            if cell.strip().isdigit():
                return True
        return False

    # Метод для проверки победителя
    def check_for_winner(self):
        for row in self.rows:
            # Проверка, что все числа в строке зачеркнуты
            if not self.has_numbers(row):
                return True
        # Возвращение False, если есть не зачеркнутые числа
        return False


# Класс Game представляет процесс игры
class Game:
    def __init__(self, player_card, computer_card):
        # Инициализация бочонка и карточек для игрока и компьютера
        self.barrel = Barrel()
        self.player_card = player_card
        self.computer_card = computer_card

    @staticmethod
    def is_valid_choice(choice):
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
            found = False
            for row in self.player_card.rows:
                for i, cell in enumerate(row):
                    if cell.strip().isdigit() and int(cell) == number:
                        # Если число присутствует на карточке и не зачеркнуто, зачеркиваем его
                        if cell != "X":
                            self.player_card.mark_number(int(cell))
                            row[i] = "X"  # Зачеркиваем числовое значение на карточке
                            found = True
                            break

            if found:
                print("Цифра зачеркнута!\n")
                # Проверка наличия победителя после зачеркивания
                if self.player_card.check_for_winner():
                    print("Вы победили!")
                    return True
            else:
                # Если числа нет на карточке, пользователь проиграл
                print("Такой цифры на вашей карточке нет или она уже зачеркнута. Вы проиграли!\n")
                return True

        # Если пользователь решил продолжить
        else:
            for row in self.player_card.rows:
                for cell in row:
                    if cell.strip().isdigit() and int(cell) == number and cell != "X":
                        # Если число присутствует на карточке, пользователь проигрывает
                        print("Вы не зачеркнули цифру, которая есть на вашей карточке. Вы проиграли!\n")
                        return True

        # Вывод карточки компьютера
        print("\nКарточка компьютера:")
        self.computer_card.display()

        # Проверка, что число присутствует на карточке компьютера и не зачеркнуто
        found = False
        for row in self.computer_card.rows:
            for i, cell in enumerate(row):
                if cell.strip().isdigit() and int(cell) == number:
                    # Если число присутствует на карточке и не зачеркнуто, зачеркиваем его
                    if cell != "X":
                        self.computer_card.mark_number(int(cell))
                        row[i] = "X"  # Зачеркиваем числовое значение на карточке
                        found = True
                        break

        if found:
            print("Цифра зачеркнута!\n")
        else:
            print("Цифры нет на карточке компьютера.\n")

        # Проверка наличия победителя после зачеркивания
        if self.computer_card.check_for_winner():
            print("Компьютер победил!")
            return True

    # Метод для выполнения всей игры
    def play_game(self):
        while True:
            # Если текущий ход возвращает True, игра завершается
            if self.play_turn():
                print("Игра завершена.")
                break
