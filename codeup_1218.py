a,b,c=map(int, input().split())
arr=[a,b,c]
arr.sort()


if arr[0]==arr[1]==arr[2]:
  print("정삼각형")
elif (arr[0]==arr[1] or arr[1]==arr[2] or arr[0]==arr[2]) and arr[0]+arr[1]>arr[2]:
  print("이등변삼각형")
elif arr[0]**2 + arr[1]**2 ==arr[2]**2:
  print("직각삼각형")
elif arr[0]+arr[1]>arr[2]:
  print("삼각형")
else:
  print("삼각형아님")