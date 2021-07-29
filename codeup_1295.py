n=input()

for i in n:
  if 122>=ord(i)>=97:
    print(chr(ord(i)-32),end="")
  elif 65<=ord(i)<=90:
    print(chr(ord(i)+32),end="")
  else:
    print(i,end="")