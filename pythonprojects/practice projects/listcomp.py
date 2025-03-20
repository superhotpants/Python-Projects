# list comprehension

# Traditional
# doubles = []

# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)

# List comprehension
# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]

# print(doubles)

# nums = [1,-2,3,-4,5,-6, 8]
# po_nums = [num for num in nums if num >= 0]
# ne_nums = [num for num in nums if num < 0]
# ev_nums = [num for num in nums if num % 2 == 0]
# od_nums = [num for num in nums if num % 2 == 1]

# print(od_nums)

grades = [53,54,14,62,92,32]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)