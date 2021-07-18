a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

arr=[a,b,c,d,e]

"""
max_value = arr[0]
for i in range(1, len(arr)):
    if max_value < arr[i]:
        max_value= arr[i]
 

min_value = arr[0]
for i in range(1, len(arr)):
    if max_value > arr[i] :
        min_value= arr[i]
        
"""
max_value=max(arr)
min_value=min(arr)
print(max_value)
print(min_value)