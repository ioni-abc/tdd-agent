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
        mat = np.asarray(testData, dtype=np.int64)
        total = int(mat.sum())
        diag = int(np.trace(mat))
        row_sums = mat.sum(axis=1)
        col_sums = mat.sum(axis=0)
        expected = int(np.sum(row_sums * col_sums))
        numerator = total * diag - expected
        denominator = total * total - expected
        return float(numerator) / float(denominator)

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
        mat = np.asarray(testData, dtype=np.float64).reshape(N, k)
        # Per-subject agreement P_i
        p_i = (np.sum(mat * mat, axis=1) - n) / (n * (n - 1))
        p_bar = float(np.mean(p_i))
        # Chance agreement P_e
        total = float(np.sum(mat))
        p_j = np.sum(mat, axis=0) / total
        p_e = float(np.sum(p_j * p_j))
        return (p_bar - p_e) / (1.0 - p_e)