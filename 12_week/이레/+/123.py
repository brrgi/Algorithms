import bisect
nums=[1,1,1,1,1,2,2,2,5,5,5,5,5,6,6,6,6,6]
n=5

print(bisect.bisect_left(nums, n))
print(bisect.bisect_right(nums, n))



nums.insert(8,1010)

print(nums)