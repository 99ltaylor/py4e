score_string = input("Enter a score between 0.0 - 1.0")
try:
  score_float = float(score_string)
  if score_float >= 0.9:
    print("A")
  elif score_float >= 0.8:
    print("B")
  elif score_float >= 0.7:
    print("C")
  elif score_float >= 0.6:
    print("D")
  elif score_float < 0.6:
    print("F")
except:
    print("Bad score")
