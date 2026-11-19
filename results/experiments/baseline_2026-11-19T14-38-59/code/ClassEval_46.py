from bisect import bisect_right


class Interpolation:
    """
    This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data
    """

    def __init__(self):
        pass

    @staticmethod
    def _find_interval(coords, value):
        """
        Return the index i such that coords[i] <= value <= coords[i+1]
        (clamped to the first/last segment for extrapolation).
        Assumes coords is sorted in ascending order and has at least 2 elements.
        """
        n = len(coords)
        i = bisect_right(coords, value) - 1
        if i < 0:
            i = 0
        if i > n - 2:
            i = n - 2
        return i

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :return: The y-coordinate of the interpolation point, list.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_1d([1, 2, 3], [1, 2, 3], [1.5, 2.5])
        [1.5, 2.5]

        """
        result = []
        for xi in x_interp:
            i = Interpolation._find_interval(x, xi)
            x0, x1 = x[i], x[i + 1]
            y0, y1 = y[i], y[i + 1]
            t = (xi - x0) / (x1 - x0)
            result.append(y0 + t * (y1 - y0))
        return result

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param z: The z-coordinate of the data point, list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :param y_interp: The y-coordinate of the interpolation point, list.
        :return: The z-coordinate of the interpolation point, list.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
        [3.0, 7.0]

        """
        result = []
        for xi, yi in zip(x_interp, y_interp):
            i = Interpolation._find_interval(x, xi)
            j = Interpolation._find_interval(y, yi)
            x0, x1 = x[i], x[i + 1]
            y0, y1 = y[j], y[j + 1]
            tx = (xi - x0) / (x1 - x0)
            ty = (yi - y0) / (y1 - y0)
            z00 = z[i][j]
            z10 = z[i + 1][j]
            z01 = z[i][j + 1]
            z11 = z[i + 1][j + 1]
            value = (z00 * (1 - tx) * (1 - ty)
                     + z10 * tx * (1 - ty)
                     + z01 * (1 - tx) * ty
                     + z11 * tx * ty)
            result.append(value)
        return result