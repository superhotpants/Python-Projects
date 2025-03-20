

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# hello("Hello", title = "Mr.", first = "John", last = "Wick")

# for x in range(1, 11):
#     print(x, end = " ")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country = 81, area = 123, first = 456, last = 789)
print(phone_num)