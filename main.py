def sumador(n):
  rec = 0

  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
   for i in range (n+1):
     rec+=i
    
  return rec

num = int(input('Ingrese un numero natural\n'))
print(sumador(num))