# working with for loop

i = 1
#
# while i <= 100:
#     print("i is ", i)
#     i = i + 3

 # using while loop print 2 table

# 2 * 1 = 2

table = int(input('multiply'))
print(type(table))
i = 1
while i <=10:
    table_mul_value = table * i
    print(str(table) + "*" + str(i) + "=" + str(table_mul_value))
    i = i + 1


i = 0
while i < 6:
    i += 1

    if i == 3:
        continue
    print(i)

i = 6
while i < 6:
    print(i)

    if i == 3:
        break
    i += 1
else:
    print("in else of while")
print("check")


