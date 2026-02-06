# List
fruits = list(["Banana", "Apple", "Orange"])
print(fruits)

# Add / Delete last fruit
fruits.append("Mango")
fruit = fruits.pop()
print("--------")
print(fruit)
print("Apple" in fruits)


# Merge lists
fruits2 = list(["Watermelon", "Pineapple"])
fruits.extend(fruits2)
print("--------")
print(fruits)

# Reverse list
fruits.reverse()
print("--------")
print(fruits)

# Sort list
fruits.sort()
print("--------")
print(fruits)

# Numbers
numbers = list(range(1, 11))
print("--------")
print(numbers)
print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(numbers[0:5])

# Find
users = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25}
]
user = next((user for user in users if user["name"] == "Alice"), None)
print("--------")
print(user)
print(user["age"])
