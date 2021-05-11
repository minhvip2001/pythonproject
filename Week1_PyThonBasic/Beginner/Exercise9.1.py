def reversed_string(string):
    reverse = string[::-1]
    if string == reverse:
      return True
    else:
      return False

print(reversed_string("121"))