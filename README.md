
Intr-un folder nou sa spunem RESTAPI haideti sa creeam un virtual environment care ne va ajuta sa pastram izolate dependintele externe. 

Deschidem terminalul si tastam: `virtualenv venv` (daca nu ai instalat virtualenv o poti face acum folosind comanda pip install virtualenv).

Vom vedea ca un nou folder venv a fost creat. 
In acest folder a fost copiat executabilul python, toate packetele externe de care avem nevoie for fi instalate aici.

Pentru a construi un RESTAPI minimal avem nevoie de un web framework, vom folosi FastApi pentru asta, si o baza de date, vom folosi SQLITE pentru a salva datele. 

Mai avem nevoie de 2 fisiere:
- in main.py vom adauga codul necesar pentru restapi;
- in requirements.txt vom adauga dependintele externe cum ar fi fastapi;

fastapi are nevoie si de uvicorn asa ca il vom adauga si pe acesta, inca un lucru de care avem "oarecum" nevoie este un ORM - un packet extern care ne ajuta sa lucram in acelasi fel cu diverse baze de date SQL (PostgresSQL, MySQL, MariaSQL etc). Am ales sqlmodel pentru asta, dar mai sunt si alte alternative. Cel mai folosit ORM (Object relational mapper) cu python este SQLAlchemy.

Inainte de a instala dependintele externe trebuie sa activam virtual environment folosim comanda `source venv/bin/activate`. Vedem acum ca inainte de numele PC-ului scrie in paranteze (venv) asta inseamna ca avem virtual environment activat.


Instalam packetele din requirements.txt folosing comanda `pip install -r requirements.txt`.

In fisierul `main.py` putem incepe sa construim rest-api-ul.


Vom crea un rest-api pentru o aplicatie care ajuta 2 sau mai multe persoane sa semneze un contract de la distanta.

Docusign este un exemplu de astfel de aplicatie
- https://www.docusign.com/

Aici putem vedea in mare care sunt cerintele pentru ca o semnatura digitala sa fie valida:
- https://support.ucsd.edu/services?id=kb_article_view&sysparm_article=KB0030064

Pe scurt:
- serverul nostru trebuie respecte cele mai inalte standarde de securitate;
- fiecare semnatura digitala trebuie sa fie unica, encriptata si sa nu poata fi modificata;
- are nevoie si de ceva aprobari de la autoritatile care se ocupa de acest domeniu;

Noi vom face doar o parte din aceste lucruri pentru a vedea cum functioneaza un rest-api.


Sa definim cerintele:

- un contract va fi in format pdf;
- contractul va fi semnat de 2 parti constituite din 1 sau mai multe persoane pentru fiecare parte;

De exemplu:

Sa spunem ca o persoana vrea sa dea un apartament in chirie si nu poate fi prezent la semnarea contractului cu chiriasii. 
Cele 2 parti vor fi odata proprietarul (sau proprietarii) apartamentului si chiriasul (sau chiriasii) apartamentului.

- contractul trimis trebuie sa poata fi unic identificat;
- semnaturile partilor trebuie sa fie unice;


Iata cum ar arata aceste date intr-o baza de date:

- am avea nevoie de un tabel cu utilizatori si semnaturile lor;
tabelul utilizatori ar avea urmatoarele coloane:
- id utilizator;
- nume;
- prenume;
- semnatura digitala;

- mai avem nevoie si de un tabel in care salvam contractele semnate;
tabelul contracte semnate va contine urmatoarele coloane:
- nume contract;
- id parti contractante;
- contract id;
- cale contract;
- semnatura digitala parti contractate;



Haideti sa mai cream un modul models.py in care sa punem logica aplicatiei. 
Aici avem functii care ne ajuta sa salvam si sa preluam date in baza de date