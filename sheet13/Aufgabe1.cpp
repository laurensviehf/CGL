#include <iostream>
#include <iomanip>
#include <print>
// Funktion zur Berechnung der Fakultaet k!
long fakultaet(int k)
{
    long result = 1;
    for (long i = 1; i <= k; ++i)
        result *= i;
    return result;
}
// Funktion zur Annaeherung von e durch n Terme
double approximate_e(int n)
{
    double summe = 0.0;
    for (int k = 0; k < n; ++k)
    {
        summe += 1. / fakultaet(k);
    }
    return summe;
}
int main()
{
    int iterationen;
    std::print("Gib hier eine Zahl ein: ");
    std::cin >> iterationen;
    // Berechne e
    double e_approx = approximate_e(iterationen);
    // Ausgabe des Ergebnisses
    std::cout << "Annaeherung von e nach " << iterationen << " Iterationen:" << std::endl;
    std::println("Die Zahl ist: {:.8f}", e_approx);
    // Tipp: Nutze std::setprecision aus <iomanip>
    return 0;
}