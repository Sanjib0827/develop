# working on strings
test_var = "i love to play badminton"
# finding the length of a variable
# finding the occurence of a character a and t in a string variable
# concatenating string with string
test_var2 = 'at ymca'

print(test_var + test_var2)
print(test_var +  test_var2)
print(test_var + " " + test_var2)

play_message = test_var + " " + test_var2
print(play_message)

# concatenating string with integer
test_var3 = 1930
test_var4 = "hrs"

print(str(test_var3) + test_var4)
print(str(test_var3) + " " + test_var4)

time = str(test_var3) + " " + test_var4
print( 'time iss ' + time)
print(type(time))

print('time is ' + time + ' type is ' + str(type(time)))





# combination test_var+1+2+3+4
print(test_var + " " + test_var2 + " " + time )
playy = test_var + " " + test_var2 + " " + time
print(playy)
print("h frequency " + str(playy.count("h")))
print(len("i love to play badminton"))

print("h frequency " , playy.count("h"))
playyy = "h frequency " , playy.count("h")
print(playyy)

playing_message ="i love to play badminton"
print(playing_message.count("a"))
print(playing_message.count("t"))
print(playing_message.count("o"))
print(playing_message.count("a"))

x = "python"
y = "is"
z = "awesome"
print(x,y,z)
print(x+y+z)
print(x + " " + y + " " + " " + z)

a = "i love to, play, badminton"
print(len(a))
age = 36
txt = "my name is john i am "
print("sanjib sahoo "+ txt + str(age))

quantity = 3
itemno = 567
price = 49.95

myorder = "i want " + str(quantity) + " pieces of item @ " + str(itemno) + " for " + str(price)
print(myorder)