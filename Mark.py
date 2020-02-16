mark = float(input("What is your grade?   Input your grade here: "))

if mark > 100 or mark < 0:
    print ( "ILLEGAL MARK !!!" )
elif mark >= 90:
    print ( "A" )
elif mark >= 70:
    print ( "B" )
elif mark >= 50:
    print ( "C" )
else: 
    print ( "Fail" )
    