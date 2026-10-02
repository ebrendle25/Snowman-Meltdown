import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if guess in secret_word:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
        else:
            mistakes += 1

        # Prüfen, ob das Wort komplett erraten wurde
        if all(letter in guessed_letters for letter in secret_word):
            print("Du hast den Schneemann gerettet!")
            break

        # Prüfen, ob das Fehlerlimit erreicht ist
        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Der Schneemann ist geschmolzen! \n Das Wort war: {secret_word}")
            break



if __name__ == "__main__":
    play_game()