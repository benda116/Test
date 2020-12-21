print("Načítání programu, prosím čekejte...")

print("Vyberte předmět(napiště jméno)")

jmeno = input()

print("Vybral/a jste si " + jmeno)

print("Vyberte obtížnost(1-3):")

obtiznost = input()

if obtiznost == "1":
    if jmeno == "Matematika":
        print("Vyřešte příklady:")
        print("10 + 45")
        vysledek1 = input()
        if vysledek1 == "55":
            print("Správně")
        else:
            print("Špatně")
        print("21 + 46")
        vysledek2 = input()
        if vysledek2 == "67":
            print("Správně")
        else:
            print("Špatně") 
            print("Konec, děkuji za test :D")
 
    if jmeno == "Čeština":
        print("Doplňte ú/ů")
        print("Dostal jsem hodně _kolů.")

        cjvysledek1 = input()

        if cjvysledek1 == "ú":
            print("Správně")
        else:
            print("Špatně")
 
        print("Tohle je velmi _zké")

        cjvysledek2 = input()
  
        if cjvysledek2 == "ú":
            print("Správně")
        else:
            print("Špatně")
        print("Děkuji za test :D")

if obtiznost == "2":
    if jmeno == "Matematika":
        print("Vyřešte příklady:")
        print("452 + 397")

        vysledek1 = input()
 
        if vysledek1 == "849":
            print("Správně")
        else:
            print("Špatně")
 
        print("1285 + 679")
  
        vysledek2 = input()
 
        if vysledek2 == "1 964":
            print("Správně")
        else:
            print("Špatně") 
            print("Konec, děkuji za test :D")
 
    if jmeno == "Čeština":
        print("Doplňte z/s")
        print("Musel jsem to _dvihnout.")

        cjvysledek1 = input()

        if cjvysledek1 == "z":
            print("Správně")
        else:
            print("Špatně")
 
        print("Video mělo 100 _hlédnutí")

        cjvysledek2 = input()
  
        if cjvysledek2 == "z":
            print("Správně")
        else:
            print("Špatně")
        print("Děkuji za test :D")
if obtiznost == "3":
    if jmeno == "Matematika":
        print("Vyřešte příklady:")
        print("42 x 72")

        vysledek1 = input()
 
        if vysledek1 == "3 024":
            print("Správně")
        else:
            print("Špatně")
 
        print("78 x 31")
  
        vysledek2 = input()
 
        if vysledek2 == "2 418":
            print("Správně")
        else:
            print("Špatně") 
            print("Konec, děkuji za test :D")

    if jmeno == "Čeština":
        print("Doplňte y/i")
        print("My jsme byl_ doma.")

        cjvysledek1 = input()

        if cjvysledek1 == "y":
            print("Správně")
        else:
            print("Špatně")
 
        print("Když jsme byl_ doma, stalo se to.")

        cjvysledek2 = input()
  
        if cjvysledek2 == "y":
            print("Správně")
        else:
            print("Špatně")
        print("Děkuji za test :D")

input("Enter pro opuštění") 