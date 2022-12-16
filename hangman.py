import random
import os
efecnblt = ['''
       __                 _     _ _   
  ___ / _| ___  ___ _ __ | |__ | | |_ 
 / _ \ |_ / _ \/ __| '_ \| '_ \| | __|
|  __/  _|  __/ (__| | | | |_) | | |_ 
 \___|_|  \___|\___|_| |_|_.__/|_|\__|''']
hangman = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

word_list = ["abruptly","absurd","boxful","cycle","duplex","exodus",
             "funny","gnostic","hyphen","injury","jumbo","knapsack",
             "luxury","mystify","nightclub","oxygen","puzzling",
             "quiz","rhythm","subway","transplant","unzip",
             "vortex","wizard","yummy","zigzag"]
chosen_word = random.choice(word_list)

os.system("clear")
print(bcolors.OKGREEN + f"\n{' '.join(efecnblt)}\n\n" + bcolors.ENDC)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(bcolors.UNDERLINE + f"{' '.join(alphabet)}\n" + bcolors.ENDC)


screen = []
guessed = []
game_over = False
counter = 6

for _ in range(len(chosen_word)):
    screen += "_"
print(bcolors.OKBLUE+ f"\t\t{' '.join(screen)}" + bcolors.ENDC)
print(bcolors.OKCYAN + hangman[0] + bcolors.ENDC)
while not game_over:
    guess_a_word  = input("\nGuess a word: ").lower()

    os.system("clear")

    if guess_a_word in guessed:
        print(bcolors.FAIL + f"\t\tYou already guessed '{guess_a_word}'!" +  bcolors.ENDC)
    elif guess_a_word not in guessed:
        if guess_a_word not in chosen_word:
            counter = counter - 1
        guessed += guess_a_word



    for point in range(len(chosen_word)):
        letter_in_word = chosen_word[point]
        if guess_a_word == letter_in_word:
            screen[point] = guess_a_word

    for position in range(len(alphabet)):
        letter_in_alphabet = alphabet[position]
        if guess_a_word == letter_in_alphabet:
            alphabet[position] = "-"

    guessed += guess_a_word

    print(bcolors.OKGREEN + f"\n{' '.join(efecnblt)}\n\n" + bcolors.ENDC)
    print(bcolors.UNDERLINE + f"{' '.join(alphabet)}\n" + bcolors.ENDC)
    print(bcolors.OKBLUE + f"\t\t{' '.join(screen)}" + bcolors.ENDC)

    if counter ==6:
        print(bcolors.OKCYAN + hangman[0] + bcolors.ENDC)
    if counter==5:
        print(bcolors.OKCYAN + hangman[1] + bcolors.ENDC)
    if counter==4:
        print(bcolors.OKCYAN + hangman[2] + bcolors.ENDC)
    if counter==3:
        print(bcolors.OKCYAN + hangman[3] + bcolors.ENDC)
    if counter==2:
        print(bcolors.OKCYAN + hangman[4] + bcolors.ENDC)
    if counter == 1:
        print(bcolors.OKCYAN + hangman[5] + bcolors.ENDC)

    if counter == 0:
        print(bcolors.OKCYAN + hangman[6] + bcolors.ENDC)
        game_over = True
        print(bcolors.FAIL + f"\n\n-------YOU LOST!--------\n" + bcolors.ENDC)
        print(bcolors.FAIL + f"The answer was --->  " + bcolors.ENDC + bcolors.OKGREEN + f"{chosen_word}\n" + bcolors.ENDC)

    if "_" not in screen:
        game_over = True
        print(bcolors.HEADER+ "\n\nCongratulations!\nYOU WON THE GAME :)\n" + bcolors.ENDC)