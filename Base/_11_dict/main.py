person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person)
print("--------")

person["job"] = "Engineer"
print(person)
print(person["job"])
print(person.get("job"))
print("--------")

additional_info = {
    "phone": "123456789",
    "city": "London"
}

person.update(additional_info)
print(person)
print("--------")

person = person | additional_info
print(person)