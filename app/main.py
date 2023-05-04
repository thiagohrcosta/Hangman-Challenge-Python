import random

word_list = ["aardvark", "baboon", "camel"]

selected_word = random.choice(word_list)

word_blank_spaces = len(selected_word)

array_of_answer = []

for space in range(0, word_blank_spaces):
  array_of_answer.append("_")

print(array_of_answer)

user_choice = input("Guess a letter: ")

for index, letter in enumerate(selected_word):
  if user_choice.lower() == letter.lower():
    array_of_answer[index] = letter
  

print(array_of_answer)
