#Asked for how many number will do the mean
number=int(input("How many number do you want to input? "))

#set the list
num_list=[]

#asked for numbers
i=int(0)
for i in range(number):
    num_list.append(int(input("Enter a number: ")))
    
#out put numbers
print("You've entered these numbers")
for i in range(number):
    print(num_list[i])
#calculate the mean
print("The mean is {}".format(sum(num_list)/number))