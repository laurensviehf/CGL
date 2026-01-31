# Blatt 14 die letzte

## Aufgabe 1

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <random>
#include <print>

class Person
{
public:
    std::string name;
    int age;
};
bool is_younger(const Person &a, const Person &b)
{
    return a.age <= b.age;
}
int main()
{
    std::vector<Person> people{
        {"Alice", 30},
        {"Bob", 24},
        {"Clara", 41},
        {"Herbert", 56},
        {"Waldtraut", 100}};
    // std::sort mit der Funktion is_younger aufrufen

    std::random_device rd;
    std::mt19937 g(rd());

    int tries = 0;

    while (!std::is_sorted(people.begin(), people.end(), is_younger))
    {
        std::shuffle(people.begin(), people.end(), g);
        tries++;
        std::print("Versuch {}: ", tries);
        for (auto &e : people)
            std::print("{} ", e.age);
        std::println("");
    }
}
```

## Aufgabe 2

```cpp 
#include <iostream>

class Particle {
public:
    double x, y;
    double vx, vy;
    double mass;

    double momentum_x() const {
        return mass * vx;
    }

    double momentum_y() const {
        return mass * vy;
    }
};

int main() {

    Particle p1;

    p1.x = 10.0;
    p1.y = 5.0;
    p1.vx = 2.5;
    p1.vy = -1.2;
    p1.mass = 5.0;

    std::cout << "Impuls in x-Richtung: " << p1.momentum_x() << " kg*m/s" << std::endl;
    std::cout << "Impuls in y-Richtung: " << p1.momentum_y() << " kg*m/s" << std::endl;

    return 0;
}
```

## Aufgabe 3

Es ist wichtig das in dem Repository alles genau begutachtet wird und analysiert wird. Ich wäre glücklich über eine code review. 
Vielen Dank.


 [Hier geht es zu meinem Repository](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
 [link](https://github.com/laurensviehf/cgl-git-uebung)

 [Dies ist die Pull request](https://github.com/tobias-fllnr/cgl-git-uebung/pull/26)

