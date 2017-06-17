cars=100 # the variance cars is 100
space_in_a_car=4.0 # the variance apace_in_a_car is 4.0
drivers=30 # variance drivers is 30
passengers=90 # passengers is 90
cars_not_driven=cars-drivers
cars_driven=drivers
carspool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven


print "There are",cars,"cars avaliable."
print "There are only",drivers,"drivers avaliable."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carspool_capacity,"people today."
print "We have",passengers,"to carpllo today."
print "We need to put about",average_passengers_per_car,"in each car."
