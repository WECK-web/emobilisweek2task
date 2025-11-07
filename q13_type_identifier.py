# q13_type_identifier.py

value = input("Enter any value: ")

# Try to determine type
if value.isdigit():
    cast_value = int(value)
elif value.replace('.', '', 1).isdigit():
    cast_value = float(value)
else:
    cast_value = value

print("Raw input:", value)
print("Data type:", type(cast_value))
