# win_percentage function
def win_percentage(wins, losses):
  total = wins + losses
  win_percentage = (wins/total) * 100
  return win_percentage
# Test
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100
