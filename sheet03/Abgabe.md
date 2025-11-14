# Abgabe3


## Aufgabe1
Darstellung der Zahl $314_{10}$
```
|Rechnung|Rest|
|314/3 = 104|2|
|104/3 = 34|2|
|34/3 = 11|1|
|11/3 = 3|2|
|3/3 = 1|0|
|1/3 = 0|1|
```
Nun werden die Reste von unten nach oben gereiht, wordurch das die neue Zahl ist
```
102122_3
```
Dastellung der Zahl $10011111_2$
```
|Binär|Hexadezimal|
|1001|9|
|1111|F|
```
Der Zahlenblock wird aufgeteilt in 4er Blöcken und anschließend werden die Zahlen dem Hexadezimal zugeordnet
```
9F_16
```
Dastellung der Zahl $521_6$
```
521_6 = 5 * 6^2 + 2*6^1 + 1*6^0 = 193_10$
|Rechnung|Rest|
|193/14 = 13|11|
|13/14 = 0|13|
```
Zuerst wird die Zahl in Dezimal angegeben und anschließend wird wie bei Teilaufgabe 1 vorgegangen.
```
DB_14
```
wobei D für 13 und B für 11 steht
Darstellung von $161_7$
```
161_7 = 1 * 7^2 + 6 * 7^1 + 1 * 7^0 = 92_10
|Rechnung|Rest|
|92/9 = 10|2|
|10/9 = 1|1|
|1/9 = 0|1|
```
Wieder gleiches Prozedere wie darüber
```
112_9
```
## Aufgabe2

```
        wget https://upload.wikimedia.org/wikipedia/commons/3/3f/Albert_Einstein_1921_by_F_Schmutzer.jpg
```

Dies Spechert die Datei in dem Ordner in welchem man sich gerade befindet.

Es handelt sich um Albert Einstein er hat die Äquivalenz von der Masse und der Energie aufgestellt: $E=mc^2$.

```
    convert Albert_Einstein_1921_by_F_Schmutzer.jpg Albert_Einstein_1921_by_F_Schmutzer.png
```

Dies kann verwendet werden um das Bild zu Konvertieren und eine kopie des neuen Dateityps zu erstellen.

Die größe der beiden Dateien wird über folgenden befehl ausgegeben:

```
    du -sh *
```
Der Output war
```
    2.4M    Albert_Einstein_1921_by_F_Schmutzer.jpg
    3.9M    Albert_Einstein_1921_by_F_Schmutzer.png
```
Diese sind unterschiedlich groß da sie unterschiedlich komprimiert sind, .png dateien sind so komprimiert dass keine dateien verloren gehen (Orginaldatei bleibt erhalten).
.jpg Dateien sind anders komprimiert sie nutzen das "lossy compression" system wo manche Daten verlroen gehen.

## Aufgabe 3

```cat foo.txt``` kann lediglich von pstaerk und cgl21-001 ausgeführt werden da foo.txt lediglich von usern die der cgl group angehören geöffnet werden kann.

Für ```cp bar.txt cglstuff/```  gilt das selbe da dies auch nur von cgl verwendert werden kann. 
Für das letzte gilt genau das gleiche. 


