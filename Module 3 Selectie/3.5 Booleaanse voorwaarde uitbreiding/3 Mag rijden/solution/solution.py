leeftijd = int(input("Wat is je leeftijd? "))
rijbewijs = input("Heb je een vast rijbewijs? (ja of nee): ")

if leeftijd >=18 and rijbewijs == "ja":
    print("Je mag alleen met de auto rijden.")
else:
    print("Je mag niet met de auto rijden.")
               
