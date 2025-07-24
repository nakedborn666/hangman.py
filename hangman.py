import random

def hangman():
    with open('russian.txt', 'r', encoding='utf-8') as file:          #файл со словами
        text = file.read()
        words = text.split()

    random_word = random.choice(words)


    tries = 6
    print("Нажмите '1', чтобы начать игру, или нажмите '0', чтобы выйти из игры.")
    def start_game(choice):         #функция старта игры, принимает параметр choice. Дается на выбор только "1"(начать игру) и "0"(выйти с игры).
        if choice == "1":
           return True
        elif choice == "0":
            print("Конец игры")
            return False
        else:     #если вводится что-то другое, то то игроку снова предлагается ввести 1 или 2, пока игрок не введет нужную цифру
            print("Вы ввели неверный символ, введите '1', чтобы начать игру, или нажмите '0', чтобы выйти из игры")
            choice = input()
            while choice != "1" or choice != "0":
                if choice == "1":
                    return True
                elif choice == "0":
                    print("Конец игры")
                    return False
                else:
                    print("Вы ввели неверный символ, введите '1', чтобы начать игру, или нажмите '0', чтобы выйти из игры")
                    choice = input()
    def valid_letter(letter):         #функция валидации буквы. Обязательно кириллица. первое условие ввел, т.к. если вводилось два символа или пробел происходила ошибка и второе условие не проходило
        if len(letter) > 1 or len(letter) < 1:
            return False
        elif 1072 <= ord(letter.lower()) <= 1103:     #диапазон в юникоде для кириллицы
            return True
        else:
            return False

    def display_hangman(tries):    #функция с рисункомв виселица(подаются попытки)
        stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''',
                    # голова, торс, обе руки, одна нога
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    ''',
                    # голова, торс, обе руки
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    ''',
                    # голова, торс и одна рука
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    ''',
                    # голова и торс
                    '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    ''',
                    # голова
                    '''
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    ''',
                    # начальное состояние
                    '''
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    '''
        ]
        return stages[tries]






    def check_letter_in_word(letter, word):  #функция проверки буквы в слове
        if set(letter.lower()).issubset(word):
            return True
            print("Вы угадали букву")
        else:
            return False



    def swap_letter(letter, word):    #функция замены буквы в masked_word, которая есть в изначальном слове. Находится индекс буквы в изначальном слове и на этот же индекс вставляется буква в masked_word
        for i in range(len(word)):
            if letter.lower() == word[i]:
                masked_word[i] = letter.lower()
        print(*masked_word)

    if start_game(input()):
        print("угадайте слово")
        word = list(random_word)      #подается рандомное слово из файла
        masked_word = ["*" for i in range(len(word))]    #создается masked_word из "*" по длинне изначального слова
        print(*masked_word)
        while masked_word != word and tries != 0:    #условие пока маскед ворд не равен слову или пока пока попыток не 0
            letter = input()
            if valid_letter(letter) == True and check_letter_in_word(letter, word) == True:  #если функция валидации и функция проверки буквы в слове возвращают тру, то принтуется что вы угадали букву и выполняется функция замены буквы
                print(display_hangman(tries))
                print("Вы угадали букву")
                swap_letter(letter, word)
            elif valid_letter(letter) == True and check_letter_in_word(letter, word) == False:   #если буквы в слове нет, то счетчик попыток уменьшается на один
                tries -= 1
                print(display_hangman(tries))
                print("Вы не угадали букву")
                print(*masked_word)
                if tries != 0:      #условие внутри сделал другого, потому что если вот этот принт выводить в прошлом условии, то когда попыток ноль принтовалось у вас осталось ноль попыток, а не просто попытки кончились, как ниже.
                    print(f'осталось {tries} попыток')
            elif valid_letter(letter) == False:
                print("Введите одну букву кириллицы")
        if tries == 0:      #когда попытки кончаются, выводится изначальное слово
            print(display_hangman(tries))
            print("попытки закончились")
            print("вы проиграли")
            print("неотгаданное слово - ", *word, sep = '')
        elif masked_word == word:
            print("слово угадано, вы выиграли")

hangman()


