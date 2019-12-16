from postcode_return_task import *

print("///Welcome!///")

while True:
    print('Please choose from the options below:')
    print("1: Get NHS location for three postcodes")
    user_input = input("Please enter the option number...")

    if user_input == '1':
        nhs_location_getter()