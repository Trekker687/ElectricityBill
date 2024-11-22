unit = int(input("Enter the units"))

if unit <= 50:
    amount = unit*2.60
    tax = 25

elif unit>50 and unit <= 100:
    amount = unit*3.25
    tax = 35

elif unit>100 and unit <= 200:
    amount = unit*8.35
    tax = 45

else:
    amount = unit*10.15
    tax = 55

total = amount + tax
print("The bill is", total)