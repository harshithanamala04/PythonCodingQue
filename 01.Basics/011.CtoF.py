# Convert a Celsius temperature to Fahrenheit using F = C × 9 / 5 + 32. Try 0°C and 25°C.
def cslToFah(c):
    f = c * 9 / 5 + 32
    return f

celsius = int(input("Enter temp in celsius:"))
print(cslToFah(celsius))