import random

word = ("apple", "orange", "banana", "coconut", "pineapple")

# hangman ascii art
hangman_art = {0 : ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\"),}

def display_man(wrong_answer):
    print("**********************")
    for line in hangman_art[wrong_answer]:
        print(line)
    print("**********************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))
    
def main():
    answer = random.choice(word)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1:
            print("Invalid input.")
            continue
        elif guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess



if __name__ == "__main__":
    main()