import random

def hangman(word):
    wrong_guesses = 0
    stages = ["", 
              "________      ",
              "|      |      ",
              "|      0      ", 
              r"|     /|\     ", 
              r"|     / \     ", 
              "|"
            ]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

wordlist = ["book","courage","demand","evidence","frequent","genuine","harmony","imagine","justice","knowledge","language","mystery","nature","opinion","progress","quality","respect","solution","tradition","unique","victory","wisdom","youth","zeal","balance","challenge","decision","effort","freedom","growth","honor","inspire","journey","kindness","limit","moment","network","opportunity","potential","question","resource","strength","trust","understand","value","wonder","yearn","zone"]
hangman(wordlist[random.randint(0,49)])
