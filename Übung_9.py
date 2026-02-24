#P2 Maschinen-Logfile

datei = open("Maschine_01_log")
inhalt = datei.read()  # Inhalt der Datei lesen
print(inhalt)  # Inhalt auf der Konsole ausgeben
datei.close()  # Datei schließen

