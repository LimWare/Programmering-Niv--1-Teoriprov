# 🐍 Programmering Nivå 1 – Teoriprov (JENSEN Education)

Interaktivt träningsquiz och lathund inför teoriprovet på Exam.net i **Programmering 1 (Python)**, baserat på Lektion 1–9.

### 🚀 [Klicka här för att starta webbquizet!](https://limware.github.io/Programmering-Niv--1-Teoriprov/)

---

## 📚 Snabblathund inför provet (Lektion 1–9)

### 1. Datorns grunder & Programspråk (Lektion 1)
* **Maskinkod:** Datorns grundspråk som består av ettor och nollor (`1` och `0`) som CPU:n direkt kan tolka.
* **Assembleringsspråk:** Ett lågnivåspråk (*Low-level language*) där instruktioner skrivs som enkla textkommandon (t.ex. `LOAD A`, `ADD B`). Måste översättas till maskinkod.
* **Högnivåspråk:** Anpassat för människor ("halvengelska"), t.ex. Python, Java och C++.
* **Interpretator vs. Kompilator:**
  * **Interpretator (tolk):** Översätter och kör programmet **rad för rad** direkt (t.ex. *Python, JavaScript, Ruby*).
  * **Kompilator:** Översätter **hela programmet på en gång** till en körbar fil, t.ex. `.exe` (t.ex. *C, C++, C#, Java*).
* **Debugging:** Processen att felsöka och åtgärda fel (*errors*) i ett datorprogram.
* **IDE (*Integrated Development Environment*):** Ett program med alla verktyg för att skriva, köra och felsöka kod (t.ex. *VS Code, PyCharm*).
* **Python-fakta:** Lanserades av **Guido van Rossum** år **1991** och använder filändelsen **`.py`**.

---

### 2. Variabler, Datatyper & Matematik (Lektion 2 & 3)
* **Variabelnamn:** Får endast innehålla bokstäver, siffror och understreck (`_`). Får **aldrig** börja med en siffra eller innehålla mellanslag. Python är *case sensitive* (`enBok` och `EnBok` är två olika variabler).
* **Grundläggande datatyper (`type()`):**
  * `int` – Heltal (t.ex. `5`, `-12`)
  * `float` – Decimaltal, skrivs alltid med **punkt** (t.ex. `2.6`)
  * `str` – Textsträng, omges av `""` eller `''` (OBS: `'123'` är en textsträng, inte ett tal!)
  * `bool` – Booleskt värde (`True` eller `False`). Alla tal utom `0` och alla strängar/listor som inte är tomma utvärderas till `True` med `bool()`.
* **Prioriteringsregler:** 1. Parenteser `()` -> 2. Potenser `**` -> 3. Multiplikation `*` & Division `/` -> 4. Addition `+` & Subtraktion `-`.
* **Specialoperatorer:**
  * `**` = Upphöjt till (`7 ** 2` ger `49`, och `49 ** 0.5` ger kvadratroten `7.0`).
  * `//` = Heltalsdivision som kapar decimalerna (`9 // 2` ger `4`, medan `9 / 2` ger `4.5`).
* **Utskrift (`print`):** Kommatecken `,` ger mellanslag mellan värden. Plustecken `+` klistrar ihop strängar utan mellanslag. `\n` = ny rad, `\t` = tabb-indrag.

---

### 3. Input, Loopar & Villkor (Lektion 4, 5, 6 & 7)
* **`input()`:** Returnerar **alltid en sträng (`str`)**. Konvertera med `int(input(...))` eller `float(input(...))` vid beräkningar, annars blir `5 * "8"` -> `"88888"`.
* **Avrundning:** `round(663.671, 2)` ger `663.67`. `round(663.99)` ger `664`.
* **`for`-loop & `range()`:** Upprepar kod ett **bestämt antal gånger**.
  * `range(5)` -> `0, 1, 2, 3, 4` (startar på 0).
  * `range(1, 6)` -> `1, 2, 3, 4, 5` (slutvärdet 6 ingår **inte**).
  * `range(1, 17, 3)` -> trean anger steglängden (`1, 4, 7, 10, 13, 16`).
  * `range(29, 24, -1)` -> räknar baklänges från 29 ner till 25.
* **`while`-loop:** Upprepar kod **så länge ett villkor är sant (`True`)**. Glöm inte att ge räknarvariabeln ett startvärde innan loopen!
* **`break` vs. `continue`:**
  * `break` avbryter **hela loopen** direkt och går till koden utanför.
  * `continue` avbryter **bara nuvarande varv** (iteration) och hoppar direkt till nästa varv.
* **Villkor (`if`, `elif`, `else`):** Glöm aldrig kolon `:` och indentering!
  * Jämförelseoperatorer: `==` (lika med), `!=` (inte lika med), `<`, `<=`, `>`, `>=`. *(OBS: Enkelt `=` används bara för tilldelning!).*

---

### 4. Listor, Dellistor & Matematikmodulen (Lektion 7 & 8)
* **Listor (`[]`):** Indexeras alltid från **`0`**.
  * `len(lista)` – Returnerar antalet element i listan.
  * `lista.append(x)` – Lägger till `x` **sist** i listan.
  * `lista.insert(index, x)` – Infogar `x` på angivet index.
  * `lista.pop(index)` – Tar bort elementet på angivet **indexnummer**.
  * `lista.remove(värde)` – Tar bort elementet med angivet **värde**.
  * `lista.clear()` – Tömmer hela listan (`[]`).
  * `if "Apple" in fruits:` – Kontrollerar om ett element finns i listan.
* **Dellistor (Slicing):**
  * `lista[3:]` – Från och med index 3 till slutet.
  * `lista[:3]` – Från början fram till index 3 (index 3 ingår **ej** -> index 0, 1, 2).
  * `lista[2:4]` – Från index 2 fram till index 4 (index 4 ingår **ej** -> index 2, 3).
  * `kopia = lista[:]` – Skapar en kopia av hela listan.
* **Matematikfunktioner:** Inbyggda är `min(lista)`, `max(lista)`, `sum(lista)` och `pow(bas, exp)`. Med `import math` får man `math.sqrt(x)` (kvadratrot) och `math.pi`.

---

### 5. Funktioner (Lektion 9)
* **Definiera funktion:** Skapas med nyckelordet `def`, följt av funktionsnamn, parametrar inom `()` och kolon `:`.
* **Returvärde (`return`):** Skickar tillbaka resultatet så att funktionsanropet ersätts av returvärdet. Alla datatyper (strängar, tal, listor) behåller sin datatyp när de skickas in som parametrar.
