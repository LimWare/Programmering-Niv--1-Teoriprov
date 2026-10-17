# -*- coding: utf-8 -*-
"""
Teoriquiz & Kodlabb i Python - Programmering 1 (Lektion 1-9)
Körs direkt i terminalen eller VS Code: python quiz.py
"""

import random

alla_fragor = [
    # --- LEKTION 1 ---
    {
        "lektion": "Lektion 1",
        "typ": "teori",
        "fraga": "Vad kallas datorns grundspråk som består av ettor och nollor och som CPU:n direkt kan tolka?",
        "alternativ": ["A) Assembleringsspråk", "B) Maskinkod", "C) Högnivåspråk", "D) Källkod"],
        "ratt": "B",
        "forklaring": "Maskinkod består av ettor och nollor som hårdvaran direkt förstår."
    },
    {
        "lektion": "Lektion 1",
        "typ": "teori",
        "fraga": "Vad är skillnaden mellan en interpretator och en kompilator?",
        "alternativ": ["A) En interpretator tolkar koden rad för rad under körning, medan en kompilator översätter hela programmet i förväg", "B) En kompilator används bara i Python", "C) En interpretator skapar alltid en .exe-fil", "D) Det betyder samma sak"],
        "ratt": "A",
        "forklaring": "Python är ett tolkande (interpreterat) språk."
    },
    {
        "lektion": "Lektion 1",
        "typ": "teori",
        "fraga": "Vad kallas processen att hitta och åtgärda fel i ett program?",
        "alternativ": ["A) Kompilering", "B) Debugging", "C) Indentering", "D) Syntaxering"],
        "ratt": "B",
        "forklaring": "Debugging är processen att spåra och åtgärda buggar/fel i kod."
    },
    {
        "lektion": "Lektion 1",
        "typ": "teori",
        "fraga": "Vad står förkortningen IDE för?",
        "alternativ": ["A) Internal Data Execution", "B) Integrated Development Environment", "C) Interactive Debugging Engine", "D) Internet Document Editor"],
        "ratt": "B",
        "forklaring": "IDE står för Integrated Development Environment (t.ex. VS Code)."
    },
    {
        "lektion": "Lektion 1",
        "typ": "kod",
        "fraga": "Skriv kod som skriver ut texten 'Hej Jensen!' på skärmen med print().",
        "tips": "Använd print(\"...\")",
        "nyckelord": ["print", "Hej Jensen!"]
    },
    {
        "lektion": "Lektion 1",
        "typ": "kod",
        "fraga": "Skriv kod som skriver ut ditt eget namn med hjälp av print().",
        "tips": "Använd print(\"Ditt Namn\")",
        "nyckelord": ["print"]
    },
    {
        "lektion": "Lektion 1",
        "typ": "kod",
        "fraga": "Skriv en print-sats som skriver ut talet 2026 på skärmen.",
        "tips": "Använd print(2026)",
        "nyckelord": ["print", "2026"]
    },

    # --- LEKTION 2 ---
    {
        "lektion": "Lektion 2",
        "typ": "teori",
        "fraga": "Vilket av följande variabelnamn är TILLÅTET i Python?",
        "alternativ": ["A) 1_variabel", "B) min variabel", "C) min_variabel_1", "D) min-variabel!"],
        "ratt": "C",
        "forklaring": "Variabelnamn får innehålla understreck (_) och siffror, men inte börja med en siffra eller innehålla mellanslag."
    },
    {
        "lektion": "Lektion 2",
        "typ": "teori",
        "fraga": "Vilken datatyp får variabeln x i koden: x = 13.5",
        "alternativ": ["A) int", "B) float", "C) str", "D) bool"],
        "ratt": "B",
        "forklaring": "Tal med decimalpunkt är av datatypen float."
    },
    {
        "lektion": "Lektion 2",
        "typ": "teori",
        "fraga": "Vad blir datatypen för x i koden: x = 'True'",
        "alternativ": ["A) bool", "B) int", "C) str", "D) float"],
        "ratt": "C",
        "forklaring": "Eftersom värdet omges av citattecken ('True') är det en textsträng (str)."
    },
    {
        "lektion": "Lektion 2",
        "typ": "teori",
        "fraga": "Vilket specialtecken skapar en ny rad inuti en print-sträng?",
        "alternativ": ["A) \\t", "B) \\n", "C) \\r", "D) \\\\"],
        "ratt": "B",
        "forklaring": "\\n står för ny rad (newline)."
    },
    {
        "lektion": "Lektion 2",
        "typ": "kod",
        "fraga": "Skapa en variabel som heter 'kurs' och tilldela den strängen 'Programmering 1', skriv sedan ut den.",
        "tips": "kurs = \"...\" och print(kurs)",
        "nyckelord": ["kurs", "=", "print"]
    },
    {
        "lektion": "Lektion 2",
        "typ": "kod",
        "fraga": "Skapa två variabler, 'tal1' med värdet 10 och 'tal2' med värdet 5, och skriv ut deras summa.",
        "tips": "tal1 = 10, tal2 = 5, print(tal1 + tal2)",
        "nyckelord": ["tal1", "tal2", "+", "print"]
    },
    {
        "lektion": "Lektion 2",
        "typ": "kod",
        "fraga": "Skapa en variabel 'pris' med värdet 199.9 och en variabel 'moms' med värdet 1.25, multiplicera dem och skriv ut.",
        "tips": "pris = 199.9, moms = 1.25, print(pris * moms)",
        "nyckelord": ["pris", "moms", "*", "print"]
    },

    # --- LEKTION 3 ---
    {
        "lektion": "Lektion 3",
        "typ": "teori",
        "fraga": "Vad skriver koden ut: print(9 // 2)",
        "alternativ": ["A) 4.5", "B) 4", "C) 5", "D) 4.0"],
        "ratt": "B",
        "forklaring": "Operatorn // utför heltalsdivision och kastar bort eventuella decimaler."
    },
    {
        "lektion": "Lektion 3",
        "typ": "teori",
        "fraga": "Vad beräknar uttrycket 2 ** 3 i Python?",
        "alternativ": ["A) 2 gånger 3", "B) 2 upphöjt till 3 (8)", "C) 2 dividerat med 3", "D) Resten av 2 / 3"],
        "ratt": "B",
        "forklaring": "** är potensoperatorn (2 * 2 * 2 = 8)."
    },
    {
        "lektion": "Lektion 3",
        "typ": "teori",
        "fraga": "Vad beräknar modulo-operatorn (%) i Python?",
        "alternativ": ["A) Vanlig division", "B) Resten vid division", "C) Procent", "D) Multiplikation"],
        "ratt": "B",
        "forklaring": "Modulo (%) returnerar resten av en division (t.ex. 5 % 2 = 1)."
    },
    {
        "lektion": "Lektion 3",
        "typ": "teori",
        "fraga": "Vilket av följande uttryck ger False i Python?",
        "alternativ": ["A) bool(-5)", "B) bool('Hej')", "C) bool(0)", "D) bool('0')"],
        "ratt": "C",
        "forklaring": "Endast talet 0 (samt tomma strängar/listor) ger False."
    },
    {
        "lektion": "Lektion 3",
        "typ": "kod",
        "fraga": "Skriv kod som beräknar produkten av 12 och 13 och skriver ut resultatet med print().",
        "tips": "print(12 * 13)",
        "nyckelord": ["print", "12", "13", "*"]
    },
    {
        "lektion": "Lektion 3",
        "typ": "kod",
        "fraga": "Skriv kod som räknar ut resten av 17 delat med 4 med modulo-operatorn (%) och skriver ut det.",
        "tips": "print(17 % 4)",
        "nyckelord": ["print", "17", "%", "4"]
    },
    {
        "lektion": "Lektion 3",
        "typ": "kod",
        "fraga": "Skriv kod som beräknar 3 upphöjt till 4 med potensoperatorn (**).",
        "tips": "print(3 ** 4)",
        "nyckelord": ["print", "3", "**", "4"]
    },

    # --- LEKTION 4 ---
    {
        "lektion": "Lektion 4",
        "typ": "teori",
        "fraga": "Vad returnerar alltid funktionen input() i Python?",
        "alternativ": ["A) Ett heltal (int)", "B) En sträng (str)", "C) Ett flyttal (float)", "D) Ett booleskt värde"],
        "ratt": "B",
        "forklaring": "input() ger alltid en sträng, varför man ofta behöver konvertera med int() eller float()."
    },
    {
        "lektion": "Lektion 4",
        "typ": "teori",
        "fraga": "Vilka tal genererar funktionen range(1, 6)?",
        "alternativ": ["A) 1, 2, 3, 4, 5, 6", "B) 0, 1, 2, 3, 4, 5", "C) 1, 2, 3, 4, 5", "D) 2, 3, 4, 5"],
        "ratt": "C",
        "forklaring": "Startvärdet 1 ingår, men slutvärdet (6) inkluderas ej."
    },
    {
        "lektion": "Lektion 4",
        "typ": "teori",
        "fraga": "Vilka tal skrivs ut av: for i in range(1, 10, 3): print(i)",
        "alternativ": ["A) 1, 4, 7, 10", "B) 1, 4, 7", "C) 1, 3, 6, 9", "D) 0, 3, 6, 9"],
        "ratt": "B",
        "forklaring": "Start 1, steg 3 upp till 10 ger 1, 4, 7 (10 ingår ej)."
    },
    {
        "lektion": "Lektion 4",
        "typ": "teori",
        "fraga": "Vad gör funktionen round(3.789, 1)?",
        "alternativ": ["A) Avrundar till 1 decimal (3.8)", "B) Avrundar till heltal (4)", "C) Ger ett felmeddelande", "D) Tar bort decimaler"],
        "ratt": "A",
        "forklaring": "round(tal, 1) avrundar till angivet antal decimaler."
    },
    {
        "lektion": "Lektion 4",
        "typ": "kod",
        "fraga": "Skriv kod som frågar användaren efter namn med input() och sparar i variabeln 'namn'.",
        "tips": "namn = input(\"Vad heter du? \")",
        "nyckelord": ["namn", "input"]
    },
    {
        "lektion": "Lektion 4",
        "typ": "kod",
        "fraga": "Skriv kod som frågar efter ålder med input(), konverterar till heltal med int() och sparar i 'ålder'.",
        "tips": "ålder = int(input(\"Ålder: \"))",
        "nyckelord": ["input", "int", "ålder"]
    },
    {
        "lektion": "Lektion 4",
        "typ": "kod",
        "fraga": "Skriv en for-loop som skriver ut alla tal från 1 till 5 med range().",
        "tips": "for i in range(1, 6): print(i)",
        "nyckelord": ["for", "range(1, 6)", "print"]
    },

    # --- LEKTION 5 ---
    {
        "lektion": "Lektion 5",
        "typ": "teori",
        "fraga": "Vilket tecken används för att kontrollera likhet i en if-sats?",
        "alternativ": ["A) =", "B) ==", "C) ===", "D) !="],
        "ratt": "B",
        "forklaring": "== används för jämförelse, medan enkelt = används för tilldelning."
    },
    {
        "lektion": "Lektion 5",
        "typ": "teori",
        "fraga": "Vilket nyckelord används för flera alternativa villkor efter en if?",
        "alternativ": ["A) else if", "B) elif", "C) case", "D) elseif"],
        "ratt": "B",
        "forklaring": "I Python förkortas else if till elif."
    },
    {
        "lektion": "Lektion 5",
        "typ": "teori",
        "fraga": "Hur skriver man 'inte lika med' i Python?",
        "alternativ": ["A) <>", "B) !=", "C) =/=", "D) NOT"],
        "ratt": "B",
        "forklaring": "'Inte lika med' skrivs med !=."
    },
    {
        "lektion": "Lektion 5",
        "typ": "teori",
        "fraga": "Vad saknas i koden: if x > 5 print('Stort')",
        "alternativ": ["A) Kolon (:) efter villkoret", "B) Parenteser", "C) Else-block", "D) Inget fel"],
        "ratt": "A",
        "forklaring": "if-satser måste alltid avslutas med kolon (:)."
    },
    {
        "lektion": "Lektion 5",
        "typ": "kod",
        "fraga": "Skriv en if-sats som kollar om 'poäng' är >= 50. Om sant, skriv ut 'Godkänt'.",
        "tips": "if poäng >= 50: print('Godkänt')",
        "nyckelord": ["if", "poäng", ">=", "print", "Godkänt"]
    },
    {
        "lektion": "Lektion 5",
        "typ": "kod",
        "fraga": "Skriv en if/else-sats som kollar om 'svar == \"ja\"'. Om sant skriv ut 'Rätt', annars 'Fel'.",
        "tips": "if svar == \"ja\": print('Rätt') else: print('Fel')",
        "nyckelord": ["if", "else", "print"]
    },
    {
        "lektion": "Lektion 5",
        "typ": "kod",
        "fraga": "Skriv en if/elif/else-sats som kollar om 'tal > 0' (skriv 'Positivt'), 'tal == 0' (skriv 'Noll'), annars 'Negativt'.",
        "tips": "if tal > 0: print('Positivt') elif tal == 0: print('Noll') else: print('Negativt')",
        "nyckelord": ["if", "elif", "else", "print"]
    },

    # --- LEKTION 6 ---
    {
        "lektion": "Lektion 6",
        "typ": "teori",
        "fraga": "När avbryts en while-loop automatiskt?",
        "alternativ": ["A) När dess villkor blir False", "B) Efter 10 varv", "C) Vid mellanslag", "D) Aldrig"],
        "ratt": "A",
        "forklaring": "En while-loop fortsätter så länge villkoret är True."
    },
    {
        "lektion": "Lektion 6",
        "typ": "teori",
        "fraga": "Varför uppstår en oändlig loop om räknaren inte uppdateras?",
        "alternativ": ["A) Villkoret förblir True för evigt", "B) Python kraschar direkt", "C) Print saknas", "D) Ingen anledning"],
        "ratt": "A",
        "forklaring": "Om villkoret aldrig ändras till False körs loopen i oändlighet."
    },
    {
        "lektion": "Lektion 6",
        "typ": "teori",
        "fraga": "Vad gör nyckelordet break i en loop?",
        "alternativ": ["A) Avbryter hela loopen omedelbart", "B) Hoppar över nuvarande varv", "C) Pausar", "D) Startar om"],
        "ratt": "A",
        "forklaring": "break avbryter loopen helt och hållet."
    },
    {
        "lektion": "Lektion 6",
        "typ": "teori",
        "fraga": "Vad gör nyckelordet continue i en loop?",
        "alternativ": ["A) Avbryter hela loopen", "B) Hoppar över resten av nuvarande varv och går till nästa", "C) Startar om programmet", "D) Gör ingenting"],
        "ratt": "B",
        "forklaring": "continue hoppar över resten av den aktuella iterationen och fortsätter med nästa varv."
    },
    {
        "lektion": "Lektion 6",
        "typ": "kod",
        "fraga": "Skriv en while-loop som körs så länge 'x < 3' och skriver ut x.",
        "tips": "while x < 3: print(x)",
        "nyckelord": ["while", "x < 3", "print"]
    },
    {
        "lektion": "Lektion 6",
        "typ": "kod",
        "fraga": "Skriv en for-loop med range(1, 6) som skriver ut alla tal från 1 till 5.",
        "tips": "for i in range(1, 6): print(i)",
        "nyckelord": ["for", "range(1, 6)", "print"]
    },
    {
        "lektion": "Lektion 6",
        "typ": "kod",
        "fraga": "Skriv en while-loop med en räknare som räknar ner från 3 till 1 och sedan skriver ut 'Klar!'.",
        "tips": "i = 3 while i > 0: print(i) i -= 1 print('Klar!')",
        "nyckelord": ["while", "print", "Klar!"]
    },

    # --- LEKTION 7 ---
    {
        "lektion": "Lektion 7",
        "typ": "teori",
        "fraga": "Vilken listmetod lägger till ett element sist i en lista?",
        "alternativ": ["A) add()", "B) append()", "C) insert()", "D) push()"],
        "ratt": "B",
        "forklaring": "append() lägger till elementet längst bak i listan."
    },
    {
        "lektion": "Lektion 7",
        "typ": "teori",
        "fraga": "Vilket index har det första elementet i en lista i Python?",
        "alternativ": ["A) 1", "B) 0", "C) -1", "D) Inget index"],
        "ratt": "B",
        "forklaring": "Python är nollindexerat (första elementet är index 0)."
    },
    {
        "lektion": "Lektion 7",
        "typ": "teori",
        "fraga": "Hur tar man bort ett element baserat på dess INDEX?",
        "alternativ": ["A) pop(index)", "B) remove(index)", "C) clear(index)", "D) delete(index)"],
        "ratt": "A",
        "forklaring": "pop(index) tar bort via indexnummer."
    },
    {
        "lektion": "Lektion 7",
        "typ": "teori",
        "fraga": "Vilken funktion ger antalet element i en lista?",
        "alternativ": ["A) size()", "B) length()", "C) len()", "D) count()"],
        "ratt": "C",
        "forklaring": "len() returnerar hur många element som finns i en lista eller sträng."
    },
    {
        "lektion": "Lektion 7",
        "typ": "kod",
        "fraga": "Skriv kod som skapar en tom lista 'frukter', och lägger till strängen 'Äpple' med append().",
        "tips": "frukter = [] och frukter.append('Äpple')",
        "nyckelord": ["frukter", "[]", "append", "Äpple"]
    },
    {
        "lektion": "Lektion 7",
        "typ": "kod",
        "fraga": "Givet listan 'bilar', skriv kod som tar bort det första elementet (index 0) med pop().",
        "tips": "bilar.pop(0)",
        "nyckelord": ["bilar", "pop", "0"]
    },
    {
        "lektion": "Lektion 7",
        "typ": "kod",
        "fraga": "Skriv kod som skapar en lista med tre namn och skriver ut det första namnet via dess index [0].",
        "tips": "namn = ['Anna', 'Björn', 'Cecilia'] print(namn[0])",
        "nyckelord": ["print", "[0]"]
    },

    # --- LEKTION 8 ---
    {
        "lektion": "Lektion 8",
        "typ": "teori",
        "fraga": "Om lista = [10, 20, 30, 40, 50], vad ger print(lista[1:4])?",
        "alternativ": ["A) [20, 30, 40]", "B) [10, 20, 30]", "C) [20, 30, 40, 50]", "D) [30, 40]"],
        "ratt": "A",
        "forklaring": "Slicing [1:4] tar index 1, 2 och 3 (index 4 inkluderas ej)."
    },
    {
        "lektion": "Lektion 8",
        "typ": "teori",
        "fraga": "Om land = 'Sverige', vad ger land[:2]?",
        "alternativ": ["A) Sv", "B) Sve", "C) S", "D) verige"],
        "ratt": "A",
        "forklaring": "Tar allt från början fram till index 2 (ej inklusive index 2), dvs 'Sv'."
    },
    {
        "lektion": "Lektion 8",
        "typ": "teori",
        "fraga": "Hur beräknar man kvadratroten ur 64 efter 'import math'?",
        "alternativ": ["A) math.sqrt(64)", "B) math.root(64)", "C) math.pow(64)", "D) sqrt(64)"],
        "ratt": "A",
        "forklaring": "math.sqrt() beräknar kvadratroten."
    },
    {
        "lektion": "Lektion 8",
        "typ": "teori",
        "fraga": "Vilken funktion ger summan av alla tal i en numerisk lista?",
        "alternativ": ["A) total()", "B) add()", "C) sum()", "D) count()"],
        "ratt": "C",
        "forklaring": "sum() summerar alla element i en numerisk lista."
    },
    {
        "lektion": "Lektion 8",
        "typ": "kod",
        "fraga": "Givet listan tal = [10, 20, 30, 40, 50], skriv kod som plockar ut [20, 30, 40] med slicing.",
        "tips": "tal[1:4]",
        "nyckelord": ["tal", "[1:4]"]
    },
    {
        "lektion": "Lektion 8",
        "typ": "kod",
        "fraga": "Skriv kod som importerar math-modulen och beräknar kvadratroten ur 64.",
        "tips": "import math och math.sqrt(64)",
        "nyckelord": ["import", "math", "sqrt", "64"]
    },
    {
        "lektion": "Lektion 8",
        "typ": "kod",
        "fraga": "Skriv kod som summerar alla tal i listan [5, 10, 15] med sum()-funktionen.",
        "tips": "print(sum([5, 10, 15]))",
        "nyckelord": ["print", "sum", "5", "10", "15"]
    },

    # --- LEKTION 9 ---
    {
        "lektion": "Lektion 9",
        "typ": "teori",
        "fraga": "Vilket nyckelord används för att definiera en egen funktion i Python?",
        "alternativ": ["A) function", "B) def", "C) fun", "D) define"],
        "ratt": "B",
        "forklaring": "Funktioner definieras med nyckelordet def."
    },
    {
        "lektion": "Lektion 9",
        "typ": "teori",
        "fraga": "Vad händer om en funktion saknar en return-sats?",
        "alternativ": ["A) Den kraschar", "B) Den returnerar automatiskt None", "C) Den returnerar 0", "D) Den körs inte"],
        "ratt": "B",
        "forklaring": "Funktioner som saknar return returnerar värdet None."
    },
    {
        "lektion": "Lektion 9",
        "typ": "teori",
        "fraga": "Vad kallas variablerna inom parenteserna när man skapar en funktion?",
        "alternativ": ["A) Parametrar (eller argument)", "B) Globala variabler", "C) Konstanter", "D) Returvärden"],
        "ratt": "A",
        "forklaring": "Parametrar tar emot inmatningsvärden när funktionen anropas."
    },
    {
        "lektion": "Lektion 9",
        "typ": "teori",
        "fraga": "Vad är skillnaden mellan lokala och globala variabler?",
        "alternativ": ["A) Lokala variabler skapas inuti en funktion och nås bara där; globala variabler skapas utanför funktioner och nås i hela programmet", "B) Det är exakt samma sak", "C) Globala variabler kan bara användas i for-loopar", "D) Lokala variabler sparas alltid på hårddisken"],
        "ratt": "A",
        "forklaring": "Lokala variabler existerar endast inne i sin funktion."
    },
    {
        "lektion": "Lektion 9",
        "typ": "kod",
        "fraga": "Skriv en funktion som heter 'plus' som tar emot två parametrar (a och b) och returnerar summan.",
        "tips": "def plus(a, b): return a + b",
        "nyckelord": ["def", "plus", "return", "+"]
    },
    {
        "lektion": "Lektion 9",
        "typ": "kod",
        "fraga": "Skriv en funktion 'kolla_tal' som tar in x. Om x > 10 ska den returnera 'Stort', annars 'Litet'.",
        "tips": "def kolla_tal(x): if x > 10: return 'Stort' else: return 'Litet'",
        "nyckelord": ["def", "kolla_tal", "if", "return", "Stort", "Litet"]
    },
    {
        "lektion": "Lektion 9",
        "typ": "kod",
        "fraga": "Skriv en funktion 'multiplicera' som tar in a och b, multiplicerar dem och returnerar resultatet.",
        "tips": "def multiplicera(a, b): return a * b",
        "nyckelord": ["def", "multiplicera", "return", "*"]
    }
]

