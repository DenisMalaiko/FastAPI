# Def
numbers_1 = [1, 2, 3]
numbers_2 = [4, 5, 6]

def find_average(numbers):
    return sum(numbers) / len(numbers)

average_1 = find_average(numbers_1)
print(average_1)

average_2 = find_average(numbers_2)
print("--------")
print(average_2)



def format_date(*, day: int, month: str, year: int) -> str:
    return f"{day}/{month}/{year}"

print("--------")
print(format_date(day=4, year=2026, month="Jan"))
print(format_date(day=5, month="Feb", year=2026))