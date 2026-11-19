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
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

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
        return sorted(value for value, count in counts.items() if count == max_count)

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
        if len(x) != len(y) or len(x) == 0:
            return None
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        dx = [a - mean_x for a in x]
        dy = [b - mean_y for b in y]
        num = sum(a * b for a, b in zip(dx, dy))
        sxx = sum(a * a for a in dx)
        syy = sum(b * b for b in dy)
        if sxx == 0 or syy == 0:
            return None
        return float(num / math.sqrt(sxx * syy))

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
            return None
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
        if not data or not data[0]:
            return []
        ncols = len(data[0])
        columns = [[row[j] for row in data] for j in range(ncols)]
        return [
            [Statistics3.correlation(columns[i], columns[j]) for j in range(ncols)]
            for i in range(ncols)
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
            return None
        m = sum(data) / n
        ss = sum((x - m) ** 2 for x in data)
        return float(math.sqrt(ss / (n - 1)))

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
        n = len(data)
        if n < 2:
            return None
        std = Statistics3.standard_deviation(data)
        if std is None or std == 0:
            return None
        m = Statistics3.mean(data)
        return [(x - m) / std for x in data]