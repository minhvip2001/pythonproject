def reverse(num):
  original = num
  reverse = 0
  print("original number", num)
  while(num != 0):
    reminder = num % 10
    reverse = (reverse * 10) + reminder
    num = num // 10
  if(original == reverse):
    return True
  else:
    return False    
print("The original and reverse number is", "the" if reverse(121) else "not", "same")
print("The original and reverse number is", "the" if reverse(125) else "not", "same")

  