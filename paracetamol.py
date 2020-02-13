AGE_BOUNDARY=12
CHILD_DOSAGE=10

age=int(input("How old are you?  "))
weight=int(input("What is your weight  "))

if age<0 or age>146:
    print("Impossible age")
elif weight<0 or weight>635:
    print("Impossible weight")
elif age<AGE_BOUNDARY:
    print("Need {}mg".format(NEED_PERKG*weight))
else:
    print("Need 2*500mg")
