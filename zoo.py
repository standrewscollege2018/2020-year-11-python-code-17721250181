MIN_AGE = 16
MIN_WEIGHT = 50

age = int(input("Enter your age:"))
weight = int(input("Enter your weight:"))

if age >= MIN_AGE and weight >= MIN_WEIGHT :
    print("You are eligible")
else :
    print("You are not eligible")