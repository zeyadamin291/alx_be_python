FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

def convert_to_celsius(fahrenheit):
    fahrenheit *= FAHRENHEIT_TO_CELSIUS_FACTOR
    return fahrenheit

def convert_to_fahrenheit(celsius):
    celsius *= CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius


temp= int(input("Enter the temperature to convert: "))
choice = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').upper()
if choice == 'C':
    in_fehr =convert_to_fahrenheit(temp)
    print(f"{temp}°C is {in_fehr}°F")
elif choice == 'F':
    in_cel =convert_to_celsius(temp)
    print(f"{temp}°F is {in_cel}°C")