# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(celsius,"°C is equal to", fahrenheit,"°F.")
