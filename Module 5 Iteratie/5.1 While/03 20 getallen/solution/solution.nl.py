getal = None
hoogste = 0
teller = 1

while teller <= 20:
    getal = int(input("Geef een getal: "))
    if getal > hoogste:
        hoogste = getal
    teller += 1
print("Het grootste getal bedraagt", str(hoogste)+".\nKlaar" )
