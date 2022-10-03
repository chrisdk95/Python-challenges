#calculate the length of a list and then append the value to the end of the list
def append_size(lst):
  lst.append(len(lst))
  return lst

#Test
print(append_size([23, 42, 108]))
