from cs50 import get_float

while True:
    change_owed = get_float("Change Owed: ")
    if change_owed >= 0:
        break

change_owed_cents = round(change_owed * 100)

num_quarters = 0
num_dimes = 0
num_nickels = 0
num_pennies = 0

while change_owed_cents > 0:
    if change_owed_cents >= 25:
        change_owed_cents -= 25
        num_quarters += 1
    elif change_owed_cents >= 10:
        change_owed_cents -=10
        num_dimes += 1
    elif change_owed_cents >= 5:
        change_owed_cents -= 5
        num_nickels += 1
    else:
        change_owed_cents -= 1
        num_pennies =+ 1

print ("Quarters: ", num_quarters)
print ("Dimes: ", num_dimes)
print ("Nickels: ", num_nickels)
print ("Pennies: ", num_pennies)
