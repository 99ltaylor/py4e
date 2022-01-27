requested_file = input('Enter a file name: ')

def searching(requested_file):
  if requested_file == 'na na boo boo':
      print("NA NA BOO BOO TO YOU - You have been punk'd!")
  else:
      requested_file = open(requested_file)
      count = 0
      running_confidence_level = 0
      for line in requested_file:
        if line.startswith('X-DSPAM-Confidence:'):
          colonpos = line.find(':')
          position_as_integer = int(colonpos+1)
          extract = line[position_as_integer:]
          floated = float(extract)
          # print(floated)
          running_confidence_level = running_confidence_level + floated
          count += 1
          # print(count)
          # print(running_confidence_level / count)
          average_spam_confidence_level = (running_confidence_level / count)
      print('Average spam confidence:',average_spam_confidence_level)

searching(requested_file)
