getal = int(input("Geef een getal: "))

while getal < 1 or getal > 65:
    getal = int(input("Te klein of te groot. Geef een correct getal: "))
kleinste = getal
teller = 1


while teller < 20:
    getal = int(input("Geef een getal: "))
    while getal < 1 or getal > 65:
        getal = int(input("Te klein of te groot. Geef een correct getal: "))
    if getal < kleinste:
        kleinste = getal
    teller += 1
print("Het kleinste getal bedraagt", str(kleinste)+".\nKlaar" )
