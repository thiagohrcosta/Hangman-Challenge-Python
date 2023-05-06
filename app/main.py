import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

user_life = 6

selected_word = random.choice(word_list)

word_blank_spaces = len(selected_word)

array_of_answer = []

wrong_attempts = 0

for space in range(0, word_blank_spaces):
  array_of_answer.append("_")

while user_life > 0 and "_" in array_of_answer:
  print("-------------------")
  if user_life > 0:
    print(stages[int(user_life)])  
  
  print(array_of_answer)
  user_choice = input("Guess a letter: ")

  for index, letter in enumerate(selected_word):
    if user_choice.lower() == letter.lower():
      array_of_answer[index] = letter

  if user_choice.lower() not in selected_word.lower():
    user_life -= 1
    print(f"You have {user_life} lives left")

if user_life == 0 and "_" in array_of_answer:
  print(stages[0])
  print("You lose")
elif "_" not in array_of_answer:
  print("You win")

  


