import random

def alegere_utilizator(alegere):
    if alegere not in ["piatra", "foarfeca", "hartie"]:
        raise ValueError("Alegere invalida!")
    return alegere

def alegere_calculator():
    return random.choice(["piatra", "foarfeca", "hartie"])

def castigator(user, computer):
    if user == computer:
        return "egal"
    elif (user == "piatra" and computer == "foarfeca") or \
         (user == "foarfeca" and computer == "hartie") or \
         (user == "hartie" and computer == "piatra"):
        return "utilizator"
    else:
        return "calculator"

def afiseaza_rezultat(user, computer, castigator_runda):
    print(f"Tu ai ales: {user}, Calculatorul a ales: {computer}")
    print(f"Castigator: {castigator_runda}\n")

def actualizeaza_scor(scor, castigator_runda):
    scor[castigator_runda] += 1
    return scor

