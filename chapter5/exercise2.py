num = 0
tot = 0.0
values = [0]

while True :
  sval = input('Enter a number: ')
  if sval == 'done' :
      break
  try:
    fval = float(sval)
  except:
      print('Invalid input')
      continue
      # print (fval)
  num = num + 1
  tot = tot + fval
  values.append(fval)
  print(values)

print('ALL DONE')
x = min(values)
y = max(values)
print(tot,num,x,y)
