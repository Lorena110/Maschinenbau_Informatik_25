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