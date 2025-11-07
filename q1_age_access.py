# q1_age_access.py

age = int(input("Enter your age: "))

if age > 18:
    print("Access granted — you receive a complimentary drink!")
elif age >= 16 and age <= 18:
    print("Access granted — enjoy a juice pack!")
else:
    print("Access denied — you’re too young!")
# This program checks the user's age and grants access based on the age criteria.