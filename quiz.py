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
        "fraga": "Vad är ett assembleringsspråk (Assembly language)?",
        "alternativ": ["A) Ett högnivåspråk för webben", "B) Ett lågnivåspråk där instruktioner skrivs som kort text", "C) Ett program för att köra Python", "D) Datorns binära ettor och nollor"],
        "ratt": "B",
        "forklaring": "Assembly är ett lågnivåspråk nära maskinkod."
    },
    {
        "lektion": "Lektion 1",
        "fraga": "Vad är skillnaden mellan en interpretator och en kompilator?",
        "alternativ": ["A) En interpretator tolkar koden rad för rad under körning, medan en kompilator översätter hela programmet i förväg", "B) En kompilator används bara i Python", "C) En interpretator skapar alltid en .exe-fil", "D) Det betyder samma sak"],
        "ratt": "A",
        "forklaring": "Python är ett tolkande (interpreterat) språk."
    },
    {
        "lektion": "Lektion 1",
        "fraga": "Vad kallas processen att hitta och åtgärda fel i ett program?",
        "alternativ": ["A) Kompilering", "B) Debugging", "C) Indentering", "D) Syntaxering"],
        "ratt": "B",
        "forklaring": "Debugging är felsökning av kod."
    },
    {
        "lektion": "Lektion 1",
        "fraga": "Vem lanserade Python år 1991?",
        "alternativ": ["A) Guido van Rossum", "B) Linus Torvalds", "C) Bill Gates", "D) James Gosling"],
        "ratt": "A",
        "forklaring": "Guido van Rossum skapade och lanserade Python 1991."
    },
    {
        "lektion": "Lektion 1",
        "fraga": "Vad står förkortningen IDE för?",
        "alternativ": ["A) Internal Data Execution", "B) Integrated Development Environment", "C) Interactive Debugging Engine", "D) Internet Document Editor"],
        "ratt": "B",
        "forklaring": "IDE står för Integrated Development Environment (t.ex. VS Code eller PyCharm)."
    },
    {
        "lektion": "Lektion 1",
        "fraga": "Vilken filändelse har standardfiler skrivna i Python?",
        "alternativ": ["A) .pt", "B) .py", "C) .python", "D) .exe"],
        "ratt": "B",
        "forklaring": "Python-filer sparas alltid med filändelsen .py."
    },

    # LEKTION 2 & 3
    {
        "lektion": "Lektion 2",
        "fraga": "Vilket av följande variabelnamn är TILLÅTET i Python?",
        "alternativ": ["A) 1_variabel", "B) min variabel", "C) min_variabel_1", "D) min-variabel!"],
        "ratt": "C",
        "forklaring": "Variabelnamn får innehålla understreck (_) och siffror, men får inte börja med en siffra eller innehålla mellanslag/bindestreck."
    },
    {
        "lektion": "Lektion 2",
        "fraga": "Vilken datatyp får variabeln x i koden: x = 13.5",
        "alternativ": ["A) int", "B) float", "C) str", "D) bool"],
        "ratt": "B",
        "forklaring": "Tal med decimalpunkt är av datatypen float."
    },
    {
        "lektion": "Lektion 2",
        "fraga": "Vad blir datatypen för x i koden: x = 'True'",
        "alternativ": ["A) bool", "B) int", "C) str", "D) float"],
        "ratt": "C",
        "forklaring": "Eftersom värdet omges av citattecken ('True') är det en textsträng (str)."
    },
    {
        "lektion": "Lektion 2",
        "fraga": "Vad skriver följande program ut på skärmen?\nprint(8 * 2 * (5 - 3) + 16 / 4 - 1)",
        "alternativ": ["A) 35.0", "B) 11.0", "C) 39.0", "D) 24.0"],
        "ratt": "A",
        "forklaring": "Parentes först, sedan multiplikation/division från vänster till höger, och sist addition/subtraktion = 35.0."
    },
    {
        "lektion": "Lektion 3",
        "fraga": "Vad skriver koden ut: print(9 // 2)",
        "alternativ": ["A) 4.5", "B) 4", "C) 5", "D) 4.0"],
        "ratt": "B",
        "forklaring": "Operatorn // utför heltalsdivision och kastar bort eventuella decimaler."
    },
    {
        "lektion": "Lektion 3",
        "fraga": "Vad beräknar uttrycket 2 ** 3 i Python?",
        "alternativ": ["A) 2 gånger 3", "B) 2 upphöjt till 3 (8)", "C) 2 dividerat med 3", "D) Resten av 2 / 3"],
        "ratt": "B",
        "forklaring": "** är potensoperatorn (2 * 2 * 2 = 8)."
    },
    {
        "lektion": "Lektion 3",
        "fraga": "Vilket av följande uttryck ger False i Python?",
        "alternativ": ["A) bool(-5)", "B) bool('Hej')", "C) bool(0)", "D) bool('0')"],
        "ratt": "C",
        "forklaring": "Endast talet 0 (samt tomma strängar/listor) ger False."
    },
    {
        "lektion": "Lektion 3",
        "fraga": "Vad beräknar modulo-operatorn (%) i Python?",
        "alternativ": ["A) Vanlig division", "B) Resten vid division", "C) Procent", "D) Multiplikation"],
        "ratt": "B",
        "forklaring": "Modulo (%) returnerar resten av en division (t.ex. 5 % 2 = 1)."
    },
    {
        "lektion": "Lektion 2",
        "fraga": "Vilket specialtecken skapar en ny rad inuti en print-sträng?",
        "alternativ": ["A) \\t", "B) \\n", "C) \\r", "D) \\\\"],
        "ratt": "B",
        "forklaring": "\\n står för ny rad (newline)."
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
        "lektion": "Lektion 4",
        "fraga": "Vilka tal genererar funktionen range(1, 6)?",
        "alternativ": ["A) 1, 2, 3, 4, 5, 6", "B) 0, 1, 2, 3, 4, 5", "C) 1, 2, 3, 4, 5", "D) 2, 3, 4, 5"],
        "ratt": "C",
        "forklaring": "Startvärdet 1 ingår, men slutvärdet (6) inkluderas ej."
    },
    {
        "lektion": "Lektion 4",
        "fraga": "Vilka tal skrivs ut av: for i in range(1, 10, 3): print(i)",
        "alternativ": ["A) 1, 4, 7, 10", "B) 1, 4, 7", "C) 1, 3, 6, 9", "D) 0, 3, 6, 9"],
        "ratt": "B",
        "forklaring": "Start 1, steg 3 upp till 10 ger 1, 4, 7 (10 ingår ej)."
    },
    {
        "lektion": "Lektion 5",
        "fraga": "Vilket tecken används för att kontrollera likhet i en if-sats?",
        "alternativ": ["A) =", "B) ==", "C) ===", "D) !="],
        "ratt": "B",
        "forklaring": "== används för jämförelse, medan enkelt = används för tilldelning."
    },
    {
        "lektion": "Lektion 5",
        "fraga": "Vad saknas i koden: \nif x > 5\n    print('Stort')",
        "alternativ": ["A) Kolon (:) efter villkoret", "B) Parenteser", "C) Else-block", "D) Inget fel"],
        "ratt": "A",
        "forklaring": "if-satser måste alltid avslutas med kolon (:)."
    },
    {
        "lektion": "Lektion 5",
        "fraga": "Vilket nyckelord används för flera alternativa villkor efter en if?",
        "alternativ": ["A) else if", "B) elif", "C) case", "D) elseif"],
        "ratt": "B",
        "forklaring": "I Python förkortas else if till elif."
    },
    {
        "lektion": "Lektion 5",
        "fraga": "Hur skriver man 'inte lika med' i Python?",
        "alternativ": ["A) <>", "B) !=", "C) =/=", "D) NOT"],
        "ratt": "B",
        "forklaring": "'Inte lika med' skrivs med !=."
    },
    {
        "lektion": "Lektion 4",
        "fraga": "Vad gör funktionen round(3.789, 1)?",
        "alternativ": ["A) Avrundar till 1 decimal (3.8)", "B) Avrundar till heltal (4)", "C) Ger ett felmeddelande", "D) Tar bort decimaler"],
        "ratt": "A",
        "forklaring": "round(tal, 1) avrundar till angivet antal decimaler (3.8)."
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
        "lektion": "Lektion 6",
        "fraga": "Varför uppstår en oändlig loop om räknaren inte uppdateras?",
        "alternativ": ["A) Villkoret förblir True för evigt", "B) Python kraschar direkt", "C) Print saknas", "D) Ingen anledning"],
        "ratt": "A",
        "forklaring": "Om villkoret aldrig ändras till False körs loopen i oändlighet."
    },
    {
        "lektion": "Lektion 7",
        "fraga": "Vad gör nyckelordet break i en loop?",
        "alternativ": ["A) Avbryter hela loopen omedelbart", "B) Hoppar över nuvarande varv", "C) Pausar", "D) Startar om"],
        "ratt": "A",
        "forklaring": "break avbryter loopen helt och hållet."
    },
    {
        "lektion": "Lektion 7",
        "fraga": "Vad gör nyckelordet continue i en loop?",
        "alternativ": ["A) Avbryter hela loopen", "B) Hoppar över resten av nuvarande varv och går till nästa", "C) Startar om programmet", "D) Gör ingenting"],
        "ratt": "B",
        "forklaring": "continue hoppar över resten av den aktuella iterationen och fortsätter med nästa varv."
    },
    {
        "lektion": "Lektion 7",
        "fraga": "Vilken listmetod lägger till ett element sist i en lista?",
        "alternativ": ["A) add()", "B) append()", "C) insert()", "D) push()"],
        "ratt": "B",
        "forklaring": "append() lägger till elementet sist."
    },
    {
        "lektion": "Lektion 7",
        "fraga": "Vilket index har det första elementet i en lista i Python?",
        "alternativ": ["A) 1", "B) 0", "C) -1", "D) Inget index"],
        "ratt": "B",
        "forklaring": "Python är nollindexerat (första elementet är index 0)."
    },
    {
        "lektion": "Lektion 7",
        "fraga": "Hur tar man bort ett element baserat på dess INDEX?",
        "alternativ": ["A) pop(index)", "B) remove(index)", "C) clear(index)", "D) delete(index)"],
        "ratt": "A",
        "forklaring": "pop(index) tar bort via indexnummer, remove() tar bort via värde."
    },
    {
        "lektion": "Lektion 7",
        "fraga": "Vilken funktion ger antalet element i en lista?",
        "alternativ": ["A) size()", "B) length()", "C) len()", "D) count()"],
        "ratt": "C",
        "forklaring": "len() returnerar hur många element som finns i en lista eller sträng."
    },

    # LEKTION 8
    {
        "lektion": "Lektion 8",
        "fraga": "Om lista = [10, 20, 30, 40, 50], vad ger print(lista[1:4])?",
        "alternativ": ["A) [20, 30, 40]", "B) [10, 20, 30]", "C) [20, 30, 40, 50]", "D) [30, 40]"],
        "ratt": "A",
        "forklaring": "Slicing [1:4] tar index 1, 2 och 3 (index 4 inkluderas ej)."
    },
    {
        "lektion": "Lektion 8",
        "fraga": "Om land = 'Sverige', vad ger land[:2]?",
        "alternativ": ["A) Sv", "B) Sve", "C) S", "D) verige"],
        "ratt": "A",
        "forklaring": "Tar allt från början fram till index 2 (ej inklusive index 2), dvs 'Sv'."
    },
    {
        "lektion": "Lektion 8",
        "fraga": "Hur importerar man matematikmodulen i Python?",
        "alternativ": ["A) include math", "B) import math", "C) using math", "D) math.load()"],
        "ratt": "B",
        "forklaring": "Moduler importeras med nyckelordet import."
    },
    {
        "lektion": "Lektion 8",
        "fraga": "Hur beräknar man kvadratroten ur 64 efter 'import math'?",
        "alternativ": ["A) math.sqrt(64)", "B) math.root(64)", "C) math.pow(64)", "D) sqrt(64)"],
        "ratt": "A",
        "forklaring": "math.sqrt() beräknar kvadratroten."
    },
    {
        "lektion": "Lektion 8",
        "fraga": "Vilken funktion ger summan av alla tal i en numerisk lista?",
        "alternativ": ["A) total()", "B) add()", "C) sum()", "D) count()"],
        "ratt": "C",
        "forklaring": "sum() summerar alla element i en numerisk lista."
    },
    {
        "lektion": "Lektion 8",
        "fraga": "Vad gör funktionerna min() och max() på en lista med tal?",
        "alternativ": ["A) Tar bort lägsta/högsta talet", "B) Hittar det minsta respektive största värdet i listan", "C) Sorterar listan", "D) Räknar antalet element"],
        "ratt": "B",
        "forklaring": "min() och max() returnerar det minsta respektive största elementet."
    },

    # LEKTION 9
    {
        "lektion": "Lektion 9",
        "fraga": "Vilket nyckelord används för att definiera en egen funktion i Python?",
        "alternativ": ["A) function", "B) def", "C) fun", "D) define"],
        "ratt": "B",
        "forklaring": "Funktioner definieras med nyckelordet def."
    },
    {
        "lektion": "Lektion 9",
        "fraga": "Vad händer om en funktion saknar en return-sats?",
        "alternativ": ["A) Den kraschar", "B) Den returnerar automatiskt None", "C) Den returnerar 0", "D) Den körs inte"],
        "ratt": "B",
        "forklaring": "Funktioner som saknar return returnerar värdet None."
    },
    {
        "lektion": "Lektion 9",
        "fraga": "Vad kallas variablerna inom parenteserna när man skapar en funktion?",
        "alternativ": ["A) Parametrar (eller argument)", "B) Globala variabler", "C) Konstanter", "D) Returvärden"],
        "ratt": "A",
        "forklaring": "Parametrar tar emot inmatningsvärden när funktionen anropas."
    },
    {
        "lektion": "Lektion 9",
        "fraga": "Vad skriver koden ut?\ndef calc(a, b):\n    return a * b + a\nprint(calc(4, 5))",
        "alternativ": ["A) 20", "B) 24", "C) 25", "D) 9"],
        "ratt": "B",
        "forklaring": "Beräknar 4 * 5 + 4 = 24 och returnerar värdet."
    },
    {
        "lektion": "Lektion 9",
        "fraga": "Vad är skillnaden mellan lokala och globala variabler?",
        "alternativ": ["A) Lokala variabler skapas inuti en funktion och nås bara där; globala variabler skapas utanför funktioner och nås i hela programmet", "B) Det är exakt samma sak", "C) Globala variabler kan bara användas i for-loopar", "D) Lokala variabler sparas alltid på hårddisken"],
        "ratt": "A",
        "forklaring": "Lokala variabler existerar endast inne i sin funktion."
    }
]

