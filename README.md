Intra pe python.org si descarca si instaleaza programul python. 
Ai grija sa selectezi Add Python to PATH (e un checkbox mai jos cand vei deschide installerul).

Daca ai Ubuntu sau un Macbook vei avea deja instalat python.

Intra pe code.visualstudio.com si descarca editorul de cod. In acesta aplicatie vom scrie codul nostru. 

Dupa instalare deschide vscode. 
Apasa butonul Extensii si instaleaza urmatoarele extensii:

- Python creat de microsoft;
- Pylance tot de la microsoft;

Aceste 2 extensii ne vor ajuta foarte mult atunci cand scriem cod.


Apasa control plus buttonul de sub ESCcape (cel care contine backtick si simbolul pentru aproximativ);

Se va deschide un terminal in vscode aici haideti sa vedem daca avem python installat.

Tasteaza python --version, daca totul e ok vei vedea versiunea python

Creeaza un fisier nou main.py in acest fisier vom scrie ceva cod.

Hai sa printam ceva in terminal.

```py
print("Python e misto!")
```

Pentru a rula codul deschidem terminalul si tastam `python3 main.py`.
Vei vedea ca in terminal va fi printat ce am scris noi.

Simplu nu?

Sa trecem prin cateva notiuni de baza;

- variabile
Intr-o variablila putem salva diverse date necesare pentru a crea un program. 
O variabila poate contine un numar, un text, un boolean sau o structura mai complexa de date  

Hai sa adunam 2 numere sau integers cum se mai numesc in limbajele de programare:
```py

a = 1
b = 2
suma = a + b

print(f"Suma dintre a + b este {suma}!")

```

Explica codul de sus ^ 

Putem face la fel si cu 2 texte sau strings cum se numesc in limbajele de programare

```py

nume = "Goldan"
prenume = "Dan"
nume_complet = nume + " " + prenume

print(f"Nume complet: {nume_complet}!")

```

Explica codul de sus ^
- suprascrie variabla
- cast int("34") etc
 

Pe langa integers si strings (numere si text) mai avem floats si booleans < explica aici

Pana acum am vazut ca putem aduna 2 numere, dar putem face si operatii de scadere (-), inmultire (*) si alte operatii.

Putem combina aceste tipuri de date in structuri mai complexe de date cum ar liste, dictionare s.a

Putem avea o lista de strings (text):

```py
orase = ["Iasi", "Bucuresti", "Brasov"]
```

O lista de integers(ints):

```py
lista_numere = [5, 5, 5]
```

O lista in python poate contine si text si numere, o alta lista, un dictionar, etc 
```py

lista = [
    1,
    "Python",
    [5, 5, 5], 
    ["Iasi", "Bucuresti", "Brasov"]
    {"nume": "Alin", "job": "developer"}
]

```

Desi python permite acest lucru este recomandat ca listele sa aiba o structura bine definita.


Din lista de mai sus acesta 

```py
{"nume": "Alin", "job": "developer"}
```

este un dictionar 

in parte stanga va fi un key de obicei un string sau int si in partea dreapta poate fi orice alt obiect (lista, string, integer, float etc).


Acum ca stim cum putem salva datele in diverse structuri de date hai sa vedem ce operatii mai putem face.

Putem lua o decizie in functie de datele pe care le avem cu if/elif/else

De exemplu hai sa facem un dictionar:

```py
utilizator = {
    "nume": "Alex",
    "varsta": 24
}
```

Acum hai sa adaugam o conditie cu if/else:

```py

if utilizator["varsta"] > 18:
    print(f"{utilizator['nume']} poftim o tigara")
elif utilizator["varsta"] == 18:
    print(f"{utilizator['nume']} n-ai voie, esti mic!")
else:
    print(f"{utilizator['nume']} n-ai voie, esti mic!")

```

Putem combina operatia de mai sus intr-un singur if/else

```py

if utilizator["varsta"] >= 18:
    print(f"{utilizator['nume']} poftim o tigara")
else:
    print(f"{utilizator['nume']} n-ai voie, esti mic!")

```

