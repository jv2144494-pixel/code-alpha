import random

# List of 5 predefined words
words = ["python", "computer", "program", "college", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

# Game loop
while incorrect_guesses < max_guesses:

    # Display the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether guess is correct
    if guess in word:
        print("Correct guess! 👍")
    else:
        incorrect_guesses += 1
        print("Wrong guess! ❌")
        print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

else:
    print("\nGame Over! 😢")
    print("The word was:", word)