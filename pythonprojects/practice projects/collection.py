#collection = single "variable" used tp stpre multiple values
# List = [] ordered and changeable, Duplicates OK
# Set = {} unordered and imuutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable, Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut")
print(fruits.count("apple"))
print(fruits.index("apple"))
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()
print(fruits)