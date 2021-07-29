a,b=map(int, input().split())

if a>=b and a%b==0:
  print("{}*{}={}".format(b,a//b,a))
elif a<b and b%a==0:
  print("{}*{}={}".format(a,b//a,b))
else:
  print("none")