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