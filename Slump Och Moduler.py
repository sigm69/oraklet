import random
player1 = input("player 1")
player2 = input("player 2")

carddraw = random.randint(1,11)
carddraw3 = random.randint(1,11)
carddraw5 = random.randint(1,11)
carddraw7 = random.randint(1,11)
print ((player1)+str("-")+ str(carddraw)+str(-carddraw3))
print (carddraw+carddraw3)
carddraw2 = random.randint(1,11)
carddraw4 = random.randint(1,11)
carddraw6 = random.randint(1,11)
carddraw8 = random.randint(1,11)
print((player2)+str("-")+ str(carddraw2)+str(-carddraw4))
print(carddraw2+carddraw4)

player100 = input("hit or stand")
if player100 == "hit": 
    print (player1+str(carddraw5)+str(-carddraw)+str(-carddraw3))
    print(carddraw+carddraw3+carddraw5)
else: 
    print (player1+ str(-carddraw+carddraw3))


player200 = input("hit or stand")
if player200 == "hit":
    print(player2+str(carddraw6)+str(-carddraw2)+str(-carddraw4))
    print(carddraw2+carddraw4+carddraw6)
else:
    print(player2+str(-carddraw2+-carddraw4))

if player100 == "stand":
    print(player1+ str(-carddraw+carddraw3))
else:
    player1000 = input ("hit or stand")

    if player1000 == "hit":
        print (player1+ "-du har korten"+str(-carddraw)+str(-carddraw3)+str(-carddraw5)+str(-carddraw7))
        print((carddraw)+(carddraw3)+(carddraw5)+(carddraw7))
    else:
        print(player1+str(-carddraw+carddraw3+carddraw5))

if player200 =="stand":
    print(player2+ str(-carddraw+carddraw3))
else:
    player2000 =input ("hit or stand")

    if player2000 == "hit":
        print ((player2)+str(carddraw2)+str(carddraw4)+str(carddraw6)+str(carddraw8))
        print(carddraw2+carddraw4+carddraw6+carddraw8)
    else:
        print(player2+str(-carddraw2+carddraw4))

    if player2000 == "stand":
        print(player2+-carddraw2+carddraw4+carddraw6+carddraw8)