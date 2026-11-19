import numpy as np

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
        matrix = np.array(testData, dtype=float).reshape(k, k)
        total = matrix.sum()
        if total == 0:
            return 0.0
        observed = np.trace(matrix) / total
        row_sums = matrix.sum(axis=1)
        col_sums = matrix.sum(axis=0)
        expected = float(np.sum(row_sums * col_sums)) / (total * total)
        if 1.0 - expected == 0:
            return 1.0
        return float((observed - expected) / (1.0 - expected))

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
        matrix = np.array(testData, dtype=float).reshape(N, k)
        # Per-item agreement P_i
        if n <= 1:
            return 0.0
        p_i = (np.sum(matrix * matrix, axis=1) - n) / (n * (n - 1))
        p_bar = float(np.mean(p_i))
        # Chance agreement P_e
        p_j = matrix.sum(axis=0) / (N * n)
        p_e = float(np.sum(p_j * p_j))
        if 1.0 - p_e == 0:
            return 1.0
        return float((p_bar - p_e) / (1.0 - p_e))