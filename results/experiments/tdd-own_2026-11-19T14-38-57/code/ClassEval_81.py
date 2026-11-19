import math

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        """
        calculates the median of the given list.
        :param data: the given list, list.
        :return: the median of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5

        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 1:
            return float(sorted_data[mid])
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0

    @staticmethod
    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
        counts = {}
        for value in data:
            counts[value] = counts.get(value, 0) + 1
        if not counts:
            return []
        max_count = max(counts.values())
        return [value for value, count in counts.items() if count == max_count]

    @staticmethod
    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
        1.0

        """
        if len(x) != len(y):
            raise ValueError("x and y must have the same length")
        n = len(x)
        if n == 0:
            raise ValueError("inputs must not be empty")
        mean_x = sum(x) / float(n)
        mean_y = sum(y) / float(n)
        dx = [value - mean_x for value in x]
        dy = [value - mean_y for value in y]
        sxy = sum(a * b for a, b in zip(dx, dy))
        sxx = sum(a * a for a in dx)
        syy = sum(b * b for b in dy)
        if sxx == 0 or syy == 0:
            raise ValueError("correlation is undefined for constant input")
        return float(sxy / math.sqrt(sxx * syy))

    @staticmethod
    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.mean([1, 2, 3])
        2.0

        """
        return sum(data) / float(len(data))

    @staticmethod
    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """
        size = len(data)
        matrix = [[1.0] * size for _ in range(size)]
        for i in range(size):
            for j in range(i + 1, size):
                value = Statistics3.correlation(data[i], data[j])
                matrix[i][j] = value
                matrix[j][i] = value
        return matrix

    @staticmethod
    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0

        """
        n = len(data)
        if n < 2:
            raise ValueError("standard deviation requires at least two values")
        mean_value = sum(data) / float(n)
        squared_sum = sum((value - mean_value) ** 2 for value in data)
        return float(math.sqrt(squared_sum / (n - 1)))

    @staticmethod
    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]

        """
        std = Statistics3.standard_deviation(data)
        if std == 0:
            raise ValueError("z-score is undefined for constant input")
        mean_value = Statistics3.mean(data)
        return [float((value - mean_value) / std) for value in data]