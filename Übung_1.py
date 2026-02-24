name = "Lorena"
alter = 23
print(f"Hallo, ich bin {name} und bin {alter} Jahre alt")

x = 10
y = 20
print(f"{x} + {y} = {x + y}")

temperatur_celsius = 22.5
temperatur_fahrenheit = temperatur_celsius * 9/5 + 32
print(f"Temperatur: {temperatur_celsius}°C = {temperatur_fahrenheit:.1f}°F")

# Konvertierung von int zu float
zahl_int = 42
zahl_float = float(zahl_int)
print(f"{zahl_int} als int: {zahl_int}, Typ: {type(zahl_int)}")
print(f"{zahl_int} als float: {zahl_float}, Typ: {type(zahl_float)}")


# Konvertierung von float zu int
zahl_float = 3.99
zahl_int = int(zahl_float)
print(f"{zahl_float} als float: {zahl_float}, Typ: {type(zahl_float)}")
print(f"{zahl_float} als int: {zahl_int}")

Wert = 3.14
print("3.14")
print(f"{Wert}, Typ: {type(Wert)}")


# Konvertierung von int zu string
zahl_int = 123
zahl_string = str(zahl_int)
print(f"{zahl_int} als int: {zahl_int}, Typ: {type(zahl_int)}")
print(f"{zahl_int} als string: {zahl_string}, Typ: {type(zahl_string)}")

# Konvertieren von float zu int mit Runden
zahl_float = 3.7
zahl_int_abgeschnitten = int(zahl_float)
zahl_int_gerundet = round(zahl_float)
print(f"{zahl_float} als float: {zahl_float}, Typ: {type(zahl_float)}")
print(f"{zahl_float} abgeschnitten : {zahl_int_abgeschnitten}")
print(f"{zahl_float} gerundet: {zahl_int_gerundet}, Typ: {type(zahl_int_gerundet)}")

Länge = 150 # mm
Kraft = 1500 # N
Dehnung = 0.25 # mm
Berechnung = (Dehnung / Länge *100)
print(f"{Berechnung}")
