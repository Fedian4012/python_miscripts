import random
from colorama import Fore

mini = 1
maxi = 100

while True:
    print(Fore.CYAN + f"J'ai choisi un nombre entre {mini} et {maxi}. Sauras-tu le retrouver ?")
    number = random.randint(mini, maxi)
    attempts = 0

    while True:
        try:
            user_proposition = int(input("Quelle est votre proposition ? "))
            if user_proposition < mini or user_proposition > maxi:
                raise ValueError(Fore.RED + f"Votre proposition n'est pas dans les valeurs acceptées. Veuillez entrer un nombre entre {mini} et {maxi}.")
            attempts += 1
            if user_proposition < number:
                print(Fore.RED + "Trop petit !")

            elif user_proposition > number:
                print(Fore.RED + "Trop grand !")

            else:
                print(Fore.GREEN + f"Vous avez trouvé en {attempts} tentatives !")
                break

        except ValueError:
            print("Veuillez entrer un nombre valide.")

    restart = input(Fore.CYAN + "Voulez-vous rejouer (O/n) ? ")
    if restart == "n":
        print(Fore.CYAN + "Merci d'avoir joué ! À bientôt !")
        break
    