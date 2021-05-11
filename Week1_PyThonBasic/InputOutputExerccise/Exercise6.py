count = 0
with open("tester.txt", "r") as fp:
  lines = fp.readlines()
  count = len(lines)
with open("new.txt", "w") as fp:
  for line in lines:
    if(count == 3):
      count -= 1
      continue
    else:
      fp.write(line)
    count-=1    