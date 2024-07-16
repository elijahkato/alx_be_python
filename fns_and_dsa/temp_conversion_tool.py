# Define global conversion factors
F_TO_C_FACTOR = 5 / 9
C_TO_F_FACTOR = 9 / 5

def f_to_c(f_temp):
    return (f_temp - 32) * F_TO_C_FACTOR

def c_to_f(c_temp):
    return (c_temp * C_TO_F_FACTOR) + 32

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = c_to_f(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = f_to_c(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
