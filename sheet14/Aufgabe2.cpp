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