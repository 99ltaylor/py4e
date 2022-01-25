str = 'X-DSPAM-Confidence:0.8475'

def find_then_extract_and_then_float(str):
  colonpos = str.find(':')
  position_as_integer = int(colonpos+1)
  print(position_as_integer)
  extract = str[position_as_integer:]
  floated = float(extract)
  print(floated)

find_then_extract_and_then_float(str)
