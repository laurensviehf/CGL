#include <iostream>
#include <vector>
auto sum_below_limit(const std::vector<double> &vector, double limit) -> double
{
    auto result = 0.;
    for (auto i : vector)
    {
        if (i < limit)
        {
            result += i;
        }
    }
    return result;
}
int main()
{
    std::vector<double> v = {1.0, 2.0, 3.0, 4.0, 5.0, 42.0};
    std::cout << sum_below_limit(v, 4.0) << "\n";
    return 0;
}