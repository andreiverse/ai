Problem Description
Context
Un pas esențial în procesul de digitalizare a patrimoniului cultural îl reprezintă colectarea, structurarea și publicarea datelor. Fără date reale, coerente și accesibile, orice analiză sau aplicație digitală ar rămâne la nivel pur teoretic.

Institutul Național al Patrimoniului contribuie direct la acest proces prin publicarea de seturi de date deschise pe platforma guvernamentală data.gov.ro, oferind acces public la informații oficiale despre instituțiile de cultură din România. Printre acestea se numără și datasetul referitor la muzeele din România, care conține informații precum denumirea muzeelor, localizarea administrativă, anul înființării, coordonate geografice și date descriptive.

În cadrul acestei probleme veți avea de realizat o analiză exploratorie pentru acest set de date.

Structura setului de date
Setul de date este furnizat în format CSV (Comma-Separated Values) și conține informații despre muzeele din România, rezultate în urma conversiei dintr-un format JSON publicat pe platforma data.gov.ro.

Fiecare rând din fișierul CSV corespunde unui muzeu, iar fiecare coloană descrie un anumit atribut al acestuia.

Câmpuri relevante
Setul de date conține, printre altele, următoarele coloane:

_id – identificator intern al înregistrării
județul – județul în care este localizat muzeul
denumirea (română) – numele muzeului în limba română
localitatea – localitatea în care se află muzeul
anul înființării – anul în care a fost înființat muzeul
categoria (română) – categoria muzeului
latitudine – coordonata geografică de latitudine
longitudine – coordonata geografică de longitudine
descrierea (română) – descriere textuală a muzeului
URL – site-ul web al muzeului (dacă este disponibil)
Valorile lipsă sunt marcate prin câmpuri goale.

Cerințe
Task-ul 1 - Numărul total de înregistrări (5 puncte)
Determinați numărul total de muzee din dataset.

Task-ul 2 - Numărul de muzee din București (10 puncte)
Determinați numărul de muzee pentru care în coloana județul găsim valoarea București.

Task-ul 3 - Numărul de coloane cu valori lipsă (15 puncte)
Determinați numărul coloanelor care conțin cel puțin o valoare lipsă (NaN).

Task-ul 4 - Anul cu cele mai multe muzee (10 puncte)
Determinați anul în care au fost înființate cele mai multe muzee, pe baza informațiilor pe care le avem specificate în coloana anul înființării.

Task-ul 5 - Distribuția muzeelor pe județe (20 puncte)
Determinați pentru fiecare județ, care apare în acest set de date, câte muzee există în acel județ.

Task-ul 6 - Procentul valorilor completate (20 puncte)
Pentru fiecare muzeu, calculați procentul de coloane completate (non-NaN) din totalul coloanelor. Calculul acestui scor este realizat utilizând următoarea formulă:

Formula

Task-ul 7 - Media scorului de completitudine (10 puncte)
Determinați media scorului de completitudine pentru întregul dataset. Pentru acest lucru, vom aduna scorurile obținute la cerința 6 și vom împărți totalul la numărul de muzee.

Task-ul 8 - Muzeele cu completitudine maximă (10 puncte)
Determinați procentul muzeelor care au scorul de completitudine maxim. Definim scorul de completitudine maxim drept valoarea maximă dintre cele determinate la task-ul 7.

Formatul fișierului de submisie
Pentru evaluarea automată trebuie să încărcați un fișier în format csv cu următoarea structură:

id – identificatorul rândului (corespunzător celui din test.csv)

pentru task-ul 1, veți folosi valoarea 1 pentru id
pentru task-ul 2, veți folosi valoarea 2 pentru id
pentru task-ul 3, veți folosi valoarea 3 pentru id
pentru task-ul 4, veți folosi valoarea 4 pentru id
pentru task-ul 5, veți folosi numele fiecărui județ (scris exact cum apare acesta în setul de date) pe post de id
pentru task-ul 6, veți folosi identificatorul intern al înregistrării (coloana _id din setul de date)
pentru task-ul 7, veți folosi valoarea 7 pentru id
pentru task-ul 8, veți folosi valoarea 8 pentru id
subtaskID – identificatorul cerinței:

1 pentru numărul total de înregistrări (task-ul 1)
2 pentru numărul de muzee din București (task-ul 2)
3 pentru numărul de coloane cu valori lipsă (task-ul 3)
4 pentru anul cu cele mai multe muzee (task-ul 4)
5 pentru distribuția muzeelor pe județe (task-ul 5)
6 pentru procentul valorilor completate (task-ul 6)
7 pentru media scorului de completitudinee (task-ul 7)
8 pentru muzeele cu completitudine maximă (task-ul 8)
answer – răspunsul corespunzător fiecărui task

pentru task-ul 1, va conține numărul total de muzee din dataset (valoare de tip integer)

pentru task-ul 2, va conține numărul de muzee din București (valoare de tip integer)

pentru task-ul 3, va conține numărul de coloane care conțin cel puțin o valoare lipsă (NaN) (valoare de tip integer)

pentru task-ul 4, va conține anul în care au fost înființate cele mai multe muzee (valoare de tip integer)

pentru task-ul 5, va conține numărul de muzee din fiecare județ (valoare de tip integer, câte un rând pentru fiecare județ)

pentru task-ul 6, va conține procentul câmpurilor completate pentru fiecare muzeu, calculat ca:

(număr câmpuri completate / număr total coloane) × 100
(valoare de tip float, recomandat rotunjită la 2 zecimale)

pentru task-ul 7, va conține media scorului de completitudine pentru întregul dataset (valoare de tip float, recomandat rotunjită la 2 zecimale)

pentru task-ul 8, va conține procentul muzeelor care au scorul de completitudine maxim (valoare de tip float, recomandat rotunjită la 2 zecimale)