#include "calculations.h"

double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    if (b == 0) {
        // Handle division by zero error
        // For example, you can return a specific value or throw an exception
        return 0;
    }
    return a / b;
}