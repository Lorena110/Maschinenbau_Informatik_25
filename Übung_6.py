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