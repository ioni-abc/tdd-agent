from math import pi, fabs

class TriCalculator:
    """
    The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """


    def __init__(self):
        pass

    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle
        :param x:float
        :return:float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
        angle = x % 360
        return float(round(self.taylor(angle, 50), 12))

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        t = x / 180 * pi
        total = 0.0
        for k in range(n + 1):
            total += ((-1) ** k) * (t ** (2 * k)) / self.factorial(2 * k)
        return total

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        angle = x % 360
        t = angle / 180 * pi
        total = 0.0
        for k in range(50):
            total += ((-1) ** k) * (t ** (2 * k + 1)) / self.factorial(2 * k + 1)
        return float(round(total, 12))


    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        s = self.sin(x)
        c = self.cos(x)
        if fabs(c) < 1e-12:
            raise ZeroDivisionError("tan is undefined for this angle")
        return float(s / c)