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
        if not data:
            raise ValueError("median() arg is an empty sequence")
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
        if not data:
            return []
        counts = {}
        for item in data:
            counts[item] = counts.get(item, 0) + 1
        max_count = max(counts.values())
        return [item for item, count in counts.items() if count == max_count]

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
        n = len(x)
        if n == 0 or n != len(y):
            raise ValueError("lists must be non-empty and of equal length")
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        dx = [v - mean_x for v in x]
        dy = [v - mean_y for v in y]
        cov = sum(a * b for a, b in zip(dx, dy))
        sxx = sum(a * a for a in dx)
        syy = sum(b * b for b in dy)
        denom = math.sqrt(sxx * syy)
        if denom == 0:
            raise ValueError("correlation undefined for constant input")
        return cov / denom

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
        if not data:
            raise ValueError("mean() arg is an empty sequence")
        return sum(data) / len(data)

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
        return [
            [Statistics3.correlation(row_i, row_j) for row_j in data]
            for row_i in data
        ]

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
        m = sum(data) / n
        variance = sum((v - m) ** 2 for v in data) / (n - 1)
        return math.sqrt(variance)

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
        m = Statistics3.mean(data)
        s = Statistics3.standard_deviation(data)
        if s == 0:
            raise ValueError("z-score undefined when standard deviation is zero")
        return [(v - m) / s for v in data]