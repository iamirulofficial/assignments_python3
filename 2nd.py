cars = 100
space_in_cars = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
name = 'Ami'
carpool_capacity = cars_driven * space_in_cars
average_passenger_in_a_car = passengers / cars_driven
print("There are", cars, "cars available")
print("There are only",drivers,"drivers available. So total ",cars_driven,"would ready to go. Total Capacity per car is",space_in_cars,"So total number of passengers are ", carpool_capacity,"hence Avarage passenger per car is ",average_passenger_in_a_car,"nos")
print(f"Number of cars {cars}")
print(f"One of the driver is {name}.")
total = cars + space_in_cars + drivers + passengers
print(f"If I add {cars}, {space_in_cars}, {drivers}, {passengers} I will get {total}")
