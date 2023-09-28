#creates an array for the customer order
order =[]
#accepts three customer fav food
while len(order) < 3:
    order.append(input("Order your fav. food: "))
#stores each order as a variable
item1,item2,item3 = order
#prints out the customer order
#print(f"Order Confirmation! You have Ordered \n {item1} \n {item2} \n {item3}")
print(f"Order Confirmation! You have Ordered:")
for i in order:
    print(i)