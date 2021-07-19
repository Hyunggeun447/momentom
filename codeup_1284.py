import math

def is_prime_number(x):
  for i in range(2,1+int(math.sqrt(x))):
    if x%i ==0:
      return False
  
  return True



n=int(input())
i=2

while True:
  a=n//i
  b=n/i
  if i>(n/2):
    print("wrong number")
    break
  elif (a==b) and (is_prime_number(i) ==True) and (is_prime_number(b)==True):
    print(i,int(b))
    break
  else:
    i+=1