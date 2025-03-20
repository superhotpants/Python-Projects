#dictionary = a collection of {key : value} pair

capitals = {"USA" : "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow",
            "Japan" : "Tokyo"}

# if capitals.get("Korea"):
#     print("That capital exists")
# else:
#     print("That capital does exist")


# capitals.update({"Germany" : "Berlin"})
# capitals.pop("China")
# capitals.clear()

# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in values:
#     print(value)


items = capitals.items()
for key, value in items:
    print(f"{key}: {value}")