a,b=input().split()
a=int(a)
n=int(b)



def how_many(a,n,k):
  arr=[0]*(n+10)
  arr[k]=1
  x=0
 

  for i in range(10,n+1):
    arr[i]=arr[i//10]+arr[i%10]

  
  for i in range(a,n+1):
    x+=arr[i]
    

  

  
    
   
        
  return x






print(how_many(a,n,1))