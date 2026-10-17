# -*- coding: utf-8 -*-
"""
Teoriquiz & Kodlabb i Python - Programmering 1 (Lektion 1-9)
Körs direkt i terminalen eller VS Code: python quiz.py
"""

import random

# Flervalsfrågor (43 st fördelade på Lektion 1-9)
flervalsfragor = [
    # LEKTION 1
    {
        "lektion": "Lektion 1",
        "fraga": "Vad kallas datorns grundspråk som består av ettor och nollor och som CPU:n direkt kan tolka?",
        "alternativ": ["A) Assembleringsspråk", "B) Maskinkod", "C) Högnivåspråk", "D) Källkod"],
        "ratt": "B",
        "forklaring": "Maskinkod består av ettor och nollor som hårdvaran direkt förstår."
    },
    {
        "lektion": "Lektion 1",
        "fraga": "Vad är skillnaden mellan en interpretator och en kompilator?",
        "alternativ": ["A) En interpretator tolkar koden rad för rad under körning, medan en kompilator översätter hela programmet i förväg", "B) En kompilator används bara i Python", "C) En interpretator skapar alltid en .exe-fil", "D) Det betyder samma sak"],
        "ratt": "A",
        "forklaring": "Python är ett tolkande (interpreterat) språk."
    },
    
    # LEKTION 2 & 3
    {
        "lektion": "Lektion 2",
        "fraga": "Vilket av följande variabelnamn är TILLÅTET i Python?",
        "alternativ": ["A) 1_variabel", "B) min variabel", "C) min_variabel_1", "D) min-variabel!"],
        "ratt": "C",
        "forklaring": "Variabelnamn får innehålla understreck (_) och siffror, men inte börja med en siffra eller innehålla mellanslag."
    },
    {
        "lektion": "Lektion 3",
        "fraga": "Vad skriver koden ut: print(9 // 2)",
        "alternativ": ["A) 4.5", "B) 4", "C) 5", "D) 4.0"],
        "ratt": "B",
        "forklaring": "Operatorn // utför heltalsdivision och kastar bort eventuella decimaler."
    },

    # LEKTION 4 & 5
    {
        "lektion": "Lektion 4",
        "fraga": "Vad returnerar alltid funktionen input() i Python?",
        "alternativ": ["A) Ett heltal (int)", "B) En sträng (str)", "C) Ett flyttal (float)", "D) Ett booleskt värde"],
        "ratt": "B",
        "forklaring": "input() ger alltid en sträng, varför man ofta behöver konvertera med int() eller float()."
    },
    {
        "lektion": "Lektion 5",
        "fraga": "Vilket tecken används för att kontrollera likhet i en if-sats?",
        "alternativ": ["A) =", "B) ==", "C) ===", "D) !="],
        "ratt": "B",
        "forklaring": "== används för jämförelse, medan enkelt = används för tilldelning."
    },

    # LEKTION 6 & 7
    {
        "lektion": "Lektion 6",
        "fraga": "När avbryts en while-loop automatiskt?",
        "alternativ": ["A) När dess villkor blir False", "B) Efter 10 varv", "C) Vid mellanslag", "D) Aldrig"],
        "ratt": "A",
        "forklaring": "En while-loop fortsätter så länge villkoret är True."
    },
    {
        "lektion": "Lektion 7",
        "fraga": "Vilken listmetod lägger till ett element sist i en lista?",
        "alternativ": ["A) add()", "B) append()", "C) insert()", "D) push()"],
        "ratt": "B",
        "forklaring": "append() lägger till elementet längst bak i listan."
    },

    # LEKTION 8 & 9
    {
        "lektion": "Lektion 8",
        "fraga": "Om lista = [10, 20, 30, 40, 50], vad ger print(lista[1:4])?",
        "alternativ": ["A) [20, 30, 40]", "B) [10, 20, 30]", "C) [20, 30, 40, 50]", "D) [30, 40]"],
        "ratt": "A",
        "forklaring": "Slicing [1:4] tar index 1, 2 och 3 (index 4 inkluderas ej)."
    },
    {
        "lektion": "Lektion 9",
        "fraga": "Vilket nyckelord används för att definiera en egen funktion i Python?",
        "alternativ": ["A) function", "B) def", "C) fun", "D) define"],
        "ratt": "B",
        "forklaring": "Funktioner definieras med nyckelordet def."
    }
]

