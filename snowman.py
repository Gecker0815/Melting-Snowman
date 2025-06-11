import random
   
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def play_game():
    """
    Starts the word guessing game 'Snowman Meltdown'.
    
    The player attempts to guess letters in a secret word within four mistakes.
    Correctly guessed letters are displayed, and incorrect guesses reduce available tries.
    """
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    guessed_letters = []
    mistakes = 0
    max_mistakes = 4

    while True:
        guess = input("Guess a letter: ").lower()
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

            print(f"You have {max_mistakes - mistakes} more tries.")

        if guessed_letters:
            print("Correct letters: " + " ".join(f'"{letter}"' for letter in guessed_letters))

if __name__ == "__main__":
    play_game()