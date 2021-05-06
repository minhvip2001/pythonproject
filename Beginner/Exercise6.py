def findNumber(arr):
  print("Given list is ", arr)   
  print("Divisible of 5 in a list")
  for i in arr:
    if (i % 5 == 0):
      print(i)
arr = [10, 20, 33, 46, 55]
findNumber(arr)