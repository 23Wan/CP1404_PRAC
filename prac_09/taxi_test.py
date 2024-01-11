from prac_09 import taxi
taxi = taxi('Prius 1', 100)
taxi.drive(40)
fare = taxi.get_fare()
print(f'{taxi} \n{fare}')
taxi.start_fare()
taxi.drive(100)
new_fare = taxi.get_fare()
print(f'{taxi} \n${fare}')