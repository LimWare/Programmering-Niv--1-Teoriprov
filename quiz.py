# -*- coding: utf-8 -*-
"""
Teoriquiz & Kodlabb i Python - Programmering 1 (Lektion 1-9)
Körs direkt i terminalen eller VS Code: python quiz.py
"""

import random

# Flervalsfrågor (Teori & Kodspårning)
flervalsfragor = [
    # LEKTION 1
    {
        "lektion": "Lektion 1",
        "fraga": "Vad kallas datorns grundspråk som består av ettor och nollor och som CPU:n direkt kan tolka?",
        "alternativ": [
            "A) Assembleringsspråk",
            "B) Maskinkod",
            "C) Högnivåspråk",
            "D) Källkod"
        ],
        "ratt": "B",
        "forklaring": "Maskinkod består av ettor och nollor som hårdvaran direkt förstår."
    },
    {
        "lektion": "Lektion 1",
        "fraga": "Vad är skillnaden mellan en interpretator och en kompilator?",
        "alternativ": [
            "A) En interpretator tolkar koden rad för rad under körning, medan en kompilator översätter hela programmet i förväg",
            "B) En kompilator används bara i Python",
            "C) En interpretator skapar alltid en .exe-fil",
            "D) Det betyder samma sak"
        ],
        "ratt": "A",
        "forklaring": "Python är ett tolkande (interpreterat) språk."
    },
    {
        "lektion": "Lektion 1",
        "fraga": "Vad kallas processen att hitta och åtgärda fel i ett program?",
        "alternativ": [
            "A) Kompilering",
            "B) Debugging",
            "C) Indentering",
            "D) Syntaxering"
        ],
        "ratt": "B",
        "forklaring": "Debugging är felsökning av kod."
    },

    # LEKTION 2 & 3
    {
        "lektion": "Lektion 2",
        "fraga": "Vilket av följande variabelnamn är TILLÅTET i Python?",
        "alternativ": [
            "A) 1_variabel",
            "B) min variabel",
            "C) min_variabel_1",
            "D) min-variabel!"
        ],
        "ratt": "C",
        "forklaring": "Variabelnamn får innehålla understreck (_) och siffror, men får inte börja med en siffra eller innehålla mellanslag/bindestreck."
    },
    {
        "lektion": "Lektion 2",
        "fraga": "Vilken datatyp får variabeln x i koden: x = 13.5",
        "alternativ": [
            "A) int",
            "B) float",
            "C) str",
            "D) bool"
        ],
        "ratt": "B",
        "forklaring": "Tal med decimalpunkt är av datatypen float."
    },
    {
        "lektion": "Lektion 3",
        "fraga": "Vad skriver koden ut: print(9 // 2)",
        "alternativ": [
            "A) 4.5",
            "B) 4",
            "C) 5",
            "D) 4.0"
        ],
        "ratt": "B",
        "forklaring": "Operatorn // utför heltalsdivision och kastar bort eventuella decimaler."
    },
    {
        "lektion": "Lektion 3",
        "fraga": "Vad beräknar uttrycket 2 ** 3 i Python?",
        "alternativ": [
            "A) 2 gånger 3",
            "B) 2 upphöjt till 3 (8)",
            "C) 2 dividerat med 3",
            "D) Resten av 2 / 3"
        ],
        "ratt": "B",
        "forklaring": "** är potensoperatorn (2 * 2 * 2 = 8)."
    },

    # LEKTION 4 & 5
    {
        "lektion": "Lektion 4",
        "fraga": "Vad returnerar alltid funktionen input() i Python?",
        "alternativ": [
            "A) Ett heltal (int)",
            "B) En sträng (str)",
            "C) Ett flyttal (float)",
            "D) Ett booleskt värde"
        ],
        "ratt": "B",
        "forklaring": "input() ger alltid en sträng, varför man ofta behöver konvertera med int() eller float()."
    },
    {
        "lektion": "Lektion 4",
        "fraga": "Vilka tal genererar funktionen range(1, 6)?",
        "alternativ": [
            "A) 1, 2, 3, 4, 5, 6",
            "B) 0, 1, 2, 3, 4, 5",
            "C) 1, 2, 3, 4, 5",
            "D) 2, 3, 4, 5"
        ],
        "ratt": "C",
        "forklaring": "Startvärdet 1 ingår, men slutvärdet (6) inkluderas ej."
    },
    {
        "lektion": "Lektion 5",
        "fraga": "Vilket tecken används för att kontrollera likhet i en if-sats?",
        "alternativ": [
            "A) =",
            "B) ==",
            "C) ===",
            "D) !="
        ],
        "ratt": "B",
        "forklaring": "== används för jämförelse, medan enkelt = används för variabeltilldelning."
    },
    {
        "lektion": "Lektion 5",
        "fraga": "Vilket nyckelord används för flera alternativa villkor efter en if-sats?",
        "alternativ": [
            "A) else if",
            "B) elif",
            "C) case",
            "D) elseif"
        ],
        "ratt": "B",
        "forklaring": "I Python förkortas else if till elif."
    },

    # LEKTION 6 & 7
    {
        "lektion": "Lektion 6",
        "fraga": "När avbryts en while-loop automatiskt?",
        "alternativ": [
            "A) När dess villkor blir False",
            "B) Efter 10 varv",
            "C) Vid mellanslag",
            "D) Aldrig"
        ],
        "ratt": "A",
        "forklaring": "En while-loop fortsätter så länge villkoret är True."
    },
    {
        "lektion": "Lektion 7",
        "fraga": "Vad gör nyckelordet break i en loop?",
        "alternativ": [
            "A) Avbryter hela loopen omedelbart",
            "B) Hoppar över nuvarande varv",
            "C) Pausar programmet",
            "D) Startar om loopen"
        ],
        "ratt": "A",
        "forklaring": "break avbryter loopen helt och hållet."
    },
    {
        "lektion": "Lektion 7",
        "fraga": "Vilken listmetod lägger till ett element sist i en lista?",
        "alternativ": [
            "A) add()",
            "B) append()",
            "C) insert()",
            "D) push()"
        ],
        "ratt": "B",
        "forklaring": "append() lägger till elementet längst bak i listan."
    },

    # LEKTION 8
    {
        "lektion": "Lektion 8",
        "fraga": "Om lista = [10, 20, 30, 40, 50], vad ger print(lista[1:4])?",
        "alternativ": [
            "A) [20, 30, 40]",
            "B) [10, 20, 30]",
            "C) [20, 30, 40, 50]",
            "D) [30, 40]"
        ],
        "ratt": "A",
        "forklaring": "Slicing [1:4] tar index 1, 2 och 3 (index 4 inkluderas ej)."
    },
    {
        "lektion": "Lektion 8",
        "fraga": "Hur importerar man matematikmodulen i Python?",
        "alternativ": [
            "A) include math",
            "B) import math",
            "C) using math",
            "D) math.load()"
        ],
        "ratt": "B",
        "forklaring": "Moduler importeras med nyckelordet import."
    },

    # LEKTION 9
    {
        "lektion": "Lektion 9",
        "fraga": "Vilket nyckelord används för att definiera en egen funktion i Python?",
        "alternativ": [
            "A) function",
            "B) def",
            "C) fun",
            "D) define"
        ],
        "ratt": "B",
        "forklaring": "Funktioner definieras med nyckelordet def."
    },
    {
        "lektion": "Lektion 9",
        "fraga": "Vad händer om en funktion saknar en return-sats?",
        "alternativ": [
            "A) Den kraschar",
            "B) Den returnerar automatiskt None",
            "C) Den returnerar 0",
            "D) Den körs inte"
        ],
        "ratt": "B",
        "forklaring": "Funktioner som saknar return returnerar värdet None."
    }
]

