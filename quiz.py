# -*- coding: utf-8 -*-
"""
Teoriquiz & Kodlabb i Python - Programmering 1 (Lektion 1-9)
Körs direkt i terminalen eller VS Code: python quiz.py
"""

import random

# Flervalsfrågor (Teori & Kodspårning)
flervalsfragor = [
    {
        "lektion": "Lektion 1",
        "fraga": "Vad är skillnaden mellan en interpretator och en kompilator?",
        "alternativ": [
            "A) Interpretatorn översätter rad för rad under körning; kompilatorn översätter hela programmet till en körbar fil",
            "B) Kompilatorn översätter rad för rad; interpretatorn skapar en .exe-fil",
            "C) Python använder enbart kompilator precis som C++",
            "D) Det är två ord för exakt samma sak"
        ],
        "ratt": "A",
        "forklaring": "Python är ett interpreterat språk där tolken översätter koden rad för rad när programmet körs."
    },
    {
        "lektion": "Lektion 2",
        "fraga": "Vad skriver print(8 * 2 * (5 - 3) + 16 / 4 - 1) ut?",
        "alternativ": [
            "A) 11.0",
            "B) 35.0",
            "C) 39.0",
            "D) 24.0"
        ],
        "ratt": "B",
        "forklaring": "Parentesen (5-3)=2 beräknas först. Sedan 8*2*2=32 och 16/4=4.0. Slutligen 32 + 4.0 - 1 = 35.0."
    },
    {
        "lektion": "Lektion 2",
        "fraga": "Vilket av följande värden ger False när man kör bool(värde)?",
        "alternativ": [
            "A) bool('False')",
            "B) bool(-1)",
            "C) bool(0)",
            "D) bool('0')"
        ],
        "ratt": "C",
        "forklaring": "Alla tal utom 0 är True, och alla strängar som inte är tomma ('') är True."
    },
    {
        "lektion": "Lektion 3",
        "fraga": "Vad skriver print(9 / 2, 'och', 9 // 2) ut?",
        "alternativ": [
            "A) 4 och 4.5",
            "B) 4.5 och 4",
            "C) 4.5 och 5",
            "D) 4.0 och 4"
        ],
        "ratt": "B",
        "forklaring": "/ utför vanlig division (4.5) medan // utför heltalsdivision och kapar decimalerna (4)."
    },
    {
        "lektion": "Lektion 4",
        "fraga": "Om användaren matar in 8 i: tal = input('Tal: ') och vi kör print(5 * tal), vad skrivs ut?",
        "alternativ": [
            "A) 40",
            "B) 88888",
            "C) 58",
            "D) TypeError"
        ],
        "ratt": "B",
        "forklaring": "input() ger alltid en sträng (str) om man inte omvandlar med int() eller float(). 5 * '8' blir '88888'."
    },
    {
        "lektion": "Lektion 4 & 5",
        "fraga": "Vilka tal skrivs ut av: for n in range(1, 10, 3): print(n) ?",
        "alternativ": [
            "A) 1, 4, 7, 10",
            "B) 1, 4, 7",
            "C) 1, 3, 6, 9",
            "D) 0, 3, 6, 9"
        ],
        "ratt": "B",
        "forklaring": "Startvärdet är 1, steglängden är 3 (1, 4, 7) och slutvärdet 10 inkluderas inte."
    },
    {
        "lektion": "Lektion 7",
        "fraga": "Vad är skillnaden mellan break och continue i en loop?",
        "alternativ": [
            "A) break avslutar hela loopen direkt; continue hoppar bara över resten av nuvarande varv och går till nästa",
            "B) continue avslutar hela programmet; break hoppar till nästa varv",
            "C) break fungerar bara i for-loopar och continue bara i while-loopar",
            "D) De gör exakt samma sak"
        ],
        "ratt": "A",
        "forklaring": "break bryter ut ur hela slingan, medan continue stoppar nuvarande iteration och fortsätter med nästa."
    },
    {
        "lektion": "Lektion 7",
        "fraga": "Vilken listmetod tar bort ett element baserat på dess INDEX respektive dess VÄRDE?",
        "alternativ": [
            "A) remove(index) och pop(värde)",
            "B) pop(index) och remove(värde)",
            "C) clear(index) och delete(värde)",
            "D) insert(index) och append(värde)"
        ],
        "ratt": "B",
        "forklaring": "I pop() anger man indexnumret (t.ex. cars.pop(0)), och i remove() anger man värdet (t.ex. cars.remove('Volvo'))."
    },
    {
        "lektion": "Lektion 8",
        "fraga": "Om lista = [1, 4, 9, 16, 25, 90], vad ger print(lista[2:4]) ?",
        "alternativ": [
            "A) [4, 9, 16]",
            "B) [9, 16]",
            "C) [9, 16, 25]",
            "D) [1, 4]"
        ],
        "ratt": "B",
        "forklaring": "lista[2:4] tar elementen från och med index 2 fram till index 4 (index 4 inkluderas inte)."
    },
    {
        "lektion": "Lektion 9",
        "fraga": "Vad skriver koden ut?\ndef calc(a, b):\n    return a * b + a\nprint(calc(4, 5))",
        "alternativ": [
            "A) 20",
            "B) 24",
            "C) 25",
            "D) 9"
        ],
        "ratt": "B",
        "forklaring": "Funktionen beräknar 4 * 5 + 4 = 24 och returnerar värdet."
    }
]

# Kodlabb-utmaningar (skriv själv)
kodutmaningar = [
    {
        "lektion": "Kodlabb (Lektion 9)",
        "uppgift": "Skriv en funktion som heter 'plus' som tar emot två parametrar (a och b), adderar dem och returnerar summan.",
        "tips": "Använd nyckelorden def, plus, return och +",
        "nyckelord": ["def", "plus", "return", "+"]
    },
    {
        "lektion": "Kodlabb (Lektion 4)",
        "uppgift": "Skriv en for-loop som skriver ut alla tal från 1 till 5 med range().",
        "tips": "Använd for, range(1, 6) och print",
        "nyckelord": ["for", "range", "print"]
    }
]

def kor_quiz():
    print("=" * 65)
    print("  VÄLKOMMEN TILL PYTHON TEORIQUIZ & KODLABB (LEKTION 1-9)")
    print("=" * 65)
    
    print("\nVälj läge:")
    print("1. Teoretiskt flervalsquiz")
    print("2. Kodlabb (skriv kod själv)")
    val = input("Ditt val (1 eller 2): ").strip()

    if val == "2":
        print("\n" + "=" * 50)
        print("  KODLABB: SKRIV KOD SJÄLV")
        print("=" * 50)
        for i, u in enumerate(kodutmaningar, 1):
            print(f"\n[Utmaning {i}] {u['lektion']}")
            print(u['uppgift'])
            print(f"Tips: {u['tips']}")
            print("-" * 40)
            svar = input("Skriv ditt lösningsförslag här:\n> ").strip()
            
            godkand = all(kw.lower() in svar.lower() for kw in u['nyckelord'])
            if godkand:
                print("✅ Snyggt! Din kod innehåller rätt nyckelord.")
            else:
                print("❌ Din kod saknade några viktiga delar.")
        return

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
