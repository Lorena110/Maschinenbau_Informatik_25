#CNC-Werkzeugwechsel
magazin = [101, 205, 310, 405, 210, 115, 320]
print(f"Werkzeugmagazin: {magazin}")
gesuchte_id = int(input("Gesuchte Werkzeug-ID: "))
print("-------------------------")

for position, werkzeug_id in enumerate(magazin, start=1):
    status = "Gefunden" if werkzeug_id == gesuchte_id else "NEIN"
    print(f"Position {position}: {werkzeug_id} {status}")

    if werkzeug_id == gesuchte_id:
        print("-------------------------")
        print(f"Werkzeug {gesuchte_id} gefunden auf Position {position}")
        print(f"Suchaufwand: {position} geprüft")
        break

else: print("-------------------------")
print(f"Werkzeug {gesuchte_id} nicht im Magazin")
print("Empfehlung: Werkzeug nachladen oder Programm anpassen.")





# Kontinuierliche Drucküberwachung
print("----------------------------")
print("Hydraulikdruck-Überwachung")
print("----------------------------")
print("Normbereich: 50-180 bar")
print("Warnung: 180-250 bar")
print("Alarm: <50 bar oder <250 bar\n")

gueltige_messung = 0
while True:
    eingabe = input("Geben Sie einen Druckwert ein (oder STOP): ")
    if eingabe.upper() == "STOP":
        print("Überwachung beendet.")
        break

    try:   
         druck = float(eingabe)
         if druck < 0:
            print("⚠️  Fehler: Negativer Wert nicht möglich! Sensor defekt.\n")
            continue
         if druck > 300:
            print("⚠️  Fehler: Unrealistischer Wert! Sensor prüfen.\n")
            continue
    except ValueError:
        print("⚠️  Fehler: Ungültiger Wert! Sensor prüfen.\n")
        continue
    
    # Gültige Messung
    gueltige_messungen += 1
    
    # Bewertung
    if druck < 50:
        print(f"🔴 ALARM! Unterdruck: {druck} bar")
        print("SYSTEM WIRD ABGESCHALTET!")
        break
    elif druck >= 250:
        print(f"🔴 ALARM! Überdruck: {druck} bar")
        print("SYSTEM WIRD ABGESCHALTET!")
        break
    elif druck >= 180:
        print(f"🟡 WARNUNG - Druck: {druck} bar (Erhöht)\n")
    else:
        print(f"🟢 OK - Druck: {druck} bar (Normal)\n")

print("─" * 35)
print("Überwachung beendet.")
print(f"Gültige Messungen: {gueltige_messungen}")