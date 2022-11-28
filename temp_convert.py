#!/usr/bin/env python3
# Created by: Lloyd Najac
# Date: Nov. 28, 2022
# This program converts the entered temperature
# in Celsius to Fahrenheit.

def calculate_fahrenheit():
    # gets temperature in celsius from the user
    temp_c_string = input("Enter the temperature (°C): ")
    print("")
    try:
        # converts user input to a float
        # so that it accepts decimal
        temp_c_float = float(temp_c_string)
        # calculates the fahrenheit of user input
        temp_f = (9 / 5) * temp_c_float + 32
        print("{:,.2f}°C is equal to {:,.2f}°F".format(temp_c_float, temp_f))
 
    # checks if the number is a string
    except Exception:
        print("{} is not a number.".format(temp_c_string))
 
 
def main():
    calculate_fahrenheit()
 
 
if __name__ == "__main__":
    main()
