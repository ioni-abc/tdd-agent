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

        segments = len(x) - 1
        result = []
        for xi in x_interp:
            chosen = None
            for i in range(segments):
                lo = min(x[i], x[i + 1])
                hi = max(x[i], x[i + 1])
                if lo <= xi <= hi:
                    chosen = i
                    break
            if chosen is None:
                # Extrapolate using the nearest end segment
                chosen = 0 if xi < min(x[0], x[1]) else segments - 1
            x0, x1 = x[chosen], x[chosen + 1]
            y0, y1 = y[chosen], y[chosen + 1]
            value = y0 + (xi - x0) * (y1 - y0) / (x1 - x0)
            result.append(round(value, 10))
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
        if len(x) < 2 or len(y) < 2:
            return []

        x_segments = len(x) - 1
        y_segments = len(y) - 1
        x_lo, x_hi = min(x), max(x)
        y_lo, y_hi = min(y), max(y)

        result = []
        for xi, yi in zip(x_interp, y_interp):
            # Points outside the grid domain are not interpolated
            if not (x_lo <= xi <= x_hi and y_lo <= yi <= y_hi):
                continue

            # Locate the x segment containing xi
            i_seg = None
            for i in range(x_segments):
                lo = min(x[i], x[i + 1])
                hi = max(x[i], x[i + 1])
                if lo <= xi <= hi:
                    i_seg = i
                    break

            # Locate the y segment containing yi
            j_seg = None
            for j in range(y_segments):
                lo = min(y[j], y[j + 1])
                hi = max(y[j], y[j + 1])
                if lo <= yi <= hi:
                    j_seg = j
                    break

            if i_seg is None or j_seg is None:
                continue

            x0, x1 = x[i_seg], x[i_seg + 1]
            y0, y1 = y[j_seg], y[j_seg + 1]
            tx = (xi - x0) / (x1 - x0)
            ty = (yi - y0) / (y1 - y0)

            z00 = z[i_seg][j_seg]
            z10 = z[i_seg + 1][j_seg]
            z01 = z[i_seg][j_seg + 1]
            z11 = z[i_seg + 1][j_seg + 1]

            value = (z00 * (1 - tx) * (1 - ty)
                     + z10 * tx * (1 - ty)
                     + z01 * (1 - tx) * ty
                     + z11 * tx * ty)
            result.append(round(value, 10))
        return result