#[start : end : step]
credit_number = "1234-5678-9012-2456"

credit_number = credit_number[::-1]
print(credit_number)
# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::3])

email = input("Enter your email: ")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username} and domain is {domain}")