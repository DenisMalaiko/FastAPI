# For
users = list([
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
])
count = 0

for user in users:
    if user["age"] > 30:
        continue
    count += 1
    print(user)

print("--------")
print(count)

user = next(user for user in users if user["name"] == "John")
print("--------")
print(user)

filteredUser = list(filter(lambda user: user["age"] > 29, users))
print("--------")
print(filteredUser)



