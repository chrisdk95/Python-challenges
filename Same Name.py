# a program that checks different names and determines if they are equal.
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False
# Test
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False