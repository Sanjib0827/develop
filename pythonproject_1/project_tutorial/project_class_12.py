# working with for and while loop together
# [INTERVIEW TYPE QUESTION]
# input : 4
# output:
# *
# **
# ***
# ****

# user_input = int(input("enter a number"))
# initial_start_point = 1
# while initial_start_point <= user_input:
#     output = "*" * initial_start_point
#     print(output)
#     initial_start_point += 1


user_input = int(input("enter a number"))
initial_start_point = 1
while initial_start_point <= user_input:
    j = 1
    output = ""
    while j <= initial_start_point:
        output = output + "*"
        j = j + 1
    print(output)
    initial_start_point += 1











# k = "hello hi how are you"
# for char in k:
#     print(char)
# print("using range function")
# for i in range(len(k)):
#     print(k[i])
