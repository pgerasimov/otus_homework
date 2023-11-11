from classes import Card, Game

# Создание карточек для игрока и компьютера
player_card = Card()
computer_card = Card()

# Создание объекта игры и запуск игры
game = Game(player_card, computer_card)
game.play_game()
