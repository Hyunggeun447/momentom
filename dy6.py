a,b,k=input().split()
a=int(a)
b=int(b)
k=int(k)


def how_many(a,b,k):
  arr=[0]*(b+10)
  arr[k]=1
  x=0
 

  for i in range(10,b+1):
    arr[i]=arr[i//10]+arr[i%10]
    if i>=a:
      x+=arr[i]

  
  if k>=a and b>=k:
    x=x+1
    
    

  

  
    
   
        
  return x






print(how_many(a,b,k))