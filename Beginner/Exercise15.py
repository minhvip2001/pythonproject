def exponent(base, exp):
  result = 1
  count = 1
  while exp > 0:
    result = result * base
    exp = exp - 1
  print(base, "raises to the power of", exp, "is: ", result, count)

exponent(5, 4) 