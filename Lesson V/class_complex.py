"""
This module implements a class for working with complex numbers.
"""

import math


class ComplexNumber:
    """
    Creates a complex number object
    with real and imaginary parts.
    Provides methods that implement
    arithmetic operations with complex numbers.
    """

    def __init__(self, real, imag=0) -> None:

        self.real = real
        self.imag = imag

    def conjugate(self):
        """
        Returns a complex conjugate
        """

        return ComplexNumber(self.real, -self.imag)

    def __add__(self, right_operand):

        result_real = self.real + right_operand.real
        result_imag = self.imag + right_operand.imag

        return ComplexNumber(result_real, result_imag)

    def __sub__(self, right_operand):

        result_real = self.real - right_operand.real
        result_imag = self.imag - right_operand.imag

        return ComplexNumber(result_real, result_imag)

    def __mul__(self, right_operand):

        result_real = self.real * right_operand.real \
            - self.imag * right_operand.imag
        result_imag = self.real * right_operand.imag \
            + self.imag * right_operand.real

        return ComplexNumber(result_real, result_imag)

    def __truediv__(self, right_operand):

        numerator = self * ComplexNumber.conjugate(right_operand)
        denominator = abs(right_operand) ** 2

        result_real = numerator.real / denominator
        result_imag = numerator.imag / denominator

        return ComplexNumber(result_real, result_imag)

    def __abs__(self):

        real_sqr = self.real ** 2
        imag_sqr = self.imag ** 2

        result = math.sqrt(real_sqr + imag_sqr)

        return float(f'{result:.2f}')

    def __str__(self):

        return f'{self.real:.2f}{self.imag:+.2f}i'


if __name__ == '__main__':

    C_RE, C_IM = [int(token) for token in input().split()]
    D_RE, D_IM = [int(token) for token in input().split()]

    C = ComplexNumber(C_RE, C_IM)
    D = ComplexNumber(D_RE, D_IM)

    print(C + D)
    print(C - D)
    print(C * D)
    print(C / D)
    print(abs(C))
    print(abs(D))
