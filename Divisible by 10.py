# a function that determines whether or not a number is divisible by ten
def divisible_by_ten(num):
  if (num % 10 == 0):
    return True
  else:
    return False


# Tests

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False
