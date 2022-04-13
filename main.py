import random
while True:
    x=int(input("cliquer sur 1 pour lancer le dé et 0 pour arrêter puis entrer"))
    if x==0:
        print("Fin du jeu")
        break
    elif x==1:
        print(random.randint(1,6))
    else:
        print("Commande incomprise")




