mark = float(input("What is your grade?")) # I use float because a mark may not be a int

if mark >= 90:   
    print ( "A" )
if mark >= 70 and mark < 90:
    print ( "B" )    
if mark >= 50 and mark < 70:
    print ( "C" )
if mark < 50:
    print ( "Fail" )