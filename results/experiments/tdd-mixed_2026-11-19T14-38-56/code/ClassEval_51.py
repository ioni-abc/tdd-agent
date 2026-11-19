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
        matrix = np.array(testData, dtype=np.int64)[:k, :k]
        total = int(matrix.sum())
        if total == 0:
            return 0.0
        observed = int(np.trace(matrix))
        row_sums = matrix.sum(axis=1)
        col_sums = matrix.sum(axis=0)
        chance = int(np.sum(row_sums * col_sums))
        numerator = total * observed - chance
        denominator = total * total - chance
        if denominator == 0:
            return 1.0
        return numerator / denominator

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
        matrix = np.array(testData, dtype=np.float64)[:N, :k]
        if N == 0 or n <= 1:
            return 0.0
        # Per-sample agreement P_i
        p_i = (np.sum(matrix ** 2, axis=1) - n) / (n * (n - 1))
        p_bar = float(np.mean(p_i))
        # Category proportions p_j, normalised by the total number of ratings in the matrix
        total = float(np.sum(matrix))
        if total == 0:
            return 0.0
        p_j = np.sum(matrix, axis=0) / total
        p_e = float(np.sum(p_j ** 2))
        if 1.0 - p_e == 0:
            return 1.0
        return float((p_bar - p_e) / (1.0 - p_e))