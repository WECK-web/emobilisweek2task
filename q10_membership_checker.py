# q10_membership_checker.py

cars = ["jeep", "suv", "sedan"]
car = input("Enter a car name: ").lower()

if car in cars:
    print("We have that car type!")
else:
    print("Sorry, not available.")
