def aufgabe1():
    drehzahl = int(input("Aktuelle Spindelzahl (U/min): "))
    if drehzahl >= 3000:
        print("WARNUNG!: Hohe Drehzahl! Werkzeugverschleiß prüfen.")



def aufgabe2():

    # Hydraulikdrucküberwachung
    druck = float(input("Systemdruck (bar): "))
    psi = druck * 14.5038
    if druck < 50:
        print(f"FEHLER: Druck zu niedrig {druck} bar / {psi:.2f} psi. Pumpe prüfen!")
    else:
        print(f"Druck OK {druck} bar / {psi:.2f} psi. System betriebsbereit.")


  


    #Spannungs-Klassifikator
    kraft = float(input("Kraft F (N):"))
    querschnittsfläche = float(input("Querschnittsfläche A (mm²):"))
    Spannung = kraft / querschnittsfläche

