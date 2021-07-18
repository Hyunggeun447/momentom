n=int(input())
nums1 = [int(x) for x in input().split()]
nums2 = sorted(nums1)
nums3 = sorted(nums1, reverse = True)

if nums1 == nums2 :
  print("오름차순")
elif nums1 == nums3:
  print("내림차순")
else:
  print("섞임")