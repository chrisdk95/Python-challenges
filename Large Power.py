#Tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. 
# large_power function here:
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False

# Tests
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
