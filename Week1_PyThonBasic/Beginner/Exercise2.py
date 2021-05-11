def sumNumber(): 
  sum = 0
  prev = 0
  for i in range(10):  
    sum = prev + i
    print("Current Number ", i, "Previous ", prev, "Sum ", sum)
    prev = i
    # i = 0 => prev = 0
    # i = 1 => prev = 0
    # i = 2 => prev = 1
print("Printing current and previous number sum in a given range(10)")    
sumNumber()