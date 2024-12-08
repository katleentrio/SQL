# Voorkennis
- Python bevat al een heel aantal standaardfuncties. Om de omgeving niet al te veel te overladen, worden een reeks andere functies niet standaard opgenomen in Python, maar worden die functies ondergebracht in Modules of bibliotheken.
- Modules moeten door de gebruiker opgeroepen worden, pas dan kunnen de functies uit de module gebruikt worden. We werkten al met 1 modules die voor de wiskunde nuttig kunnen zijn namelijk de module math (bevat wiskundige functies zoals sqrt, exp, log, sin, cos, tan, asin, acos, atan, …)
  
# De module math

**Voorbeeld 1**
![image](image.png)

**Output**
![image](image_3.png)

# Gericht een functie oproepen

**Voorbeeld 2**
![image](image_2.png)
**Output**
![image](image_3.png)

Analyseer bovenstaande voorbeelden even. 
- In het eerste voorbeeld zie je *import math* als uitgangspunt. In je code gebruik je *math.sqrt(prompt)*
- In het tweede voorbeeld zie je *from math import sqrt* als uitgangspunt. In je code gebruik je *sqrt(prompt)*

Beide voorbeelden geven hetzelfde resultaat. Afhankelijk van je doel, kies je welke methode je gebruikt. Wanneer je maar 1 argument van de hele module nodig hebt, gebruik dan bij voorkeur de tweede methode.


# Aanpassen
Pas nu jouw code in main.py aan zodat je jouw variabele PI verandert naar de pi uit de math module. Dit is dan zelfs nauwkeuriger omdat pi natuurlijk gekend is met meer cijfers na de komma dan we zelf als constante hebben ingegeven.

**Volgens voorbeeld 1**
![image](image_5.png)

**Volgens voorbeeld 2**
![image](image_4.png)

Heb je gemerkt dat de variabele PI als contante in hoofdletters was en de opgeroepen pi in kleine letters?


# De module random
Hetzelfde verhaal geldt voor de *random* module.
Deze module genereert een willekeurig getal, al dan door jouw aangegeven parameters.

**Voorbeeld 1**
![image](image_6.png)
**Voorbeeld 2**
![image](image_7.png)
**Output**
![image](image_8.png)

# De module pcinput

Tot nu toe zijn we er steeds vanuit gegaan dat de gebruiker naadloos onze gevraagde waarden ingeeft (bvb een 5 bij een geheel getal, een 3.6 bij een float getal, ...).
Wanneer de gebruiker dat niet doet, kan het ingeven van waarden tot foutmeldingen leiden als de gebruiker niet het type object ingeeft dat verwacht wordt.
Dat kan opgevangen worden door extra functies te gebruiken die zelf gedefinieerd zijn en in een module verzameld werden. Die module heet **pcinput.py**.
Deze module staat niet automatisch in de database van python en moeten we handmatig toevoegen.
Wil je deze module gebruiken in combinatie met het programma Thonny, moet je de module ook daar in de *Lib*-file gaan plaatsen of in dezelfde map als deze waar je de programma’s onder brengt die de module zullen gebruiken.
Ook in Replit zie je dat de leerkracht deze module heeft klaargezet om te gebruiken. Kijk maar eens aan de linkerkant in het navigatievenster en zoek **pcinput.py**.



Volgende functies zijn aanwezig: getFloat(), getInteger(), getString(), getLetter(). Wat je daarbij moet ingeven komt overeen met de originele functie input() en eventueel de type casting.

Geeft een gebruiker niet het verwachte object in, dan komt geen foutmelding maar een melding dat het object niet past, en kan er een nieuwe poging ondernomen worden.

**Voorbeeld**

![image](image_9.png)

**Output**

![image](image_10.png)

## Aanpassen
Pas nu jouw code in main.py aan zodat je via de module pcinput de functie getFloat gebruikt.

**Volgens voorbeeld 1**
![image](image_12.png)

**Volgens voorbeeld 2**
![image](image_13.png)