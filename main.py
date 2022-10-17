import random
import hangman_art
import hangman_words

print(f'{hangman_art.logo}\n\n')

lives = 6
chosen_word = random.choice(hangman_words.word_list)
guess = input('Guess a letter: \n').lower()

#List with underscore strings based on length of chosen_word
display = []
for underscore in chosen_word:
  display.append("_")

#Loop for blanks with letters to compare and replace
while display.count("_") != 0 and lives > 0:  
  for letter in range(len(chosen_word)):
    if chosen_word[letter] == guess:
      display[letter] = chosen_word[letter]
  if guess not in display:
    lives -= 1
  print(f'{hangman_art.stages[lives]}')
  print(f'\nThe word:\n{display}')
  #No need for more input if blanks are filled
  if display.count("_") != 0 and lives > 0:
    guess = input('\nGuess a letter:\n').lower()
  
if lives == 0:
  print("\nYou lost.\n")
else:
  print("\nYou won.\n")