import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    max_mistakes = len(STAGES) - 1
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)

    wrong_letters = [l for l in guessed_letters if l not in secret_word]
    print("Wrong guesses:", ", ".join(wrong_letters) if wrong_letters else "none")
    print(f"Mistakes: {mistakes}/{max_mistakes}")
    print("=" * 30)
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

        while True:
            guess = input("Guess a letter: ").lower()

            if len(guess) == 1 and guess.isalpha():
                break

        if guess not in guessed_letters:
            guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1

        # Prüfen, ob das Wort komplett erraten wurde
        if all(letter in guessed_letters for letter in secret_word):
            print("You saved the snowman!")
            break

        # Prüfen, ob das Fehlerlimit erreicht ist
        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"The snowman has melted! \n The word was: {secret_word}")
            break

    print("\n")

    play_again = input("Play again (y/n): ").lower()

    if play_again == "y":
        play_game()


if __name__ == "__main__":
    play_game()