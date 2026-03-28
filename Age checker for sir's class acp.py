# Program to check eligibility for enrollment based on age

age = int(input("Enter student's age: "))

if age >= 10:
    if age <= 20:
        print("Student is eligible to enroll in the class.")
    else:
        print("Student is NOT eligible (age is more than 20).")
else:
    print("Student is NOT eligible (age is less than 10).")