# Kodlabb-utmaningar (10 st)
kodutmaningar = [
    {
        "lektion": "Kodlabb 1 (Lätt) – Utskrift",
        "uppgift": "Skriv kod som skriver ut texten 'Hej Jensen!' på skärmen med print().",
        "tips": "Använd print(\"...\")",
        "nyckelord": ["print", "Hej Jensen!"]
    },
    {
        "lektion": "Kodlabb 2 (Lätt) – Variabel",
        "uppgift": "Skapa en variabel som heter 'namn' och tilldela den din egen textsträng, skriv sedan ut den med print().",
        "tips": "Använd namn = ... och print(namn)",
        "nyckelord": ["namn", "=", "print"]
    },
    {
        "lektion": "Kodlabb 3 (Medel) – Aritmetik",
        "uppgift": "Skriv kod som beräknar produkten av 12 och 13 och skriver ut resultatet med print().",
        "tips": "Använd print(12 * 13)",
        "nyckelord": ["print", "12", "13", "*"]
    },
    {
        "lektion": "Kodlabb 4 (Medel) – For-loop & Range",
        "uppgift": "Skriv en for-loop som skriver ut alla tal från 1 till 5 (använd range och print).",
        "tips": "Använd for, range(1, 6) och print",
        "nyckelord": ["for", "range", "print"]
    },
    {
        "lektion": "Kodlabb 5 (Medel) – Input & Konvertering",
        "uppgift": "Skriv kod som frågar efter ålder med input(), konverterar till int och sparar i variabeln 'ålder'.",
        "tips": "Använd input(), int() och ålder =",
        "nyckelord": ["input", "int", "ålder"]
    },
    {
        "lektion": "Kodlabb 6 (Medel) – Villkorssats",
        "uppgift": "Skriv en if-sats som kollar om variabeln 'poäng' är >= 50. Om det är sant, skriv ut 'Godkänt'.",
        "tips": "Använd if, poäng, >= och print",
        "nyckelord": ["if", "poäng", ">=", "print", "Godkänt"]
    },
    {
        "lektion": "Kodlabb 7 (Medel) – Listor & Append",
        "uppgift": "Skriv kod som skapar en tom lista 'namn', och lägger till strängen 'Alice' med rätt listmetod.",
        "tips": "Använd [] och append",
        "nyckelord": ["namn", "[]", "append", "Alice"]
    },
    {
        "lektion": "Kodlabb 8 (Svår) – Slicing",
        "uppgift": "Givet listan tal = [10, 20, 30, 40, 50], skriv kod som plockar ut de tre mittersta [20, 30, 40] med slicing.",
        "tips": "Använd tal[1:4]",
        "nyckelord": ["tal", "[1:4]"]
    },
    {
        "lektion": "Kodlabb 9 (Svår) – Egen Funktion",
        "uppgift": "Skriv en funktion som heter 'plus' som tar emot två parametrar (a och b), adderar dem och returnerar summan.",
        "tips": "Använd nyckelorden def, plus, return och +",
        "nyckelord": ["def", "plus", "return", "+"]
    },
    {
        "lektion": "Kodlabb 10 (Svår) – Funktion med villkor",
        "uppgift": "Skriv en funktion 'kolla_tal' som tar in x. Om x > 10 ska den returnera 'Stort', annars 'Litet'.",
        "tips": "Använd def, kolla_tal, if, return",
        "nyckelord": ["def", "kolla_tal", "if", "return", "Stort", "Litet"]
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
