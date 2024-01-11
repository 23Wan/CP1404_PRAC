from silver_service_taxi import *

taxi = SilverServiceTaxi('Hummer', 100, 2)
taxi.drive(18)
print(taxi)
print(f'${taxi.get_fare()}')