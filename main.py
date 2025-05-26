from game import alegere_utilizator, alegere_calculator, castigator, afiseaza_rezultat, actualizeaza_scor

def joaca():
    try:
        runde = int(input("Cate runde vrei sa joci? "))
    except ValueError:
        print("Trebuie sa introduci un numar!")
        return

    scor = {"utilizator": 0, "calculator": 0, "egal": 0}

    for i in range(runde):
        print(f"\nRunda {i + 1}:")
        user_input = input("Alege: piatra, foarfeca, hartie: ")
        try:
            user = alegere_utilizator(user_input)
        except ValueError:
            print("Ai introdus o alegere gresita.")
            continue

        computer = alegere_calculator()
        rezultat = castigator(user, computer)
        scor = actualizeaza_scor(scor, rezultat)

        afiseaza_rezultat(user, computer, rezultat)

    print("Scor final:", scor)

if __name__ == "__main__":
    joaca()