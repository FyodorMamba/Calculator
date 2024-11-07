#ifndef CALCULATIONS_H
#define CALCULATIONS_H

/**
 * @file calculations.h
 * @brief Provides basic arithmetic operations.
 */

/**
 * @brief Adds two numbers.
 * 
 * @param a The first number.
 * @param b The second number.
 * @return The sum of a and b.
 */
double add(double a, double b);

/**
 * @brief Subtracts two numbers.
 * 
 * @param a The first number.
 * @param b The second number.
 * @return The difference of a and b.
 */
double subtract(double a, double b);

/**
 * @brief Multiplies two numbers.
 * 
 * @param a The first number.
 * @param b The second number.
 * @return The product of a and b.
 */
double multiply(double a, double b);

/**
 * @brief Divides two numbers.
 * 
 * @param a The dividend.
 * @param b The divisor.
 * @return The quotient of a and b.
 * @note This function will throw a division by zero error if b is zero.
 */
double divide(double a, double b);

#endif