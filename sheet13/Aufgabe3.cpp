#include <iostream>
#include <vector>
auto scalar_product(const std::vector<double> &vector1,
                    const std::vector<double> &vector2) -> double
{
    if (vector1.size() != vector2.size())
        throw std::runtime_error("Die Vectoren sind nicht gleich lang!");
    if (vector1.empty())
        throw std::runtime_error("Die Vectoren sind leer!");

    auto result = 0.;
    for (size_t i = 0; i < vector1.size(); ++i)
        result += vector1[i] * vector2[i];
    return result;
}
int main()
{
    std::vector<double> v1 = {1.0, 2.0, 3.0, 4.0};
    std::vector<double> v2 = {1.0, -1.0, -1.0, 1.0};
    std::cout << scalar_product(v1, v2) << "\n";
    return 0;
}