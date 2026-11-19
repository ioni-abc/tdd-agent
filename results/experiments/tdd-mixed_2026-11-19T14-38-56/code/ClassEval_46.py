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
        result = []
        segments = list(range(len(x) - 1))
        for xi in x_interp:
            value = None
            # Use the first consecutive segment (in list order) that contains xi.
            for i in segments:
                x0, x1 = x[i], x[i + 1]
                if x0 == x1:
                    continue
                if min(x0, x1) <= xi <= max(x0, x1):
                    value = y[i] + (xi - x0) * (y[i + 1] - y[i]) / (x1 - x0)
                    break
            if value is None:
                # Extrapolate using the first valid segment.
                for i in segments:
                    x0, x1 = x[i], x[i + 1]
                    if x0 != x1:
                        value = y[i] + (xi - x0) * (y[i + 1] - y[i]) / (x1 - x0)
                        break
            result.append(value)
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
        def locate(coords, v):
            # Return (index, t) such that v = coords[index] + t * (coords[index + 1] - coords[index]),
            # or None if v lies outside the coordinate range.
            for i in range(len(coords) - 1):
                c0, c1 = coords[i], coords[i + 1]
                if c0 == c1:
                    continue
                if min(c0, c1) <= v <= max(c0, c1):
                    return i, (v - c0) / (c1 - c0)
            return None

        result = []
        for xi, yi in zip(x_interp, y_interp):
            loc_x = locate(x, xi)
            loc_y = locate(y, yi)
            if loc_x is None or loc_y is None:
                continue
            i, tx = loc_x
            j, ty = loc_y
            value = (z[i][j] * (1 - tx) * (1 - ty)
                     + z[i + 1][j] * tx * (1 - ty)
                     + z[i][j + 1] * (1 - tx) * ty
                     + z[i + 1][j + 1] * tx * ty)
            result.append(value)
        return result