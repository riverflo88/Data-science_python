#list of cafe menu
cafe_menu = ["choco", "tea", "milk tea", "mucaca", "valento"]
#dictionary of stock
stock = {"choco":10,"tea":20, "milk tea":20, "mucaca":10, "valento":30}
#dictionary containing cafe_menu and their prices
price = {"choco":10,"tea":5, "milk tea":50, "mucaca": 10, "valento":60}
# list comprehension listing the total price of avaialble stock 
total_stock = sum([stock[menu] * price[menu] for menu in cafe_menu])
print(f'Price of total stock = ${total_stock}')   
