# Exercise 12: Calculate income tax for the given income
#  by adhering to the below rules
income = 0
tax = 0
income = int(input("Input income: "))
if income <= 10000:
  tax = 0
elif income <= 20000:
  tax = (income - 10000) * 10 / 100   
else:
  tax = 0

  tax = 10000 * 10 / 100

  tax +=(income - 20000) * 20 / 100

print("Total tax to pay is:", tax)  

