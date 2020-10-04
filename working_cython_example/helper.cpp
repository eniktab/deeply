#include <cmath>
#include "helper.h"

double PhredToPError(const int phred) {
    return std::pow(10.0, -static_cast<double>(phred) / 10.0);
}