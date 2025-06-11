import random
   
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
    """  
      ___  
     /___\\  
     (o o)  
     ( : )  
     ( : )  
    """,  # Stage 0: Full snowman
    """  
      ___  
     /___\\  
     (o o)  
     ( : )  
    """,  # Stage 1: Bottom part starts melting
    """  
      ___  
     /___\\  
     (o o)  
    """,  # Stage 2: Only the head remains
    """  
      ___  
     /___\\  
    """,  # Stage 3: Snowman completely melted
]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current state of the game, including the melting snowman and guessed letters."""
    print(STAGES[mistakes])

    revealed_word = "".join(letter if letter in guessed_letters else "_" for letter in secret_word)
    print(revealed_word)

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def play_game():
    """Starts the word guessing game 'Snowman Meltdown'."""
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    guessed_letters = []
    mistakes = 0
    max_mistakes = 4

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
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

        if set(secret_word) <= set(guessed_letters):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Game Won!")
            break

if __name__ == "__main__":
    play_game()