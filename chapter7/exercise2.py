requested_file = input('Enter a file name: ')
requested_file = open(requested_file)

def searching(requested_file):
  for line in requested_file:
    if line.startswith('X-DSPAM-Confidence:'):
      count = 0
      colonpos = line.find(':')
      position_as_integer = int(colonpos+1)
      extract = line[position_as_integer:]
      floated = float(extract)
      print(floated)
      count = count + 1

# NEXT:
# find sum of floats that are currently printing
# print number of times they occur
# then print out average spam confidence

searching(requested_file)
print(count)
