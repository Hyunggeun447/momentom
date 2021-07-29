n=int(input())

n=((n//10)+(n%10)*10)*2
if n>=100:
  n=n-100
print(n)
if n>50:
  print("OH MY GOD")

else:
  print("GOOD")