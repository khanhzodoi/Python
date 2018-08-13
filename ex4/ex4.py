# 100 cars
cars = 100
# car's space is 4.0
space_in_car = 4.0
# 30 divers
drivers = 30
#90 passengers
passengers = 90
#cars_not_driven is the numer of cars that are not driven by any drivers
cars_not_driven = cars - drivers
#cars_driven is the number of drivers
cars_driven = drivers
#carpool_capacity is the number of all spaces in driven_car
carpool_capacity = cars_driven * space_in_car
#average_passengers_per_car is the average passengers to put in each driven_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars , "cars availble.")
print("There are only", drivers, "drivers availble.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")
