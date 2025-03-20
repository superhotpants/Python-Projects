#Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = int(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cannot be less than or equal to zero")

while rate <= 0:
    rate = int(input("Enter the principle amount: "))
    if rate <= 0:
        print("Interest rate cannot be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the principle amount: "))
    if time <= 0:
        print("Time cannot be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years/s: ${total: .2f}")
