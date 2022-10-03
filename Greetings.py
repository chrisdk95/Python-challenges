#to greet everyone
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list
# or
# def add_greetings(names):
#   list = []
#   for name in names:
#     list.append("Hello, " + name)
#   return list
#Test
print(add_greetings(["Owen", "Max", "Sophie"]))
