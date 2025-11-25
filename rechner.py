# Einfacher Taschenrechner für zwei Zahlen
#Dieses Programm addiert zwei Benutzer eingegebene Zahlen

#Begrüßung
print("Willkommen beim Python-Taschenrechner!")
print ("-" *40)

#Erste Zahl einlesen
zahl1 = float(input("Gib die erste Zahl ein: "))

#Zweite Zahl einlesen
zahl2 = float(input("Gib die zweite Zahl ein: "))

#Berechnungen durchführen
summe = zahl1 +zahl2
differenz = zahl1 -zahl2
produkt= zahl1*zahl2
quotient = zahl1 /zahl2

#Ergebnisse ausgeben
print("-"*40)
print("Ergebnisse:")
print(f"(zahl1)+(zahl2)=(summe)")
print(f"(zahl1)-(zahl2)=(differenz)")
