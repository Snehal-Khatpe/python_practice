# Wite a program to calculate bill for pizza
""" Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want (S/M/L): ") 
add_pepperoni = input("Do you want pepperoni? (Y or N): ") 
extra_cheese = input("Do you want extra cheese? (Y or N): ") 

base_price = 0

#calculation for small pizza:
if size == "S":
  base_price += 15
  if add_pepperoni=="Y":
    base_price += 2
  if extra_cheese == "Y":
    base_price += 1
  print(f"Your final bill is: ${base_price}")

#calculation for medium size pizza
elif size=="M":
  base_price += 20
  if add_pepperoni=="Y":
    base_price+=3
  if extra_cheese=="Y":
    base_price+=1
  print(f"Your final bill is: ${base_price}")

elif size=="L":
  base_price += 25
  if add_pepperoni=="Y":
    base_price+=3
  if extra_cheese=="Y":
    base_price+=1
  print(f"Your final bill is: ${base_price}")