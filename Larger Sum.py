#calculating which list of two inputs has the larger sum
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for lst in lst1:
    sum1 += lst
  for lst in lst2:
    sum2 += lst
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

#Test
print(larger_sum([1, 9, 5], [2, 3, 7]))
