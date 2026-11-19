class Interpolation:
    """
    This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data
    """

    def __init__(self):
        pass

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
        if len(x) < 2 or len(y) < 2:
            return []

        n_segments = min(len(x), len(y)) - 1
        result = []
        for xi in x_interp:
            segment = None
            for i in range(n_segments):
                x0, x1 = x[i], x[i + 1]
                if min(x0, x1) <= xi <= max(x0, x1):
                    segment = i
                    break
            if segment is None:
                # Outside every segment: extrapolate using the first segment.
                segment = 0
            x0, x1 = x[segment], x[segment + 1]
            y0, y1 = y[segment], y[segment + 1]
            result.append(y0 + (y1 - y0) * (xi - x0) / (x1 - x0))
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
        def find_segment(coords, value):
            for i in range(len(coords) - 1):
                c0, c1 = coords[i], coords[i + 1]
                if c0 != c1 and min(c0, c1) <= value <= max(c0, c1):
                    return i
            return None

        if len(x) < 2 or len(y) < 2:
            return []

        result = []
        for xi, yi in zip(x_interp, y_interp):
            i = find_segment(x, xi)
            j = find_segment(y, yi)
            if i is None or j is None:
                continue
            tx = (xi - x[i]) / (x[i + 1] - x[i])
            ty = (yi - y[j]) / (y[j + 1] - y[j])
            value = (z[i][j] * (1 - tx) * (1 - ty)
                     + z[i + 1][j] * tx * (1 - ty)
                     + z[i][j + 1] * (1 - tx) * ty
                     + z[i + 1][j + 1] * tx * ty)
            result.append(value)
        return result