from unittest.mock import patch

from classes import Barrel, Card, Game


# Тесты для Barrel
def test_barrel_draw():
    # Тест проверяет, что метод draw() возвращает число в правильном диапазоне.
    barrel = Barrel()
    number = barrel.draw()
    assert 1 <= number <= 90


def test_barrel_empty():
    # Тест проверяет, что метод draw() возвращает None, когда бочонки заканчиваются.
    barrel = Barrel()
    for _ in range(89):
        barrel.draw()
    assert barrel.draw() is None


# Тесты для Card
def test_card_creation():
    # Тест проверяет, что объект Card успешно создается.
    card = Card()
    assert isinstance(card, Card)


def test_card_dimensions():
    # Тест проверяет правильное количество строк и столбцов на карточке.
    card = Card()
    assert len(card.rows) == Card._Card__rows
    for row in card.rows:
        assert len(row) == Card._Card__cols


def test_number_and_space_distribution():
    # Тест проверяет правильное распределение чисел и пробелов в каждой строке карточки.
    card = Card()
    for row in card.rows:
        nums_count = sum(cell.strip().isdigit() for cell in row)
        spaces_count = sum(not cell.strip().isdigit() for cell in row)
        assert nums_count == Card._Card__nums_in_row
        assert spaces_count == Card._Card__cols - Card._Card__nums_in_row


def test_no_repeating_numbers_in_row():
    # Тест проверяет отсутствие повторяющихся чисел внутри каждой строки карточки.
    card = Card()
    for row in card.rows:
        nums = []
        for cell in row:
            if cell.strip().isdigit():
                num = int(cell)
                nums.append(num)
    assert len(nums) == len(set(nums))


def test_check_for_winner_empty_row():
    # Тест проверяет, что метод check_for_winner возвращает True, если все числа в строке зачеркнуты.
    card = Card()

    # Зачеркиваем все числа в одной строке
    row = card.rows[0]
    for i, cell in enumerate(row):
        if cell.strip().isdigit():
            row[i] = "X"

    assert card.check_for_winner()


# Тесты для Game
def test_game_init():
    # Тест проверяет, что создаются обе карточки и боченок при запуске игры
    with patch('classes.Barrel') as mock_barrel:
        game = Game(Card(), Card())

        # Проверяем, что обе карточки успешно созданы
        assert isinstance(game.player_card, Card)
        assert isinstance(game.computer_card, Card)

        # Проверяем, что боченок успешно создан
        assert game.barrel == mock_barrel.return_value
