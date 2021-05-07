str1 = "P@#yn26at^&i5ve"
charCount = 0
digitCount = 0
symbolCount = 0
for i in str1:
  if i.isalpha():
    charCount += 1
  elif i.isnumeric():
    digitCount += 1
  else:
    symbolCount += 1
print("Chars = ", charCount)
print("Digits = ", digitCount)
print("Symbol = ", symbolCount)
