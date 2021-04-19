import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print("You threw " + str(dice1) + " and " + str(dice2) + ".")
total = int(dice1) + int(dice2)
print("The result is " + str(total) + ".")