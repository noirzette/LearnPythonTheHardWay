# The number of cars
cars =  100

# How many people can fit in the car
space_in_a_car = 4.0 

#How many drivers there are
drivers = 30

#How many passengers there are
passengers = 90

#How many cars aren't being driven
cars_not_driven = cars - drivers

#How many cars are being driven
cars_driven = drivers

#How many people can be transported
carpool_capacity = cars_driven * space_in_a_car

#Average number of passengers per car
average_passengers_per_car = passengers / cars_not_driven


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")

print("There are %s cars available" % cars)
print("There are only %s drivers available" % drivers)

print(f"There are {cars} cars available")
print(f"There are only {drivers} drivers available")