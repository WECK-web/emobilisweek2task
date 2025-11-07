# q9_favorite_fruits.py

colors = ["red", "green", "yellow"]
fruits = ["apple", "banana", "pear"]

count = 0
for color in colors:
    for fruit in fruits:
        print(f"{color} : {fruit}")
        count += 1

print(f"Total combinations: {count}")
# This program generates and displays all combinations of colors and fruits, along with the total count of combinations.