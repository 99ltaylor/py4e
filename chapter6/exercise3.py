word = input('Please enter something: ')

def count(word):
  count = 0
  for letter in word:
    count = count + 1
  print(count)

count(word)
