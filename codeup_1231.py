n=input()

for i in range (0,len(n)):

  if (n[i]=='+'):
    num1=int(n[:i])
    num2=int(n[i+1:])
    print(num1+num2)

  elif n[i]=="-":
    num1=int(n[:i])
    num2=int(n[i+1:])
    print(num1-num2)

  elif n[i]=="*":
    num1=int(n[:i])
    num2=int(n[i+1:])
    print(num1*num2)

  elif n[i]=="/":
    num1=int(n[:i])
    num2=int(n[i+1:])
    print("%.2f" %(num1/num2))