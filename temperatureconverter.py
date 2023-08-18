def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

if __name__ == "__main__":
    print("Temperature Unit Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")

    choice = int(input("Enter your choice: "))
    temperature = float(input("Enter temperature: "))

    if choice == 1:
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result}°F")
    elif choice == 2:
        result = celsius_to_kelvin(temperature)
        print(f"{temperature}°C is equal to {result} K")
    elif choice == 3:
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result}°C")
    elif choice == 4:
        result = fahrenheit_to_kelvin(temperature)
        print(f"{temperature}°F is equal to {result} K")
    elif choice == 5:
        result = kelvin_to_celsius(temperature)
        print(f"{temperature} K is equal to {result}°C")
    elif choice == 6:
        result = kelvin_to_fahrenheit(temperature)
        print(f"{temperature} K is equal to {result}°F")
    else:
        print("Invalid choice")
