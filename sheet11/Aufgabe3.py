def quick_sort(liste):
    # Abbruchbedingung: Listen mit 0 oder 1 Element sind bereits sortiert
    if len(liste) <= 1:
        return liste
    
    # Wahl des Pivot-Elements (hier das mittlere Element)
    pivot = liste[len(liste) // 2]
    
    # Partitionierung der Liste in drei Teile:
    # 1. Alle Elemente kleiner als das Pivot
    links = [x for x in liste if x < pivot]
    # 2. Alle Elemente gleich dem Pivot (behandelt Duplikate)
    mitte = [x for x in liste if x == pivot]
    # 3. Alle Elemente größer als das Pivot
    rechts = [x for x in liste if x > pivot]
    
    # Rekursiver Aufruf für die linke und rechte Teilseite
    # und Zusammenfügen der Teilergebnisse
    return quick_sort(links) + mitte + quick_sort(rechts)

# Beispiel zur Überprüfung:
unsortiert = [3, 6, 8, 10, 1, 2, 1]
sortiert = quick_sort(unsortiert)
print(f"Unsortiert: {unsortiert}")
print(f"Sortiert:   {sortiert}")