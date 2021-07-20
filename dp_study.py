n=int(input())
arr=input().split()
for i in range(len(arr)):
    arr[i]=int(arr[i])


total1=[arr[0]]                    #y를 찾기위한 배열생성1
for i in range(1,n):
  total1.append(total1[i-1]+arr[i])


total2=[arr[n-1]]                  #x를 찾기위한 배열생성2
for i in range(1,n):
  total2.append(total2[i-1]+arr[n-i-1])

total1.reverse()            #최대값이 중복일경우 가장 큰 y값을 찾기위해
total2.reverse()            #최대값이 중복일경우 가장 작은 x값을 찾기위해

index1=total1.index(max(total1))
index2=total2.index(max(total2))

x=index2
y=n-1-index1

def atob_add(a,b,c):  # c[a]~c[b]까지의 합
  t=0
  for i in range(a,b+1):
    t=t+c[i]
  return t

'''
print("total1",end=" ")
print(total1)
print("total2",end=" ")
print(total2)
print("index1",end=" ")
print(index1)
print("index2",end=" ")
print(index2)
print("x",end=" ")
print(x)
print("y",end=" ")
print(y)

print(arr)

'''
print(atob_add(x,y,arr))