import random

def alegere_utilizator(alegere):
    """ Verifică dacă alegerea utilizatorului este validă """
    if alegere not in ["piatra", "foarfeca", "hartie"]:
        raise ValueError("Alegere invalida!")
    return alegere

def alegere_calculator():
    """ Returnează o alegere aleatoare pentru calculator """
    return random.choice(["piatra", "foarfeca", "hartie"])

def castigator(user, computer):
    """ Determină câștigătorul rundei """
    if user == computer:
        return "egal"
    elif (user == "piatra" and computer == "foarfeca") or \
         (user == "foarfeca" and computer == "hartie") or \
         (user == "hartie" and computer == "piatra"):
        return "utilizator"
    else:
        return "calculator"

def afiseaza_rezultat(user, computer, castigator_runda):
    """ Afișează alegerile și rezultatul rundei """
    print(f"Tu ai ales: {user}, Calculatorul a ales: {computer}")
    print(f"Castigator: {castigator_runda}\n")

def actualizeaza_scor(scor, castigator_runda):
    """ Actualizează scorul în funcție de rezultatul rundei """
    scor[castigator_runda] += 1
    return scor
