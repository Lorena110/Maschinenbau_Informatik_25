#CNC-Werkzeugwechsel
magazin = [101, 205, 310, 405, 210, 115, 320]
gesuchte_id = int(input("Gesuchte Werkzeug-ID: "))
print(f"Werkzeugmagazin: {magazin}")
print("-------------------------")


for position, werkzeug_id in enumerate(magazin, start=1):
    status = "Gefunden" if werkzeug_id == {gesuchte_id}
    else "NEIN"
    print(f"Position {position}: {gesuchte_id} {status}")