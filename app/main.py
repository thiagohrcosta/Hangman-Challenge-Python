import random

word_list = ["aardvark", "baboon", "camel"]

user_life = 6

selected_word = random.choice(word_list)

word_blank_spaces = len(selected_word)

array_of_answer = []

for space in range(0, word_blank_spaces):
  array_of_answer.append("_")

while user_life > 0 and "_" in array_of_answer:
  print(array_of_answer)
  user_choice = input("Guess a letter: ")

  for index, letter in enumerate(selected_word):
    if user_choice.lower() == letter.lower():
      array_of_answer[index] = letter

  if user_choice.lower() not in selected_word.lower():
    user_life -= 1
    print(f"You have {user_life} lives left")
    