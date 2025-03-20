#FOR LOOPS -> Fixed numbers of time

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

#continue => SKIP
#break => FINISH

# for x in range(1, 21):
#     if x == 13:
#         break
#     else:
#         print(x)

#NESTED LOOPS = A loop within another loop(outer, inner)
# outer loop:
#   inner loop:

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a sumbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end = "")
    print()