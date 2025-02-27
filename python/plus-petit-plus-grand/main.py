import random

mini = 1
maxi = 100

while True:
    print(f"J'ai choisi un nombre entre {mini} et {maxi}. Sauras-tu le retrouver ?")
    number = random.randint(mini, maxi)
    attempts = 0

    while True:
        try:
            user_proposition = int(input("Quelle est votre proposition ? "))
            if user_proposition < mini or user_proposition > maxi:
                raise ValueError(f"Votre proposition n'est pas dans les valeurs acceptées. Veuillez entrer un nombre entre {mini} et {maxi}.")
            attempts += 1
            if user_proposition < number:
                print("Trop petit !")

            elif user_proposition > number:
                print("Trop grand !")

            else:
                print(f"Vous avez trouvé en {attempts} tentatives !")
                break

        except ValueError:
            print("Veuillez entrer un nombre valide.")

    restart = input("Voulez-vous rejouer (O/n) ? ")
    if restart == "n":
        print("Merci d'avoir joué ! À bientôt !")
        break
    