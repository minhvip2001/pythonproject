def getMiddleThreeChars(text):
  middleIndex = int(len(text) / 2)
  print("Original string is", text)
  middleThreeChar = text[middleIndex - 1:middleIndex + 2]
  print("Middle Three Char is", middleThreeChar)
getMiddleThreeChars("JhonDipPeta")
getMiddleThreeChars("Jasonay")