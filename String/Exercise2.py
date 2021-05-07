def insertMiddle(s1, s2):
  middleIndex = int(len(s1)/2)
  print("Original Strings are", s1, s2)
  middleInsert = s1[:middleIndex:] + s2 + s1[middleIndex:]
  print("After appending new string in middle", middleInsert)
insertMiddle('Ault', 'Kelly')  
