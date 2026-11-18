import numpy as np
from fractions import Fraction


class KappaCalculator:
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """


    @staticmethod
    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        matrix = np.asarray(testData).tolist()
        # Use exact rational arithmetic to avoid floating point rounding issues
        values = [[Fraction(v) for v in row[:k]] for row in matrix[:k]]

        total = sum(sum(row) for row in values)
        if total == 0:
            return 0.0

        observed = sum(values[i][i] for i in range(k)) / total

        row_sums = [sum(values[i][j] for j in range(k)) for i in range(k)]
        col_sums = [sum(values[i][j] for i in range(k)) for j in range(k)]

        expected = sum(row_sums[i] * col_sums[i] for i in range(k)) / (total * total)

        if expected == 1:
            return 0.0

        return float((observed - expected) / (1 - expected))

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fliss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
        >>>                              [0, 2, 6, 4, 2],
        >>>                              [0, 0, 3, 5, 6],
        >>>                              [0, 3, 9, 2, 0],
        >>>                              [2, 2, 8, 1, 1],
        >>>                              [7, 7, 0, 0, 0],
        >>>                              [3, 2, 6, 3, 0],
        >>>                              [2, 5, 3, 2, 2],
        >>>                              [6, 5, 2, 1, 0],
        >>>                              [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """
        matrix = np.asarray(testData).tolist()
        rows = [[Fraction(v) for v in row[:k]] for row in matrix[:N]]

        if N == 0 or n <= 1:
            return 0.0

        # Per-subject agreement P_i
        P_i = []
        for row in rows:
            sum_sq = sum(v * v for v in row)
            P_i.append((sum_sq - n) / (n * (n - 1)))
        P_bar = sum(P_i) / N

        # Chance agreement P_e from category proportions p_j
        # The grand total is the sum of all entries in the matrix
        total = sum(sum(row) for row in rows)
        if total == 0:
            return 0.0
        P_e = Fraction(0)
        for j in range(k):
            p_j = sum(rows[i][j] for i in range(len(rows))) / total
            P_e += p_j * p_j

        if P_e == 1:
            return 0.0

        return float((P_bar - P_e) / (1 - P_e))