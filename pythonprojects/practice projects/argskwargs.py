# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1,2,3,4))

# def display_name(*args):
#     for arg in args:
#         print(arg, end = " ")

# display_name("Spongebob", "Squarepants")
# print()

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street = "123 fake street",
#               apt = "100",
#               city = "Detroit", 
#               state = "MI", 
#               zip = "84923" )

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Superpants", "III",
               street = "123 fake street",
               pobox = "PO box #1001",
               city = "Detroit", 
               state = "MI", 
               zip = "84923")