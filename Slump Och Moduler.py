import random
player1 = input("player 1-")
player2 = input("player 2-")
delers = input("deler name-")

carddraw = random.randint(1,11)
carddraw3 = random.randint(1,11)
carddraw5 = random.randint(1,11)
carddraw7 = random.randint(1,11)
carddraw9 = random.randint(1,11)
print ((player1)+str("-")+ str(carddraw)+str(-carddraw3))
print (carddraw+carddraw3)
carddraw2 = random.randint(1,11)
carddraw4 = random.randint(1,11)
carddraw6 = random.randint(1,11)
carddraw8 = random.randint(1,11)
carddraw10 = random.randint(1,11)
print((player2)+str("-")+ str(carddraw2)+str(-carddraw4))
print(carddraw2+carddraw4)
deler = random.randint(1,11)
deler2 = random.randint(1,11)
deler3 = random.randint(1,11)
deler4 = random.randint(1,11)
deler5 = random.randint(1,11)
print(delers+ str(-deler)+str(-deler2))
print((deler+deler2))

player100 = input(player1+"-hit or stand-")
if player100 == "hit": 
    print (player1+ "-du har korten"+str(-carddraw5)+str(-carddraw)+str(-carddraw3))
    print(("vilket blir-")+str(carddraw+carddraw3+carddraw5))
else: 
    print (player1+ str(-carddraw+carddraw3))


player200 = input(player2+"-hit or stand-")
if player200 == "hit":
    print(player2+ "-du har korten"+str(-carddraw6)+str(-carddraw2)+str(-carddraw4))
    print(("vilket blir-")+str(carddraw2+carddraw4+carddraw6))
else:
    print(player2+str(-carddraw2+-carddraw4))

if player100 == "stand":
    print(player1+ str(-carddraw+carddraw3))
else:
    player1000 = input (player1+"-hit or stand-")

    if player1000 == "hit":
        print (player1+ "-du har korten"+str(-carddraw)+str(-carddraw3)+str(-carddraw5)+str(-carddraw7))
        print (("vilket blir-")+str(carddraw+carddraw3+carddraw5+carddraw7))
    else:
        print(player1+str(-carddraw+carddraw3+carddraw5))

if player200 =="stand":
    print(player2+ str(-carddraw+carddraw3))
else:
    player2000 =input (player2+"-hit or stand-")

    if player2000 == "hit":
        print ((player2)+ "-du har korten"+str(-carddraw2)+str(-carddraw4)+str(-carddraw6)+str(-carddraw8))
        print(("vilket blir-")+str(carddraw2+carddraw4+carddraw6+carddraw8))
    else:
        print(player2+str(-carddraw2+carddraw4))

if player100 == "stand":
    print(" ")
else: 
    if player1000 == "stand":
        print(str(-carddraw)+str(carddraw3)+str(carddraw5))
    else: 
        player10000 = input(player1+"-hit or stand-")
        if player10000 == "hit":
            print((player1)+ "-du har korten"+ str(-carddraw)+str(-carddraw3)+str(-carddraw5)+str(-carddraw7)+str(-carddraw9))
            print("vilket blir-"+ str (carddraw+carddraw3+carddraw5+carddraw7+carddraw9))
        else:
            print(player1+ str(carddraw+carddraw3+carddraw5+carddraw7))

if player200 == "stand":
    print(" ")
else: 
    if player2000 == "stand":
        print(str(-carddraw2)+str(carddraw4)+str(carddraw6))
    else: 
        player20000 = input(player2+"-hit or stand-")
        if player20000 == "hit":
            print((player2)+ "-du har korten"+ str(-carddraw2)+str(-carddraw4)+str(-carddraw6)+str(-carddraw8)+str(-carddraw10))
            print("vilket blir-"+ str (carddraw2+carddraw4+carddraw6+carddraw8+carddraw10))
        else:
            print(player2+ str(carddraw2+carddraw4+carddraw5+carddraw6))

if (carddraw+carddraw3+carddraw5) or (carddraw2+carddraw4+carddraw6) > (deler+deler2):
    print (delers+("-har-")+str(deler+deler2+deler3))
else: 
    print(delers)+("-har-")+str(deler+deler2)
if (carddraw+carddraw3+carddraw5) or (carddraw2+carddraw4+carddraw6) > (deler+deler2):
    if (carddraw+carddraw3+carddraw5+carddraw7) or (carddraw2+carddraw4+carddraw6+carddraw8) > (deler+deler2+deler3):
        print ((delers)+("-har-")+str(deler+deler2+deler3+deler4))
        if (carddraw+carddraw3+carddraw5+carddraw7+carddraw9) or (carddraw2+carddraw4+carddraw6+carddraw8+carddraw10) > (deler+deler2+deler3+deler4):
            print ((delers)+("-har-")+str(deler+deler2+deler3+deler4+deler5))

    
