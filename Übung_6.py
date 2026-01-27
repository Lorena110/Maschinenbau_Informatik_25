#Probe
messwerte = [7,2,5,8,11,13]
i = -1
print(messwerte[i])

#Probe_1
messwerte = ["l", "a", "r"]
messwerte2 = ["e", "f"]
i = 1
print(messwerte[i])

messwerte3 = [messwerte,messwerte2]
print(messwerte3)

#Probe_2
messwerte = [7,2,5,8,11,13]
summe = 0
for i in messwerte:
    print(i)
    summe = summe +i    #summe += i
print(f"Summe: {summe}")




#Aufgabe T1
prime_candidate = int(input("Gib eine Zahl ein:"))
if prime_candidate < 2:
    print("keine Primzahl")
else:
    ist_prim = True
    aktueller_teiler = 2
    while aktueller_teiler * aktueller_teiler <= prime_candidate:
        if prime_candidate % aktueller_teiler == 0:
            ist_prim = False
        aktueller_teiler += 1
    if ist_prim:
        print(f"{prime_candidate} es handelt sich um eine Primzahl.")
    else:
        print(f"{prime_candidate} ist keine Primzahl")


        

# CNC-Drehzahl-Sequenz 

print("Drehen-Sequenz (U/min):", end=" ")
for drehen in range(200, 2001, 200):
    print(drehen, end=" ")
print() #Neue Zeile

print("Fräsen-Sequenz (U/min):", end=" ")
for fraesen in range(3000, 10001, 1000):
    print(fraesen, end=" ")
print()

print("Bohren-Sequenz (U/min):", end=" ")
for bohren in range(1000, 5001, 500):
    print(bohren, end=" ")
print()

print("Hochlauf-Test:", end=" ")
for hochlauf in range(0, 1001, 100):
    print(hochlauf, end=" ")
print()

print("Notfall Abbremsen:", end=" ")
for notfall in range(3000, -1, -500):
    print(notfall, end=" ")
print()






# Zahnrad-Übersetzung

# Eingabe der Anzahl der Getriebestufen
n = int(input("Anzahl der Getriebestufen: "))

# Initialisierung der Gesamt-Übersetzung
i_gesamt = 1.0

# Schleife zur Eingabe der Übersetzungen pro Stufe
for stufe in range(1, n + 1):
    i_stufe = float(input(f"Übersetzung Stufe {stufe}: "))
    i_gesamt *= i_stufe

# Berechnung der Ausgangsdrehzahl (Eingangsdrehzahl = 1500 U/min)
n_ein = 1500
n_aus = n_ein / i_gesamt

# Ausgabe
print("───────────────────────────────")
print(f"Gesamt-Übersetzung: {i_gesamt:.2f}")
print(f"Eingangsdrehzahl: {n_ein} U/min")
print(f"Ausgangsdrehzahl: {n_aus:.2f} U/min")

# Zusatzaufgabe: Drehmomentberechnung
M_ein = 50  # Nm
eta = 0.95  # Wirkungsgrad pro Stufe
eta_gesamt = eta ** n
M_aus = M_ein * i_gesamt * eta_gesamt

print(f"Eingangsdrehmoment: {M_ein} Nm")
print(f"Ausgangsdrehmoment: {M_aus:.2f} Nm")