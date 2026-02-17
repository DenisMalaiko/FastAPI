users_roles = ("admin", "editor", "user")

print("---------")
for role in users_roles:
    print(role)

print("---------")
print("admin" in users_roles)

print("---------")
print(users_roles[0])

print("---------")
role_1, role_2, _ = users_roles
print(role_1)
print(role_2)