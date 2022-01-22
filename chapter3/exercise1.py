sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

if fh > 40 :
  print("Overtime")
  xp = 40 * fr + ((fh - 40.0)* (fr * 1.5))
else:
  print("Regular")
  xp = fh * fr
print("Pay:", xp)
