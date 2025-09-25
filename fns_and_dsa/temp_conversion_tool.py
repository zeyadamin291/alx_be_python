FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

try:
    temp = float(input("Enter the temperature to convert: "))
    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if choice == 'C':
        in_fehr = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {in_fehr}°F")
    elif choice == 'F':
        in_cel = convert_to_celsius(temp)
        print(f"{temp}°F is {in_cel}°C")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