# Kodlabb-utmaningar
kodutmaningar = [
    {
        "lektion": "Kodlabb (Lätt) – Utskrift",
        "uppgift": "Skriv kod som skriver ut texten 'Hej Jensen!' på skärmen med print().",
        "tips": "Använd print(\"...\")",
        "nyckelord": ["print", "Hej Jensen!"]
    },
    {
        "lektion": "Kodlabb (Medel) – For-loop & Range",
        "uppgift": "Skriv en for-loop som skriver ut alla tal från 1 till 5 (använd range och print).",
        "tips": "Använd for, range(1, 6) och print",
        "nyckelord": ["for", "range", "print"]
    },
    {
        "lektion": "Kodlabb (Svår) – Egen Funktion",
        "uppgift": "Skriv en funktion som heter 'plus' som tar emot två parametrar (a och b), adderar dem och returnerar summan.",
        "tips": "Använd nyckelorden def, plus, return och +",
        "nyckelord": ["def", "plus", "return", "+"]
    }
]

def kor_quiz():
    print("=" * 65)
    print("  VÄLKOMMEN TILL PYTHON TEORIQUIZ & KODLABB (LEKTION 1-9)")
    print("=" * 65)
    
    print("\nVälj träningsläge:")
    print("1. Teoretiskt flervalsquiz")
    print("2. Kodlabb (skriv kod själv)")
    val = input("Ditt val (1 eller 2): ").strip()

    if val == "2":
        print("\n" + "=" * 55)
        print("  KODLABB: SKRIV KOD SJÄLV")
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
