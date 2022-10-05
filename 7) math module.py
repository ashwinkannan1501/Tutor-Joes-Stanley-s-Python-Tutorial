# math module

import math


def math_module():
    print("\n ------ Functions ----- \n")
    # Functions :-

    print('sqrt(x) function :- ', math.sqrt(81))  # This fucntion returns the square root of the x value.
    print('isqrt(n) function :- ', math.isqrt(15))  # This function returns the nearest integer square root of n value.
    print('dist(p, q) function :- ',
          math.dist((10, 20), (30, 50)))  # This function returns the distance between 2 points(p and q).
    print('factorial(x) function :- ',
          math.factorial(5))  # This function returns the factorial of a number. 5!=5x4x3x2x1
    print('gcd(x, y) function :- ', math.gcd(10,
                                             50))  # This function retrns the greatest common divisor (i.e the highest value that can divide 2 integers).
    print('pow(x, y) function :- ',
          math.pow(5, 3))  # This function returns the value of x to the power of y. (i.e x ** y)
    print('remainder(x, y) function :- ', math.remainder(10,
                                                         20))  # This function returns the closest value that can make numerator completely divisible by the denominator.
    print('prod(*iterables) function :- ',
          math.prod([2, 2, 2]))  # This function returns the product of an iterable (list, string, tuple, array, etc.)
    print('perm(n, k=None) function :- ', math.perm(5,
                                                    2))  # This function returns the number of ways to choose k itemswith order and without repetition. It Evaluates to n! / (n – k)! when k <= n and evaluates to 0 when k > n.
    print('hypot(*coordinates) function :- ',
          math.hypot(10, 50, 30))  # This function retruns the hypotenous of the values passed in the argument.
    print('floor(x) function :- ',
          math.floor(3.666))  # It rounds a number downwards to the nearest integer and returns the result.
    print('ceil(x) function :- ',
          math.ceil(3.666))  # It rounds a number upwards to the nearest integer and returns the result
    print('fabs(x) function :- ', math.fabs(-3.256))  # It returns the absolute value of a number
    print('comb(n, k) function :- ', math.comb(12,
                                               23))  # It returns the number of ways to choose k items from n items without repetition and order.

    print('sin(x) function :- ', math.sin(45.23))  # It returns teh sine of x value.
    print('cos(x) function :- ', math.cos(85.56))  # It returns the cosine of x value
    print('tan(x) function :- ', math.tan(12.92))  # It returns the tangent of x value.

    print('sinh(x) function :- ', math.sinh(45.23))  # It returns the hyperbolic sine of x value
    print('cosh(x) function :- ', math.cos(85.56))  # It returns the hyperbolic cosine of x value
    print('tanh(x) function :- ', math.tanh(12.92))  # It returns the hyperbolic tangent of x value

    print('asin(x) function :- ', math.asin(-0.369))  # it returns the arc sine of x value
    print('acos(x) function :- ', math.acos(1))  # It returns the arc cosine of x value
    print('atan(x) function :- ', math.atan(-1))  # It returns the arc tangent of x value

    print('asinh(x) function :- ', math.asinh(0.369))  # It returns the hyperbolic arc sine of x value
    print('acosh(x) function :- ', math.acosh(2))  # It returns the hyperbolic arc cosine of x value
    print('atanh(x) function :- ', math.atanh(0.95))  # It returns the hyperbolic arc tangent of x value

    print('atan2(y, x) function :- ', math.atan2(24, 12))  # It returns the arc tangent of y/x in radians

    print('degrees(x) function :- ', math.degrees(12.36))  # It converts the angle from radians to degree.
    print('radians(x) function :- ', math.radians(42.92))  # It converts the angle from degree to radians.

    print('copysign(x, y) function :- ', math.copysign(123,
                                                       -563))  # It returns the float consistng of the value of teh first parameter and the sign of the secodn parameter.
    print('fmod(x, y) function :- ', math.fmod(4, 2))  # It returns the remainder of the two parameters
    print('frexp(x) function :- ', math.frexp(
        12))  # It returns the mantissa and the exponent (m, e) of a specified value where mantissa (m) is a floating point value and exponent (e) is a exponent value such that (x = m * (2 ** e)) exactly.
    print('fsum(iterable) function :- ',
          math.fsum([5, 3, 9, 10, 53]))  # It returns the sum of all items in a iterable. (tuples, arrays, list, etc.)
    print('ldexp(x, i) function :- ',
          math.ldexp(20, 85))  # It returns the expression (x * (2 ** i)) where 'x' is mantissa and 'i' is exponent.
    print('modf(x) function :- ', math.modf(12))  # It returns the fractional and integer parts of x
    print('trunc(x) function :- ', math.trunc(36.369))  # It returns the truncated integer parts of x value.

    print('exp(x) function :- ', math.exp(32))  # It returns the value of (E**x).
    print('expm1(x) function :- ', math.expm1(20))  # It returns the value of ((E ** X) - 1)

    print('log(x, base=math.e) function :- ',
          math.log(12, 3))  # It returns the natural logarithmic of a number, (or) the logarithm of the number to base.
    print('log2(x) function :-', math.log2(12))  # It returns the base 2 logarithm of x value
    print('log10(x) function :- ', math.log10(12))  # It returns the base 10 logarithm of x value
    print('log1p(x) function :- ', math.log1p(12))  # Ir returns the natural logarithm of (1 + X)

    print('erf(x) function :- ', math.erf(12))  # It returns the error function of x value.
    print('erfc(x) function :- ', math.erfc(13))  # It retruns the complementary error function of x value.

    print('gamma(x) function :- ', math.gamma(16))  # It returns the gamma value of x. It is equal to 'factorial(x-1)'
    print('lgamma() function :- ', math.lgamma(16))  # It returns the log gamma value of x.

    print('isclose() function :- ',
          math.isclose(2.36, 1.03))  # It checks whether the two values are close to each other or not
    print('isfinite(x) function :- ', math.isfinite(16))  # It check whether x is a finite number or not
    print('isinf(x) function :- ', math.isinf(float(math.inf)))  # It checks whether x is a infinte number or not.
    print('isnan(x) function :- ', math.isnan(float(math.nan)))  # It checks whetehr x is a NAN (Not a Number) or not.

    print('\n ------ Constants ------ \n')

    # Constants
    print('e : ', math.e)  # It returns the "Euler's" number (2.71828182846)
    print('inf : ', math.inf)  # It returns the floating point positive infinity
    print('nan : ',
          math.nan)  # It returns the floating point nan(Not a Number) value. This value is not a legal number. It is equivalent to 'float("nan")'
    print('pi : ', math.pi)  # It returns the 'PI' value (22/7 (or) 3.141592653589793).
    print('tau : ',
          math.tau)  # It returns the 'tau' value (6.283185307179586). It is defined as the ratio of the circumference to the radius of a circle.


if __name__ == "__main__":
    math_module()
