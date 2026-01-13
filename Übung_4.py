temperatur = float(input("CNC.Kühlmittel-Temperatur (°C): "))
betriebsbereich = ""
idealbereich = ""
empfehlung = ""

if temperatur < 15 :
    betriebsbereich = "Zu kalt: unter 15°C"
    idealbereich = "Nein"
    empfehlung = " Maschine STOPPEN! Kühlmittel erwärmen"

if 15 < temperatur < 20 :
    betriebsbereich = "Suboptimal kühl"
    idealbereich = "Nein"
    empfehlung = " funktionsfähig, aber nicht ideal"


#print(f"CNC-Kühlmittel-Temperatur (°C): {temperatur} ")
print(f"Betriebsbereich:{betriebsbereich}")
print(f"Idealbereich (22-26°C):{idealbereich}")
print(f"Empfehlung:{empfehlung}")