# Kodlabb uppdelat per lektion (1-9) + blandade
kodutmaningar = [
    {
        "lektion": "Lektion 1 – Utskrift",
        "uppgift": "Skriv kod som skriver ut texten 'Hej Jensen!' på skärmen med print().",
        "tips": "Använd print(\"...\")",
        "nyckelord": ["print", "Hej Jensen!"]
    },
    {
        "lektion": "Lektion 2 – Variabler",
        "uppgift": "Skapa en variabel som heter 'kurs' och tilldela den strängen 'Programmering 1', skriv sedan ut den.",
        "tips": "kurs = \"...\" och print(kurs)",
        "nyckelord": ["kurs", "=", "print"]
    },
    {
        "lektion": "Lektion 3 – Aritmetik",
        "uppgift": "Skriv kod som beräknar resten av 17 delat med 4 med modulo-operatorn (%) och skriver ut resultatet.",
        "tips": "Använd print(17 % 4)",
        "nyckelord": ["print", "17", "%", "4"]
    },
    {
        "lektion": "Lektion 4 – Input & Typkonvertering",
        "uppgift": "Skriv kod som frågar efter ålder med input(), konverterar till heltal med int() och sparar i 'ålder'.",
        "tips": "ålder = int(input(...))",
        "nyckelord": ["input", "int", "ålder"]
    },
    {
        "lektion": "Lektion 5 – Villkorssats",
        "uppgift": "Skriv en if-sats som kollar om 'poäng' är större än eller lika med 50. Om sant, skriv ut 'Godkänt'.",
        "tips": "if poäng >= 50:",
        "nyckelord": ["if", "poäng", ">=", "print", "Godkänt"]
    },
    {
        "lektion": "Lektion 6 – While-loop",
        "uppgift": "Skriv en while-loop som körs så länge 'x < 3' och skriver ut x.",
        "tips": "while x < 3:",
        "nyckelord": ["while", "x < 3", "print"]
    },
    {
        "lektion": "Lektion 7 – Listor & Append",
        "uppgift": "Skriv kod som skapar en tom lista 'frukter', och lägger till strängen 'Äpple' med rätt metod.",
        "tips": "frukter = [] och frukter.append(...)",
        "nyckelord": ["frukter", "[]", "append", "Äpple"]
    },
    {
        "lektion": "Lektion 8 – Slicing",
        "uppgift": "Givet listan tal = [10, 20, 30, 40, 50], skriv kod som plockar ut de tre mittersta med slicing [1:4].",
        "tips": "tal[1:4]",
        "nyckelord": ["tal", "[1:4]"]
    },
    {
        "lektion": "Lektion 9 – Funktioner",
        "uppgift": "Skriv en funktion som heter 'plus' som tar emot två parametrar (a och b) och returnerar summan.",
        "tips": "def plus(a, b): return a + b",
        "nyckelord": ["def", "plus", "return", "+"]
    },
    {
        "lektion": "Blandad utmaning – Funktion med villkor",
        "uppgift": "Skriv en funktion 'kolla_tal' som tar in x. Om x > 10 ska den returnera 'Stort', annars 'Litet'.",
        "tips": "def kolla_tal(x): if x > 10: return 'Stort' else: return 'Litet'",
        "nyckelord": ["def", "kolla_tal", "if", "return", "Stort", "Litet"]
    }
]

def kor_quiz():
    print("=" * 65)
    print("  VÄLKOMMEN TILL PYTHON TEORIQUIZ & KODLABB (LEKTION 1-9)")
    print("=" * 65)
    
    print("\nVälj träningsläge:")
    print("1. Teoretiskt flervalsquiz")
    print("2. Kodlabb (Skriv kod lektion för lektion 1-9 + blandat)")
    val = input("Ditt val (1 eller 2): ").strip()

    if val == "2":
        print("\n" + "=" * 55)
        print("  KODLABB: SKRIV KOD FRÅN LEKTION 1 TILL 9")
        print("=" * 55)
        for i, u in enumerate(kodutmaningar, 1):
            print(f"\n[Utmaning {i}] {u['lektion']}")
            print(f"Uppgift: {u['uppgift']}")
            print(f"Tips: {u['tips']}")
            print("-" * 45)
            svar = input("Skriv ditt lösningsförslag här:\n> ").strip()
            
            godkand = all(kw.lower() in svar.lower() for kw in u['nyckelord'])
            if godkand:
                print("✅ Snyggt! Din kod innehåller rätt nyckelord och struktur.")
            else:
                print("❌ Din kod saknade några viktiga delar.")
        return

    # Standard flervalsquiz
    aktuella_fragor = flervalsfragor[:]
    random.shuffle(aktuella_fragor)
    poang = 0

    for i, q in enumerate(aktuella_fragor, 1):
        print(f"\nFråga {i} av {len(aktuella_fragor)} [{q['lektion']}]")
        print(q["fraga"])
        print("-" * 45)
        for alt in q["alternativ"]:
            print(alt)
        
        svar = input("\nDitt svar (A/B/C/D eller 'q' för att avsluta): ").strip().upper()
        if svar == "Q":
            print("Avslutar quizet...")
            break
        
        if svar == q["ratt"]:
            print("✅ Rätt svar!")
            poang += 1
        else:
            print(f"❌ Fel! Rätt svar är {q['ratt']}.")
        print(f"Förklaring: {q['forklaring']}")

    print("\n" + "=" * 65)
    print(f"Slutresultat: Du fick {poang} av {len(aktuella_fragor)} rätt!")
    print("=" * 65)

if __name__ == "__main__":
    kor_quiz()
