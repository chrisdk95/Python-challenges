# testing if a number falls within a certain range.
def in_range(num, lower, upper):
  if (num >= lower) & (num<= upper):
    return True
  else:
    return False

print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
 #should print False
