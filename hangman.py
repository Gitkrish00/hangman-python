import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

hangman_art = {
    0: ("    ",
        "    ",
        "    "),
    1: ("  o    ",
        "     ",
        "    "),
    2: ("  o  ",
        "  |  ",
        "    "),
    3: ("  o  ",
        " /|  ",
        "    "),
    4: ("  o  ",
        " /|\\ ",
        "    "),
    5: ("  o  ",
        " /|\\ ",
        "    \\"),
    6: ("  o  ",
        " /|\\ ",
        " / \\")
}

def choose_word(words):
    word = random.choice(words)
    return word

def letter_guess(word, guessed_letters):
    display = []
    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)
        

def user_guess():
    while True:
        user_guess = input("Enter a guess:").lower()
        if len(user_guess) == 1 and user_guess.isalpha():
            return user_guess
        else:
            print("Enter a valid guess.")
            continue
        

def update_scorlines(word, wrong_guess, user_guess, guessed_letters):
    if user_guess in word:
        guessed_letters.add(user_guess)
    else:
        wrong_guess += 1
    return guessed_letters, wrong_guess



def main():
    word = choose_word(words)
    wrong_guess = 0
    guessed_letters = set()

    print("Welcome to hangman")
    while wrong_guess < 6:
        for line in hangman_art[wrong_guess]:
            print(line)

        display = letter_guess(word, guessed_letters)
        print("Word:", display)

                        
        if "_" not in display:
            print("Congrats you win the game")
            break

        guess = user_guess()
        guessed_letters, wrong_guess = update_scorlines(word, wrong_guess, guess, guessed_letters)
 
    else:
        print("You loose the game")
        for line in hangman_art[6]:
                print(line)
        print(f"The words was {word}")
main()

