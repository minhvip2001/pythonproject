str1 = "PyNaTive"
lower = []
upper = []
for i in str1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
sorted_string = ''.join(lower + upper)
print(sorted_string)