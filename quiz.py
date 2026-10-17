# -*- coding: utf-8 -*-
"""
Teoriquiz & Kodlabb i Python - Programmering 1 (Lektion 1-9)
Körs direkt i terminalen eller VS Code: python quiz.py
"""

import random

# Frågor uppdelade per lektion (både teori och kodlabb)
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
        "typ": "kod",
        "fraga": "Skriv kod som skriver ut texten 'Hej Jensen!' på skärmen med print().",
        "tips": "Använd print(\"...\")",
        "nyckelord": ["print", "Hej Jensen!"]
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
        "typ": "kod",
        "fraga": "Skapa en variabel som heter 'kurs' och tilldela den strängen 'Programmering 1', skriv sedan ut den.",
        "tips": "kurs = \"...\" och print(kurs)",
        "nyckelord": ["kurs", "=", "print"]
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
        "typ": "kod",
        "fraga": "Skriv kod som räknar ut resten av 17 delat med 4 med modulo-operatorn (%) och skriver ut det.",
        "tips": "print(17 % 4)",
        "nyckelord": ["print", "17", "%", "4"]
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
        "typ": "kod",
        "fraga": "Skriv kod som frågar efter ålder med input(), konverterar till heltal med int() och sparar i 'ålder'.",
        "tips": "ålder = int(input(...))",
        "nyckelord": ["input", "int", "ålder"]
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
        "typ": "kod",
        "fraga": "Skriv en if-sats som kollar om 'poäng' är >= 50. Om sant, skriv ut 'Godkänt'.",
        "tips": "if poäng >= 50: print('Godkänt')",
        "nyckelord": ["if", "poäng", ">=", "print", "Godkänt"]
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
        "typ": "kod",
        "fraga": "Skriv en while-loop som körs så länge 'x < 3' och skriver ut x.",
        "tips": "while x < 3: print(x)",
        "nyckelord": ["while", "x < 3", "print"]
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
        "typ": "kod",
        "fraga": "Skriv kod som skapar en tom lista 'frukter', och lägger till strängen 'Äpple' med append().",
        "tips": "frukter = [] och frukter.append('Äpple')",
        "nyckelord": ["frukter", "[]", "append", "Äpple"]
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
        "typ": "kod",
        "fraga": "Givet listan tal = [10, 20, 30, 40, 50], skriv kod som plockar ut [20, 30, 40] med slicing.",
        "tips": "tal[1:4]",
        "nyckelord": ["tal", "[1:4]"]
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
        "typ": "kod",
        "fraga": "Skriv en funktion som heter 'plus' som tar emot två parametrar (a och b) och returnerar summan.",
        "tips": "def plus(a, b): return a + b",
        "nyckelord": ["def", "plus", "return", "+"]
    }
]

def kor_quiz():
    print("=" * 65)
    print("  VÄLKOMMEN TILL PYTHON TEORIQUIZ & KODLABB (LEKTION 1-9)")
    print("=" * 65)
    
    print("\nVälj träningsläge:")
    print("0. Alla övningar (Blandat)")
    for i in range(1, 10):
        print(f"{i}. Lektion {i} (Teori & Kod)")
    
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
