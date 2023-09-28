# create an empty list that will store user input
numbers = []
# create a variable that will note the number of input from the user 
count=0

#get input from the user
# in a while loop
while True:
    number = int(input("Enter a number or enter -1 to compute average: "))
    # if the input number is -1, exit the loop
    if number == -1:
        break
    # if the input number is not -1 , continue the computationis 
    else:
        # this counts the number of input
        count += 1
        # this stires/arranges the input in a list
        numbers.append(number)
# print the average of the list at the end of the computation       
print(f"the average of the numbers is : {sum(numbers)/count}")  
#print(count)      


