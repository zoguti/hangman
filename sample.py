import random
def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        char=(input("moji:"))
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
            
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        
        if "_" not in board:
            print("you Win")
            print(" ".join(board))
            win=True
            break
            
    if not win:
         print("¥n".join(stages[0:wrong+1]))
         print("you lose.true word is{}".format(word))

animals=["snake","emp","dog","raian"]
a=random.randint(0,3)
hangman(animals[a])
