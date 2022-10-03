# condition will always be false no matter what value you pass into it
def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False
# Test
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
