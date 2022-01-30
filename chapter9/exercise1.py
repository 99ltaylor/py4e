import_file = open('words.txt')

for line in import_file:
  words = line.split()
  vals = list(words.values())
  print(vals)

  # not complete
