import random

svar= ["Ja, helt klart.","absolut inte","fråga igen imorgon","det vill du inte vera.","tackar","sigma"]

fråga = input("fråga oraklet: ")
print("Du frågade :", fråga)
print(random.choice(svar))