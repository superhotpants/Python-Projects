# #PYTHON LIST
# supplies = ["tent", "sleeping bag", "cup", "knifs",
#                 "flash drives", "camp kodomo", "coffess",
#                 "marshmellows"]

# camp_site = ["Crystal Lake", 404, 89.3, True]

# # me = camping_list[7]

# # you = camping_list[-1]

# # print(me)
# # print(you)
# # print(camping_list)

# # #what can I do using python? I don't even know 
# # #if this grammer is right or not.

# #ADDING TOILET PAPER INTO THE LIST
# #-> Method

# # supplies = supplies + ["toilet paper", "bidet"]
# # = supplies.extend([])

# supplies.insert(0, "bidet")
# supplies.insert(-1, "toilet paper")

# # supplies.remove("tent")
# # supplies.remove("sleeping bag")

# supplies.pop(1)
# print("This item was just deleted: " + supplies.pop(1))


# print(supplies)

#LIST MUTABLE
# alist = ["apple", "grape", "lemon"]

# alist[0] = "cherry"

# print(alist)

#TUPLE IMMUTABLE
atuple = ("apple", "grape", "lemon")

atuple[0] = "cherry"

print(atuple)