# building user input
city_flight_display = "Enter city name: \n"
city_flight_options= ['ENG', 'LAG', 'KAD', 'PHC', 'MAD', 'JOS']
#use enumerate to itemize the options
for index, item in enumerate(city_flight_options, start=1):
    city_flight_display += f'{index}: {item}\n'

city_flight_display += f"select the correct city no: "

#here a while loop is used to allow the user to try until the right option is selected
#the enumertae made it possible for the user to select the number rather than typing the whole destination name
city_flight = 0

while city_flight not in range(1,len(city_flight_options)+1):
    city_flight = int(input(city_flight_display))

num_nights = int(input("Enter no of nights: "))
rental_days = int(input("Car rentals(days): "))
price = {
    "ENG": 40,
    "LAG": 67,
    "KAD": 60,
    "PHC": 32,
    "MAD": 89,
    "JOS": 70   
}

#hotel cost depends on the cost per day
def hotel_cost(num_nights=num_nights,hotel_charge_per_night=10):
    hotel_cost = num_nights * hotel_charge_per_night
    return hotel_cost

#plane cost
def plane_cost(city_flight=city_flight):
    #use enumerate to get the item name
     plane_cost = [(price[item],item) for index, item in enumerate(city_flight_options,start=1) if index == city_flight]
     return plane_cost
    
#car rentals
def car_rental(rental_days=rental_days,crental_per_day=5):
    return rental_days * crental_per_day
    
    
#holiday_cost accepts function as arg
def holiday_cost(car_rental,hotel_cost,plane_cost):
    holiday_cost=int(car_rental())+int(hotel_cost())+int(plane_cost()[0][0])
    return holiday_cost
    
print(f'Hotel Cost for {num_nights} =>${hotel_cost()}')
print(f'Plane Fare for {plane_cost()[0][1]} =>${plane_cost()[0][0]}')

print(f'Care rental cost for {rental_days}days =>${car_rental()}')
print(f"Total holiday cost including hotel,plane and rental cost => ${holiday_cost(car_rental,hotel_cost,plane_cost)}")