Am vazut cum putem compara valori si lua decizii. 
Mai sunt si simboluri pe care le putem folosi pentru a face comparatii (mai mic sau egal, mai mare sau egal etc).


Putem grupa aceste mici operatiuni logice in functii si clase. 
Functiile si clasele create mai apoi le putem grupa in module si packete pe masura ce aplicatia creste.


Putem parcurge o lista sau un dictionar folosing for loops:

```py

orase = ["Iasi", "Bucuresti", "Brasov"]

for oras in orase:
    if oras == "Brasov":
        print("Foarte frumos orasul Brasov")
        continue

    print(f"E ok orasul {oras}")

```

Foloseste `and` si `or`.

Mai avem si while loop, dar acesta il folosim in cazurile in care avem ceva de asteptat sau parcurgem o structura mai complexa de date neconoscuta si vrem sa culegem/verificam anumite informatii.

```py

import random
import time

paharul_plin = True
while paharul_plin:
    print("sezi\n")
    time.sleep(1)
    print("bea\n")

    paharul_plin = random.choice([True, False])

print("du-te acasa si te culca")


```


Functii

Putem izola adunarea pe care am facut-o la inceput intr-o functie 

```py

def aduna(a: int, b: int):
    return a + b

```

Acum putem aduna orice alte 2 numere.

La fel putem face si cu operatia de if else:

```py

def cere_o_tigara(utilizator: dict):
    if utilizator["varsta"] >= 18:
        print(f"{utilizator['nume']} poftim o tigara")
    else:
        print(f"{utilizator['nume']} n-ai voie, esti mic!")

```

O variabla nu este acessibila peste tot in program. 
Daca creeam o variabla intr-o functie aceasta va fi disponibila doar pentru blocul respectiv de cod.

De asemeni, mare atentie atunci cand modifici o variabila primita ca parametru intr-o functie. 
Exemplu:

```py

def cere_o_tigara(utilizator: dict):
    utilizator["nume"] = "Costi"

    if utilizator["varsta"] >= 18:
        print(f"{utilizator['nume']} poftim o tigara")
    else:
        print(f"{utilizator['nume']} n-ai voie, esti mic!")


om = {"nume": "Alex", "varsta": 24}

print(om)

cere_o_tigara(om)

print(om)

```

Variabila creata `utilizator` este stocata in memorie si daca se vor aplica modificari cum am facut mai adiniaori variabila va fi schimbata in cele mai multe cazuri nu ne afecteaza prea mult, dar e ceva de luat in considerare. 


Clase in python

O clasa este foarte utila atunci cand scrii cod dupa dogma programare orientata pe obiecte (POO). 
Sunt niste standarde formate de-a lungul timpului care daca sunt implementate va fi mai usor pentru programatorii care intra intr-un proiect mai vechi sa inteleaga logica codului.


```py

class Utilizator:
    def __init__(self, nume: str, prenume: str) -> None:
        self.nume = nume
        self.prenume = prenume
        self.nume_complet = nume + " " + prenume

    def _creeaza_csv_pdf(self, date_csv: dict):
        # TODO: creaza un pdf, salveaza-l si trimite cale pdf
        return "/cv.pdf"

    def creeaza_cv(self, experienta: list[dict], educatie: list[dict] = None):
        date_csv = {
            "nume_complet": self.nume_complet,
            "experienta": experienta,
            "educatie": educatie,
        }
        return self._creeaza_csv_pdf(date_csv)


u = Utilizator(nume="Furgu", prenume="Tiberiu")

cale_cv = u.creeaza_cv(
    experienta=[
        {
            "companie": "Google",
            "pozitie": "developer",
            "perioada": {"inceput": "2020", "sfarsit": "2025"},
        }
    ]
)

print(cale_cv)

```

Explica: 
- self, 
- __init__, 
- class variables, 
- default parameters


Functiile unei clase se numesc metode.


Spor