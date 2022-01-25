word = input('Give me a word, please:')
letter_to_find = input('Give me a letter to find, please:')

def is_it_included(word,letter_to_find):
  number_of_times = word.count(letter_to_find)
  print(number_of_times)

is_it_included(word,letter_to_find)
