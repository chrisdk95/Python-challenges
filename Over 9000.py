#function that stops when sum is over 9000
def over_nine_thousand(lst):
  number = 0
  for num in lst:
    number += num
    if number > 9000:
      break
  return number
#Test
print(over_nine_thousand([8000, 900, 120, 5000]))
