#Program to calculate power using a loop

#Taking input from the user
base = int(input("Enter the base number : "))
power = int(input("Enter the power : "))

result = 1

#Using for loop to calculate power
for i in range(power) :
    result = result * base

#Display result
print("Result: " , result)