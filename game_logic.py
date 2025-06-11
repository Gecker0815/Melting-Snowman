import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current state of the game, including the melting snowman and guessed letters."""
    print(ascii_art.STAGES[mistakes])

    revealed_word = "".join(letter if letter in guessed_letters else "_" for letter in secret_word)
    print(revealed_word)

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def get_single_character():
    """ Prompts the user for a single letter input and validates the entry."""
    while True:
        guess = input("Guess a letter: ").lower()

        if guess.isdigit() or len(guess) > 1:
            print("Your guess should be one letter!")
        else:
            return guess

def play_game():
    """Starts the word guessing game 'Snowman Meltdown'."""
    while True:        
        secret_word = get_random_word()
        print("Welcome to Snowman Meltdown!")
        #print("Secret word selected: " + secret_word)  # for testing, later remove this line

        guessed_letters = []
        mistakes = 0
        max_mistakes = 4

        while True:
            display_game_state(mistakes, secret_word, guessed_letters)
            guess = get_single_character()
            print(f"You guessed: {guess}")

            if guess in secret_word:
                if guess in guessed_letters:
                    print("You already guessed this letter.")
                else:
                    guessed_letters.append(guess)
            else:
                mistakes += 1
                if mistakes == max_mistakes:
                    print("Game over!")
                    break

            if set(secret_word) <= set(guessed_letters):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("Game Won!")
                break

        play_again = input("If you want to play another round (y/n): ").lower()

        if play_again != "y":
            break