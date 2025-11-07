# q8_collection_sorter.py

numbers = [3, 15, 8, 22, 5, 18, 11]
count = 0

for num in numbers:
    if num <= 10:
        continue
    print(num)
    count += 1

print(f"Total numbers greater than 10: {count}")
