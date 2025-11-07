# q15_nested_data_lookup.py

myFamily = {
    "father": {"name": "John", "year": 1985},
    "mother": {"name": "Jane", "year": 1990}
}

member = input("Enter 'father' or 'mother': ").lower()

if member in myFamily:
    info = myFamily[member]
    print(f"{member.capitalize()}'s name is {info['name']} and birth year is {info['year']}.")
else:
    print("Family member not found.")
# This program looks up and displays the name and birth year of a specified family member from a nested dictionary.