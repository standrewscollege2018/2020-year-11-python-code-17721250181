#age boundarys and Fees for different ages.
AGE_BOUNDRY_ONE=5
AGE_BOUNDRY_TWO=13
AGE_BOUNDRY_THREE=18
FEE_ONE="Free"
FEE_TWO="$7"
FEE_THREE="$9"
FEE_FOUR="$12"
FEE_STUDENT="$8"
#Is he/she a student?(0 no   1 yes)
STUDENT=int(0)

#Vars (input age)
age=int(input("How old are you  "))

#Is he/she a student?
if age>=AGE_BOUNDRY_TWO:
    STUDENT=int(input("Are you a student? (If you are, type '1'. If you are not, type '0')  "))

#main program
if age<0 or age>146:
    print("Inpossible age")
elif age<AGE_BOUNDRY_ONE:
    print("Your fee is {}".format(FEE_ONE))
elif age<AGE_BOUNDRY_TWO:
    print("Your fee is {}".format(FEE_TWO))
elif STUDENT==1:
    print("Your fee is {}".format(FEE_STUDENT))
elif age<AGE_BOUNDRY_THREE:
    print("Your fee is {}".format(FEE_THREE))
else:
    print("Your fee is {}".format(FEE_FOUR))