def removeChar(str, n):
  if(n >= len(str)): return "n must be less than the length of the string"
  return str[n:]
print(removeChar("pynative", 4))    