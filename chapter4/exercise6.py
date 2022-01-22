
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

def computepay(hours,rate):
  try:
    fh = float(hours)
    fr = float(rate)
    if fh > 40 :
      print("Overtime")
      xp = 40 * fr + ((fh - 40.0)* (fr * 1.5))
      print("Pay:", xp)
    else:
      print("Regular")
      xp = fh * fr
      print("Pay:", xp)
  except:
    print('Please enter numeric input')

computepay(hours,rate)
