#find the maximum number in a list of numbers
def max_num(nums):
  maximum = nums[0]
  for num in nums:
    if num > maximum:
      maximum = num
  return maximum

#Test
print(max_num([50, -10, 0, 75, 20]))
