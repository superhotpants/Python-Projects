print("Hello, welcome to Thunderbolt Coffee!!!!!")


name = input("What's your name?\n")

if name == "Ben" or name == "Nick" or name == "Loki":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?: "))
    if evil_status == "Yes" and good_deeds < 4:
        print("FUCK OFF YOU MOTHER FUCKER!!!")
    elif evil_status == "Yes" and good_deeds > 4:
        print("Welcome " + name + "!") 
        exit()
    else:
        print("Hello GOOD Ben!!")
else:
    print("Hello " + name + ", thanks for coming in today\n\n\n")

# if 4 > 3:
#     print("correct")
# else:
#     print("not correct")

# if order == "Frappeccino":
#     price = 13
# elif order == "Black Coffee":
#     price = 3
# elif order == "Espresso":
#     price = 5
# else:
#     print("Sorry, We do not have that here.")
#     price = 0




# me = "Ben"
# me == "Ben"
#"=" -> equal, "==" -> Boolean
#not equal -> != comparison logical operator challenge labs fuck off reputation repetation
