import math


# Asks for to hit and armor class
def get_val(question):
    val = int(input(question))

    while not check_valid_num(val):
        print("\n" + "Please enter a number: " + "\n")
        val = input(question)

    return val


# Returns true if given int
# Returns false otherwise
def check_valid_num(val):
    if type(val) != int:
        return False
    else:
        return True


# returns number with one only one decimal place
def truncate_one_decimal(num):
    num *= 10
    num = math.trunc(float(num))
    num /= 10
    return num


# calculates the probability of hitting given a "to hit"
# modifier and an armor class
def calculate_percentage(bonus, goal):
    top = 20 - (goal - bonus) + 1
    return float(top) / 20 * 100


# calculates the probability of hitting with advantage
def calculate_advantage(bonus, goal):
    hitTop = 20 - (goal - bonus) + 1
    noHitTop = 20 - hitTop
    probNot = float(noHitTop) ** 2 / 400
    return (1 - probNot) * 100


# calculates the probability of hitting with disadvantage
def calculate_disadvantage(bonus, goal):
    hitTop = 20 - (goal - bonus) + 1
    probYes = float(hitTop) ** 2 / 400
    return probYes * 100


# calculates the probability of hitting when you have elven accuracy active
def calculate_elven_accuracy(bonus, goal):
    hitTop = 20 - (goal - bonus) + 1
    noHitTop = 20 - hitTop
    probNot = float(noHitTop) ** 3 / (20 ** 3)
    return (1 - probNot) * 100


toHit = get_val("What is your \"to hit\" modifier? ")
armorClass = get_val("What is the AC of the enemy? ")

percentage = calculate_percentage(toHit, armorClass)
advPercentage = calculate_advantage(toHit, armorClass)
disPercentage = calculate_disadvantage(toHit, armorClass)
elvenAccuracy = calculate_elven_accuracy(toHit, armorClass)

print("You have a " + str(int(percentage)) + "% chance of hitting")
print("You have a " + str(truncate_one_decimal(advPercentage)) + "% chance of hitting with advantage")
print("You have a " + str(truncate_one_decimal(disPercentage)) + "% chance of hitting with disadvantage")
print("You have a " + str(truncate_one_decimal(elvenAccuracy)) + "% chance of hitting with elven accuracy")
