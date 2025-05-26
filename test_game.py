import unittest
from game import (
    alegere_utilizator,
    alegere_calculator,
    castigator,
    afiseaza_rezultat,
    actualizeaza_scor
)

class TestJoc(unittest.TestCase):


    def test_alegere_valida_piatra(self):
        self.assertEqual(alegere_utilizator("piatra"), "piatra")

    def test_alegere_valida_hartie(self):
        self.assertEqual(alegere_utilizator("hartie"), "hartie")

    def test_alegere_invalida(self):
        with self.assertRaises(ValueError):
            alegere_utilizator("fier")


    def test_alegere_calculator_in_lista(self):
        self.assertIn(alegere_calculator(), ["piatra", "hartie", "foarfeca"])

    def test_alegere_calculator_tip_str(self):
        self.assertIsInstance(alegere_calculator(), str)

    def test_alegere_calculator_nu_returneaza_none(self):
        self.assertIsNotNone(alegere_calculator())


    def test_utilizator_castiga(self):
        self.assertEqual(castigator("piatra", "foarfeca"), "utilizator")

    def test_calculator_castiga(self):
        self.assertEqual(castigator("foarfeca", "piatra"), "calculator")

    def test_egalitate(self):
        self.assertEqual(castigator("hartie", "hartie"), "egal")


    def test_afisare_output_fara_eroare(self):
        try:
            afiseaza_rezultat("piatra", "hartie", "calculator")
        except Exception as e:
            self.fail(f"A dat eroare la afisare: {e}")

    def test_afisare_egal(self):
        try:
            afiseaza_rezultat("hartie", "hartie", "egal")
        except:
            self.fail("Afisarea egalității a eșuat.")

    def test_afisare_castig_utilizator(self):
        try:
            afiseaza_rezultat("foarfeca", "hartie", "utilizator")
        except:
            self.fail("Afisarea câștigului utilizatorului a eșuat.")


    def test_actualizare_scor_utilizator(self):
        scor = {"utilizator": 0, "calculator": 0, "egal": 0}
        rezultat = actualizeaza_scor(scor, "utilizator")
        self.assertEqual(rezultat["utilizator"], 1)

    def test_actualizare_scor_calculator(self):
        scor = {"utilizator": 0, "calculator": 0, "egal": 0}
        rezultat = actualizeaza_scor(scor, "calculator")
        self.assertEqual(rezultat["calculator"], 1)

    def test_actualizare_scor_egal(self):
        scor = {"utilizator": 0, "calculator": 0, "egal": 0}
        rezultat = actualizeaza_scor(scor, "egal")
        self.assertEqual(rezultat["egal"], 1)

if __name__ == "__main__":
    unittest.main()

