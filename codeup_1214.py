a,b=map(int, input().split())

if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
  print(31)
elif b==4 or b==6 or b==9 or b==11:
  print(30)
elif b==2:
  if a%400==0 or (a%4==0 and a%100!=0):
    print(29)
  else:
    print(28)