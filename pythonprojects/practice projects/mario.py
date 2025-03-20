def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invaild input. Please provide a positive integer.")

height = get_int("Height: ")

while height < 1 or height > 8:
    print("Invaild input. Please provide a number between 1 - 8.")
    height = get_int("Height: ")

for i in range(1, height + 1):
    print(" " * (height - 1) + "#" * i)