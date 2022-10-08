ssa = input("enter first number ")
sss = input("enter second number ")
print("type ssa : ", type(ssa))
print("type sss : ", type(sss))
print("type ssa : ", type(int(ssa)))
print("type ssa : ", type(ssa))
ssa = int(ssa)
sss = int(sss)
print("after type casting type ssa : ", type(ssa))
if ssa != sss:
    print("ssa is not equal to sss")
    if ssa > sss:
        print("ssa is greater")
        first_name = input("enter first name ")
        print(first_name)
        if first_name == "chiku bhai":
            print("they are brothers")
        elif first_name == "lubu bhai":
            print("they are neighbours")
        elif first_name == "rajiv":
            print("small brother")
        elif first_name == "Sanjib":
            print("Sanjib match found")
        elif first_name == "sanjib":
            print("sanjib match found")
            surname = input("enter the surname ")
            print("sanjib", surname)

        else:
            print("no strings matched with sanjib")

    else:
        print("sss is greater")
else:
    print("ssa is equal to sss")

if ssa >= sss:
    print("sss is greater than equal to ssa")

print("execution complete")

