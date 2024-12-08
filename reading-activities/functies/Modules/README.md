# 1 start met deze code
Hiermee ben je geëindigd in uitbreiding 2


#De omtrek en oppervlakte van een cirkel berekenen

#gegevens
straal = float(input("Geef de straal van de cirkel "))
PI = 3.1415926

#berekeningen
omtrek = 2*PI*straal
oppervlakte = PI*straal**2

#output
print("Voor een cirkel met een straal ",straal,"cm",sep="",end=" ")
print("is de omtrek ",round(omtrek,5),"cm",sep="",end=" ")
print("en de oppervlakte ",round(oppervlakte,5),"cm²",sep="",end="\nEinde programma")

# aanpassing pi voorbeeld 1
#De omtrek en oppervlakte van een cirkel berekenen

import math

#gegevens
straal = float(input("Geef de straal van de cirkel "))


#berekeningen
omtrek = 2*math.pi*straal
oppervlakte = math.pi*straal**2

#output
print("Voor een cirkel met een straal ",straal,"cm",sep="",end=" ")
print("is de omtrek ",round(omtrek,5),"cm",sep="",end=" ")
print("en de oppervlakte ",round(oppervlakte,5),"cm²",sep="",end="\nEinde programma")



# aanpassing pi voorbeeld 2
#De omtrek en oppervlakte van een cirkel berekenen

from math import pi

#gegevens
straal = float(input("Geef de straal van de cirkel "))


#berekeningen
omtrek = 2*pi*straal
oppervlakte = pi*straal**2

#output
print("Voor een cirkel met een straal ",straal,"cm",sep="",end=" ")
print("is de omtrek ",round(omtrek,5),"cm",sep="",end=" ")
print("en de oppervlakte ",round(oppervlakte,5),"cm²",sep="",end="\nEinde programma")

# aanpassing volgens import pcinput 
#De omtrek en oppervlakte van een cirkel berekenen

from math import pi
import pcinput

#gegevens
straal = pcinput.getFloat("Geef de straal van de cirkel ")


#berekeningen
omtrek = 2*pi*straal
oppervlakte = pi*straal**2

#output
print("Voor een cirkel met een straal ",straal,"cm",sep="",end=" ")
print("is de omtrek ",round(omtrek,5),"cm",sep="",end=" ")
print("en de oppervlakte ",round(oppervlakte,5),"cm²",sep="",end="\nEinde programma")

# aanpassing volgens from ... import
#De omtrek en oppervlakte van een cirkel berekenen

from math import pi
from pcinput import getFloat

#gegevens
straal = getFloat("Geef de straal van de cirkel ")


#berekeningen
omtrek = 2*pi*straal
oppervlakte = pi*straal**2

#output
print("Voor een cirkel met een straal ",straal,"cm",sep="",end=" ")
print("is de omtrek ",round(omtrek,5),"cm",sep="",end=" ")
print("en de oppervlakte ",round(oppervlakte,5),"cm²",sep="",end="\nEinde programma")






