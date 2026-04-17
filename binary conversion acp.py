# Decimal to Binary Conversion

num = int(input(" Enter a decimal humber : "))

# Special case for 0
if num == 0:
    print("Binary number is: 0")
else:
    binary = " "

    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    print("Binary number is : ", binary)