def checkNumber(arr):
  print("Given list is ", arr)   
  for i in range(len(arr)):
    if arr[0] == arr[len(arr)-1]:
      return True
    else:
      return False     
arr = [10, 20, 30, 40, 10]  
print("Result is", checkNumber(arr))