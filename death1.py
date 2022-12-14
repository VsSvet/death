import random


def check_user_input(letter: str):
    if len(letter) == 1:
        return ord(letter) in range(1040, 1104)
    else:
        return input("Нужно ввести одну букву: ")


def check_repetitions_user_input(user_input, entered_letters):
    return user_input not in entered_letters


def check_presence_letter_in_word(user_input, hidden_word, guessed_word):
    for i in range(len(hidden_word)):
        if user_input == hidden_word[i]:
            guessed_word[i] = hidden_word[i]
    print(*guessed_word)


if __name__ == "__main__":
    game_over = False
    while not game_over:
        print("Попробуй угадать слово по буквам")

        glossary = ("Книга", "Игра", "Смерть")
        attempts = 5
        hidden_word = list(random.choice(glossary).lower())

        guessed_word = list("_" * len(hidden_word))
        entered_letters = []
        print(f"В загаданном слове {len(guessed_word)} букв")
        print(*guessed_word)

        while not game_over:
            user_input = input("Введите букву: ").lower()
            if check_user_input(user_input):
                while not check_repetitions_user_input(user_input, entered_letters):
                    user_input = input("Эту букву уже вводили, введите другую: ").lower()
                entered_letters += user_input
                check_presence_letter_in_word(user_input, hidden_word, guessed_word)
                if user_input not in hidden_word:
                    attempts -= 1
                    print(f"Осталось {attempts} попыток")

            if attempts < 1:
                print("Вы проиграли")
                game_over = True
            elif guessed_word == hidden_word:
                print('Поздравляем, вы угадали')
                game_over = True