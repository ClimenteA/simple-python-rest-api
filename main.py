# print("Python e misto!")

# a = 1
# b = 2
# suma = a + b

# print(f"Suma dintre a + b este {suma}!")


# nume = "Goldan"
# prenume = "Dan"
# nume_complet = nume + " " + prenume

# print(f"Nume complet: {nume_complet}!")


# def cere_o_tigara(utilizator: dict):
#     utilizator["nume"] = "Costi"

#     if utilizator["varsta"] >= 18:
#         print(f"{utilizator['nume']} poftim o tigara")
#     else:
#         print(f"{utilizator['nume']} n-ai voie, esti mic!")


# om = {"nume": "Alex", "varsta": 24}

# print(om)

# cere_o_tigara(om)

# print(om)


# class Utilizator:
#     def __init__(self, nume: str, prenume: str) -> None:
#         self.nume = nume
#         self.prenume = prenume
#         self.nume_complet = nume + " " + prenume

#     def _creeaza_csv_pdf(self, date_csv: dict):
#         # TODO: creaza un pdf, salveaza-l si trimite cale pdf
#         return "/cv.pdf"

#     def creeaza_cv(self, experienta: list[dict], educatie: list[dict] = None):
#         date_csv = {
#             "nume_complet": self.nume_complet,
#             "experienta": experienta,
#             "educatie": educatie,
#         }
#         return self._creeaza_csv_pdf(date_csv)


# u = Utilizator(nume="Furgu", prenume="Tiberiu")

# cale_cv = u.creeaza_cv(
#     experienta=[
#         {
#             "companie": "Google",
#             "pozitie": "developer",
#             "perioada": {"inceput": "2020", "sfarsit": "2025"},
#         }
#     ]
# )

# print(cale_cv)


# import random
# import time

# paharul_plin = True
# while paharul_plin:
#     print("sezi\n")
#     time.sleep(1)
#     print("bea\n")

#     paharul_plin = random.choice([True, False])

# print("du-te acasa si te culca")
