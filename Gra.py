import random
HP = 10
points = 0
wydarzenie = random.choice(["NPC", "diament", "Potwor", "Apteczka", "pusty", "potwor", "potwor", "potwor", "diament", "potwor", "potwor", "potwor", "potwor", "potwor", "potwor", "potwor", "potwor"])
print("Wiaj w labiryncie Diamentow ")
print("musisz miec 10 Points , zanim umrzesz")
print("NA start Masz 10 HP i zero points")
print("Powodzenia !!!\n")
while HP > 0 and points < 10:
    kierunek = input("WYBIERAJ : \n PROSTO - w \n DO TYŁU - s\n W PRAWO - d\n W LEWO - a\n Sklep - q \n Wpisz: ")
    if kierunek == "q":
        if points >= 2:
            print(f"Witaj w sklepie! MASZ {points} Diamentów,\n Możesz kupić: ")
            print("1. Mała potka życia (+1 HP) - koszt 2 diamenty")
            print("2. duza potka życia (+2 HP) - koszt 3 diamenty")
            print("3. Wykrywacz diamentow (zwiększa szanse na diamenta) - koszt 3 diamenty")
            wybor = input("Co chcesz kupić wybierz 1, 2 lub 3 :  ")
            if wybor == "1" and points >= 2:
                points -= 2
                HP += 1
                print("Kupiłeś dużą miksturę życia. Masz teraz", HP)
            elif wybor == "2" and points >= 3:
                points -= 3
                HP += 3
            elif wybor == "3" and points >= 3:
                points -= 3
                wydarzenie.append("diament")
                print("Kupiłeś wykrywacz diametów. Powodzenia w szukaniu!  ")
            else:
                print("Zła odpowiedz lub cie niestac biedaku ")
        else:
            print("Niewejdziesz Niestac cie")
        continue
        
    if wydarzenie == "diament":
        points += 1 
        print(F"Znalazłeś diament! masz teraz {points} ")
    elif wydarzenie == "Potwor":
        HP -= 2
        print(f"O NIE TO POTWOR !!! STRACIŁES 2 HP I MASZ TERAZ {HP}HP :(((((")
    elif wydarzenie == "Apteczka":
        HP += 3
        print(f"Znalazłeś apteczke dzięki niej teraz masz {HP} Hp")
    elif wydarzenie == "NPC":
        npctekst = random.choice(["KUBA JUZYK: WITAJ PSZYBYSZU widziałeś moze moje okulary ?", "KRZYSZTOW KRAWCZYK: Co ty tu robisz?", "SPONGEBOB: POMOCY", "WARDENGA: Uwazaj na potwora ponoc on niegryzie... ON POŁYka w caŁOSCI !!!"])
        print("SPOTKAŁEŚ NPC")
        print(npctekst)
    else:
        print("Nic tu niema idz dalej ")
    print()

if points >= 10:
    print("Gratulacje wygrałeś")
elif HP <= 0:
    print("GAME OVER")
