from english_words import get_english_words_set
from Hang_man_art import logo
from Hang_man_art import stages
import random

def is_letter(character):
    return character.isalpha() and len(character) == 1

# Get a set of English words
words_set = get_english_words_set(['web2'])
# Convert the set to a list
words_list = list(words_set)

# Randomly choose a word from word_list
chosen_word = random.choice(words_list)
chosen_word = chosen_word.lower()

# Generate an empty list to display each letter of the chosen_word
display = ["_" for _ in chosen_word]
lives = len(stages) - 1
# Game's UI
print(logo)
print("Welcome to the Hangman, Let's guess letters that are in this word: \n")
print(" ".join(display))
print("You have 6 chances before you are hang. Let's gooooooo")

print(stages[lives])

# Game's Logic
end_game = False
while not end_game:
    # Prompt to the user and ask them to guess a letter
    guess = input('\nGuess a letter: ').lower()
    if not is_letter(guess) and guess!= 'end':
        print("Please input only letter")
        continue
    if guess == 'end':
        end_game = True
        print("Game ended by user.")
        break

    if guess in display:
        print(f"You've already guessed {guess}. Try another letter.")
        continue

    # the guess letter is in the chosen word
    if guess in chosen_word:
        count = 0
        for i in range(len(chosen_word)):
          
            if guess == chosen_word[i]:
                display[i] = guess
                count+=1
        print(stages[lives])
        if count ==1:
            print(f"There is {count} '{guess}' in this word.")
        else:
            print(f"There are {count} '{guess}' in this word.")
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        print(stages[lives])
        if lives == 0:          
            print("You lose. The word was:", chosen_word)
            break

    # Print the display list
    print(" ".join(display))

    if "_" not in display:
        print("You've survived!")
        end_game = True
