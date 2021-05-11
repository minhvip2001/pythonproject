def mergeList(lis1, list2):
  print("list1 =", list1)
  print("list2 =", list2)
  list3 = []
  for i in list1:
    if(i % 2 == 1):
      list3.append(i)
  for i in list2:
     if(i % 2 == 0):
      list3.append(i)
  return list3    
list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]          
print("Result List is", mergeList(list1, list2))