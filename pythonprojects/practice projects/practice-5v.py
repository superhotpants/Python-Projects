print("Hello World!!")

num = int(input("Enter your favorite number: "))

while True : 
    if num < 0 :
        print("That is a negative number")
        break
    elif num > 0 :
        print("That is a positive number")
        break

    else : 
        print("That is not a number")
        break

