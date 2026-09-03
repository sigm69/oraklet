import random
player1 = input("player 1")
player2 = input("player 2")

carddraw = random.randint(1,11)
carddraw3 = random.randint(1,11)
carddraw5 = random.randint(1,11)
print ((player1)+ str(carddraw))
carddraw2 = random.randint(1,11)
carddraw4 = random.randint(1,11)
carddraw6 = random.randint(1,11)
print((player2)+ str(carddraw2))

player100 = input("hit or stand")
if player100 == "hit": 
    print (player1+str(carddraw3+carddraw))
else: 
    print (player100+ str(carddraw))

player200 = input("hit or stand")