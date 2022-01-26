requested_file = input('Enter a file name: ')
requested_file = open(requested_file)

def capitalise_all_lines(requested_file):
  for line in requested_file:
    print(line.upper())

capitalise_all_lines(requested_file)
