#To Write A Program to Calculate How Many Total Digits are there in a number entered by the user

num = 78945
count = 0

while num != 0:
    num = num // 10
    count = count + 1

print("Number of digits : ", count)