# Aufgabe 1
- 3+5 gibt 8 als `int`.
- 3 + 5.0 gibt das Ergebnis als `double` (8.0).
- "3" + "5" gibt einen Error da c string nicht addiert werden können.
- std::string("3") + "5" Funktioniert da Strings mit c Strings addiert werden können ("35").
- 3/2 Funktioniert da int mit int geteilt wird, das Ergebnis wird nach unten gerundet und ein `int`.
- 3.0 / 2 identisch zu oben ew wird ein `double` erhalten.
- int(2.71828) funktioniert das Ergebnis ist ein `int` (2) sollte nicht verwendet werden sondern `static_cast<int>(2.71828)`
- std::round(2.71828) rundet die Zahl Ausgabe ist ein `double`.

# Aufgabe 2
Der Compiler compiliert die .cpp file in eine .obj file, der Linker verlinkt alle .obj files und fügt sie zusammen in eine .exe. Dies wird gemacht in dem man auf den run Pfeil clickt.

```cpp
#include <iostream>
#include <time.h>
int main(int argc, char *argv[])
{

    srand(time(NULL));
    int maximum;
    int guess;
    int guess_count = 1;
    int random_number;

    std::cout << "Maximum: ";
    std::cin >> maximum;

    random_number = rand() % maximum;

    do
    {
        std::cout << "Rate welche Zahl: ";
        std::cin >> guess;
        if (guess < random_number)
        {
            std::cout << "Deine Zahl ist zu klein!" << std::endl;
        }
        else if (guess > random_number)
        {
            std::cout << "Deine Zahl ist zu groß!" << std::endl;
        }
        guess_count++;
    } while (guess != random_number);
    std::cout << "Du hast " << guess_count << " Versuche gebraucht" << std::endl;
    return 0;
}
``` 

# Aufgabe 3

Die Funktion wird ein boolschen return geben sprich true oder false.
Die eingaben sind jeweils `int`
```cpp
#include <iostream>
// --- HIER DIE FUNKTION DEFINIEREN ---
bool pruefeTipp(int tipp, int loesung)
{
    if (tipp == loesung)
    {
        std::cout << "Treffer! Gut gemacht." << std::endl;
        return true; // Rückgabe für Erfolg
    }
    else if (tipp > loesung)
    {
        std::cout << "Zu hoch!" << std::endl;
    }
    else
    {
        std::cout << "Zu niedrig!" << std::endl;
    }
    return false; // Rückgabe für "noch nicht gefunden"
}
int main()
{
    int secret = 42; // Beispiel-Zufallszahl
    int guess;
    bool gefunden = false;
    std::cout << "Willkommen zum Zahlen-Raten!" << std::endl;
    while (!gefunden)
    {
        std::cout << "Dein Tipp: ";
        std::cin >> guess;
        // --- HIER DEN FUNKTIONSAUFRUF EINFÜGEN ---
        gefunden = pruefeTipp(guess, secret);
    }
    return 0;
}
```