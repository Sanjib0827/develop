ssa = input("enter first number")
sss = input("enter second number")
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

        if "sanjib " == "chiku bhai":
            print("they are brothers")
        elif "sanjib" == "lubu bhai":
            print("they are neighbours")
        elif "sanjib" == "rajiv":
            print("small brother")
        elif "Sanjib" == "sanjib":
            print("Sanjib match found")
        elif "sanjib" == "sanjib":
            print("sanjib match found")
            surname = input("enter the surname")
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

