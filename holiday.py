print("Please select holiday destination from Berlin, Malaga or Kuala Lumpur.")
city_flight = input("Enter flight destination : ").lower()  # get flight destination and convert to all lowercase

def plane_cost(city_flight):        # function to calculate flight cost
    
    while city_flight != "berlin" and city_flight != "kuala lumpur" and city_flight != "malaga":
        city_flight = input("There are no flights to that destination, please select Berlin, Malaga or Kuala Lumpur: ").lower()
        
    if city_flight == "berlin":                 # if user input isn't a recognised city, prompt again for input
        flight_cost = 70
    elif city_flight == "kuala lumpur":         # set value based on input
        flight_cost = 750
    elif city_flight == "malaga":
        flight_cost = 40

    return(flight_cost)           
plane_cost = (plane_cost(city_flight))  # variable to store value of plane_cost function for later use

def hotel_cost(num_nights):             # function to calculate hotel price
    if city_flight == "berlin":
        night_cost = 100
    elif city_flight == "kuala lumpur":
        night_cost = 40
    elif city_flight == "malaga":
        night_cost = 50
    total_hotel = night_cost*num_nights

    return(total_hotel)

def car_rental(rental_days):        # function to calculate car rental cost
    day_rental = 0
    if city_flight == "berlin":
        day_rental = 30
    elif city_flight == "kuala lumpur":
        day_rental = 20
    elif city_flight == "malaga":
        day_rental = 25
    total_car = day_rental*rental_days

    return(total_car)
 
while True:     # get user input for number of nights to stay
    try:        # display error and prompt again if input is non numerical, 0 or more than 100
        num_nights = int(input("How many nights will you stay? "))
        break
    except ValueError:                  
        print("Please enter a number between 1 and 100.") 
while num_nights <1 or num_nights >100 :
    num_nights = int(input("Please enter between 1 and 100 nights: "))

while True:     # get user input for number of car rental days
    try:        # display error and prompt again if input is non numerical, 0 or more than num_nights
        rental_days = int(input("How many days to you require car rental? "))
        break
    except ValueError:
        print("Please enter a number between 1 and 100.") 
while rental_days <1 or rental_days >100 :
    rental_days = int(input("Please enter between 1 and 100 nights: "))
while rental_days > num_nights:
    rental_days = int(input(f"You have requested more days car rental than the holiday duration, please enter a number no more than {num_nights}: "))

car_rental = (car_rental(rental_days))  # variable to store car_rental value
hotel_cost = (hotel_cost(num_nights))   # variable to store hotel_cost value

holiday_cost = ""       # create empty variable for holiday_cost function

def holiday_cost(a, b, c):  # function to calculate the total holiday cost
    a = plane_cost
    b = hotel_cost
    c = car_rental
    x = a + b + c
    return(x)

holiday_cost = holiday_cost(plane_cost, hotel_cost, car_rental) # variable to store holiday_cost value

print(f"\nThe total cost for this holiday is {holiday_cost}.")  # display total and breakdown to user
print(f"Breakdown: \nFlights: {plane_cost} \nCar Rental: {car_rental} \nHotel: {hotel_cost}")