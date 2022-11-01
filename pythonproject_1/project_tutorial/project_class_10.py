a = "Hello, World!"
# print(a[1])
# print(a[9])
print(a[12])
# print(a[4:6])
# print(a[:12])
print(a[12:])
print(len(a))
print(a[len(a)-1])
print(a[-1])
print(a[-2:])
print(a[-5:-2])

# reversing a string
print(a[::-1])
# print(a[-13:])
print(a[:])
print(a[::2])
print(a[::3])
print(a[::-2])
print(a[-2::-2])
# for x in "banana":
#     print(x)


# objective- take a string input and check if it is palindrome or not
# check palindrome

# example= madam -> madam --> palindrome
# example= sanjiv -> vijnas --> not a palindrome

input_variable = input("check palindrome")
# print(input_variable[::-1])
reverse_of_input = input_variable[::-1]
if input_variable == reverse_of_input:
    print("palindrome")
else:
    print("not a palindrome")

input_variable = input("check palindrome")
reverse_of_input = input_variable[::-1]