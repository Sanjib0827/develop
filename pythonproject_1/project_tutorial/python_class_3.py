test_var = "i live in cuttack"
test_var2 = "near shiv mandir"
test_var3 = "pincode"
test_var4 = 753001


print(test_var)
print(len(test_var))
print(test_var2)
print(test_var , test_var2)
print(len(test_var + test_var2))
print(test_var.count("i"))
print(test_var +" " + test_var2 +" " + test_var3)
print(len(test_var +" " + test_var2 +" " + test_var3))
print(str(test_var4))
print(test_var +" " + test_var2 +" " + test_var3 + " " + str(test_var4))
print(len(test_var +" " + test_var2 +" " + test_var3 + " " + str(test_var4)))

print(("san"+ test_var + test_var2+test_var3).count("i"))
sanj = "san "+ test_var+" "+test_var2+" "+test_var3
print(sanj)
print(sanj, type(sanj))
print(sanj.count("ne"))
sanjj = sanj.count("ne")
if sanjj > 0:
    print("found ne")
else:
    print("not found ne")

sanjj = sanj.count("sanjiv")
if sanjj > 0:
    print("found sanjiv")
else:
    print("not found sanjiv")


sanjj = sanj.count("cuttack")
if sanjj > 0:
    print("found cuttack")
else:
    print("not found cuttack")

sanjj = sanj.count("Cuttack")
if sanjj > 0:
    print("found Cuttack")
else:
    print("not found Cuttack")


sanjj = sanj.count("Cuttack".lower())
if sanjj > 0:
    print("found Cuttack")
else:
    print("not found Cuttack")

sanjj = sanj.count("CUTTACK".lower())
if sanjj > 0:
    print("found Cuttack")
else:
    print("not found Cuttack")

search_var = "mandirs"
sanjj = sanj.count(search_var)
if sanjj > 0:
    print("found " + search_var)
else:
    print("not found " + search_var)

search_var = "mandir"
sanjj = sanj.count(search_var)
if sanjj > 0:
    print("found " + str(sanjj) + search_var)
else:
    print("not found " + str(sanjj) + search_var)


search_var = "i"
sanjj = sanj.count(search_var)
if sanjj > 0:
    print("found " + str(sanjj) + " " + search_var)
else:
    print("not found " + str(sanjj) + " " + search_var)


search_var = "i"
sanjj = sanj.count(search_var)
if sanjj > 3:
    print("found many " + str(sanjj) + " " + search_var)
elif sanjj <3 and sanjj >0:
    print("found" + str(sanjj) + " " + search_var)
else:
    print("not found " + str(sanjj) + " " + search_var)


search_var = "in"
print("ide",sanj)
sanjj = sanj.count(search_var)
print("identifier",sanjj)
if sanjj > 3:
    print("holy found many " + str(sanjj) + " " + search_var)
elif sanjj <3 and sanjj >0:
    print("holy found" + str(sanjj) + " " + search_var)
else:
    print("holy not found " + str(sanjj) + " " + search_var)


search_var = "in"
print("ide",sanj)
sanjj = sanj.count(search_var)
print("identifier",sanjj)
if sanjj > 4:
    print("holly found many " + str(sanjj) + " " + search_var)
elif sanjj <=4 and sanjj >2:
    print("holly found average " + str(sanjj) + " " + search_var)
elif sanjj <=2 and sanjj >0:
    print("holly found minimal " + str(sanjj) + " " + search_var)
else:
    print("holly not found " + str(sanjj) + " " + search_var)










sanjj = sanj.count("mandir")
if sanjj > 0:
    print("demo found mandir")
else:
    print("demo not found")

