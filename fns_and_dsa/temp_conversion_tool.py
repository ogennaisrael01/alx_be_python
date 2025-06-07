CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def convert_temperature():
    """
        CONVERSION FUNCTION
    """
    tem_to_convert = input(f"Enter the temperature to convert: ")
    unit = input("Is this temperature in Fahrenheit or Celsius? (F/C): ")

    if unit.upper() == 'F':
        converted_temp = convert_to_celsius(float(tem_to_convert))
        print(f"{tem_to_convert}°F is {converted_temp}°C")  
    elif unit.upper() == 'C':
        converted_temp = convert_to_fahrenheit(float(tem_to_convert))
        print(f"{tem_to_convert}°C is {converted_temp}°F")
    else:
        print("Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius.")

def main():
    """
    Main function to run the temperature conversion tool.
    """
    print("Welcome to the Temperature Conversion Tool!")
    convert_temperature()

if __name__ == "__main__":
    main()
