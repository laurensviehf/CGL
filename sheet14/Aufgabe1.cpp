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