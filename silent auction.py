#setting bidding item and reserve price
BIDDING_ITEM=input("What is the auction for? ")
input_check=True
while input_check:
    try:
        RESERVE_PRICE=int(input("What is the reserve price? "))
        input_check=False
    except:
        print("The reserve price must be a number")

#change line
print()

#print start
print("The auction for the sloth has started! (Type 'finish' as name to finish the programe)")

#change line
print()

#set highest bid
highest_bid=float(0)

keep_asking=True
while keep_asking:
    #input name
    name=input("What is your name? ")
    #if read finish then stop the programe
    if name=="finish":
        keep_asking=False
    else:
        #input bid
        input_check=True
        while input_check:
            try:
                read_bid=float(input("What is your bid? "))
                input_check=False
            except:
                print("The bid must be a number")
        #chece the bid is higher than the highest or not
        if read_bid<=highest_bid:
            print("Please enter a higher bid")
        else:
            highest_bid=read_bid
        #output the highestbid
        print("Highest bid so far is {} with ${}".format(name,highest_bid))
        #change line
        print()
        
#The end
print()
if highest_bid>=RESERVE_PRICE:
    print("The auction for the {} finished with a bid of ${}.".format(BIDDING_ITEM,highest_bid))
else:
    print("The highest bid is less than the reverse price.")