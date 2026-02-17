from itertools import product


def add_all(*args) :
    summary = 0
    for arg in args:
        summary += arg
    return summary

print(add_all(1, 2, 3))
print("--------")

values = [1, 2, 3]
other_values = [4, 5, 6]

print(add_all(*values, *other_values))
print("---------")


def introduce(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print("---------")


introduce(name="John", age=30)



def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True

    return old_dict, is_modified


user = { "name": "John", "age": 30 }
user, was_modified = modify_dict(old_dict=user, name="John", age=25)

print(user)
print(was_modified)