import random
import hangman_words
import hangman_art

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
lives = 6
word_length = len(chosen_word)
placeholder = "_" * word_length
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter")
        continue

    guessed_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word, you lose a life")

    display = ""
    for letter in chosen_word:
        if letter in correct_letters or letter == guess:
            display += letter
            if letter == guess:
                correct_letters.append(guess)
        else:
            display += "_"

    print(hangman_art.stages[lives])
    print("Word to guess: " + display)

    if lives == 0:
        game_over = True
        print("***********************YOU LOSE**********************")
        print(f"The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")