def kor_quiz():
    print("=" * 65)
    print("  VÄLKOMMEN TILL PYTHON TEORIQUIZ & KODLABB (LEKTION 1-9)")
    print("=" * 65)
    
    print("\nVälj lektion eller läge:")
    print("0. Alla övningar (Blandat)")
    for i in range(1, 10):
        print(f"{i}. Lektion {i} (Flera teorifrågor & flera kodövningar)")
    
    val = input("\nDitt val (0-9): ").strip()

    if val in [str(i) for i in range(1, 10)]:
        valda_fragor = [q for q in alla_fragor if q["lektion"] == f"Lektion {val}"]
        print(f"\n--- ÖVNINGAR FÖR LEKTION {val} ---")
    else:
        valda_fragor = alla_fragor[:]
        random.shuffle(valda_fragor)
        print("\n--- ALLA ÖVNINGAR (SLUMPADE) ---")

    poang = 0
    totalt = len(valda_fragor)

    for i, q in enumerate(valda_fragor, 1):
        print(f"\nFråga {i} av {totalt} [{q['lektion']}]")
        
        if q["typ"] == "teori":
            print(q["fraga"])
            print("-" * 45)
            for alt in q["alternativ"]:
                print(alt)
            
            svar = input("\nDitt svar (A/B/C/D): ").strip().upper()
            if svar == q["ratt"]:
                print("✅ Rätt svar!")
                poang += 1
            else:
                print(f"❌ Fel! Rätt svar är {q['ratt']}.")
            print(f"Förklaring: {q['forklaring']}")
            
        else:  # Kodlabb
            print(f"✍️ KODUPPGIFT: {q['fraga']}")
            print(f"Tips: {q['tips']}")
            print("-" * 45)
            svar = input("Skriv ditt lösningsförslag här:\n> ").strip()
            
            godkand = all(kw.lower() in svar.lower() for kw in q['nyckelord'])
            if godkand:
                print("✅ Snyggt! Din kod innehåller rätt nyckelord och struktur.")
                poang += 1
            else:
                print("❌ Din kod saknade några viktiga delar.")

    print("\n" + "=" * 65)
    print(f"Slutresultat: Du fick {poang} av {totalt} rätt!")
    print("=" * 65)

if __name__ == "__main__":
    kor_quiz()
