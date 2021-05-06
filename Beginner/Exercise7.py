def appearance(str, word):
  count = 0
  count = str.count(word)
  if(count == 0): print(word, "appeared", count, "time")
  elif(count < 2): print(word, "appeared", count, "time")
  else: print(word, "appeared", count ,"times")
str = "Emma is good developer. Emma is a writer"
word = "Emma"
appearance(str, word)