# Определить действия в программе. Что программа будет делать. Под каждое действие нужна своя функция.
# Одно действие - одна функция
# Для начала делаем минимально жизнеспособный продукт. Реализуем рабочий код. Дл начала делаем минимум
# Игра Виселица: программа загадывает слово, и предлагает его угодать вводя по 1 букве.
# Если пользователь угадывает букву, программа сообщает ему об этом и запоминает что эту букву уже угадали.
# Программа закроется когда пользователь угадает все буквы или потратит все попытки (3).
# В случае успеха - Поздравляем вы угаадали
# В случае провала - Вы проиграли
# Если пользователь повторно вводит уже угаданную букву - Предупреждение: эта буква уже угадана
# Если в слове есть повторяющиеся буквы - они угадываются за 1 попытку.

import random
# импользуй faker


if __name__ == "__main__":
    game_over = False
    while not game_over:

        print("Попробуй угадать слово по буквам")

        glossary = ("Книга", "Игра", "Смерть")
        attempts = 5
        hidden_word = [item for item in random.choice(glossary).lower()] # сделать проще, без генерации списка
        guessed_word = ['_' for item in range(len(hidden_word))]
        entered_letters = []

        while attempts != 0 and not game_over:
            player_input = input("Введите букву: ").lower()
            while player_input in entered_letters:
                print('Букву уже вводили')
                player_input = input("Введите букву: ").lower()
            entered_letters += player_input
            for i in range(len(hidden_word)):
                if player_input == hidden_word[i]:
                    guessed_word[i] = hidden_word[i]
            if player_input not in hidden_word:
                attempts -= 1
                print(f"Осталось {attempts} попыток")
            if guessed_word == hidden_word:
                print('Поздравляем, вы угадали')
                game_over = True
                break # реализовать без этого
            print(guessed_word)
        else:
            print("Вы проиграли")
            game_over = True
