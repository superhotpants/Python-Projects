# name = input("Enter your full name: ")
# number = input("Enter your phone number: ")

# result = len(name)
# result = name.find("G")
# result = name.rfind("G")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# name = name.isdigit()
# name = name.isalpha()
# result = number.count("-")
# result = number.replace("-", "")
# print(help(str))


# print(result)

username = input("Enter your username: ")

username.find(" ")

username.isalpha()

if len(username) > 12:
    print("Your username can't be more than 12 characters.")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces.")
elif not username.isalpha():
    print("Your username can't contain numbers.")
else:
    print(f"Welcome {username}")