#find the indices in two equally sized lists where the numbers match.
def same_values(lst1, lst2):
  new_list = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_list.append(index)
  return new_list

#Test
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
