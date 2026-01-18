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
