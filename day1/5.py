a = int(input("Enter runs of PLAYER 1: "))
b = int(input("Enter runs of PLAYER 2: "))
c = int(input("Enter runs of PLAYER 3: "))

sta = (a/60)*100
stb = (b/60)*100
stc = (c/60)*100

print("Strike rate of PLAYER 1: ",sta)
print("Strike rate of PLAYER 2: ",stb)
print("Strike rate of PLAYER 3: ",stc)

print("Score after next 60 balls: ")
print("PLAYER 1: ", (a +(sta/100)*60))
print("PLAYER 2: ", (b +(stb/100)*60))
print("PLAYER 3: ", (c +(stc/100)*60))

print("Maximum sixes each player hit: ")
print("PLAYER 1: ",(a +(sta/100)*60)/6)
print("PLAYER 2: ",(b +(stb/100)*60)/6)
print("PLAYER 3: ",(c +(stc/100)*60)/6)
