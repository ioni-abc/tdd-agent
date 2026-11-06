import bisect


class Interpolation:
    """
    This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data
    """

    def __init__(self):
        pass

    @staticmethod
    def _find_segment(coords, value):
        """
        Return index i such that coords[i] <= value <= coords[i + 1].
        Raises ValueError if value lies outside the coordinate range.
        """
        if value < coords[0] or value > coords[-1]:
            raise ValueError(f"Interpolation point {value} is outside the data range "
                             f"[{coords[0]}, {coords[-1]}]")
        if len(coords) == 1:
            return 0
        i = bisect.bisect_right(coords, value) - 1
        if i >= len(coords) - 1:
            i = len(coords) - 2
        return i

    @staticmethod
    def _lerp(x0, x1, y0, y1, xi):
        """Linear interpolation between (x0, y0) and (x1, y1) at xi."""
        if x1 == x0:
            return float(y0)
        return y0 + (xi - x0) * (y1 - y0) / (x1 - x0)

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
        if len(x) != len(y):
            raise ValueError("x and y must have the same length")
        if len(x) == 0:
            raise ValueError("x and y must not be empty")

        pairs = sorted(zip(x, y), key=lambda p: p[0])
        xs = [p[0] for p in pairs]
        ys = [p[1] for p in pairs]

        result = []
        for xi in x_interp:
            i = Interpolation._find_segment(xs, xi)
            if len(xs) == 1:
                result.append(float(ys[0]))
                continue
            result.append(Interpolation._lerp(xs[i], xs[i + 1], ys[i], ys[i + 1], xi))
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
        if len(z) != len(x) or any(len(row) != len(y) for row in z):
            raise ValueError("z must have shape len(x) x len(y)")
        if len(x) == 0 or len(y) == 0:
            raise ValueError("x and y must not be empty")
        if len(x_interp) != len(y_interp):
            raise ValueError("x_interp and y_interp must have the same length")

        result = []
        for xi, yi in zip(x_interp, y_interp):
            i = Interpolation._find_segment(x, xi)
            j = Interpolation._find_segment(y, yi)

            if len(x) == 1:
                # Degenerate case: only one x row, interpolate along y only
                row_val = Interpolation._lerp(y[j], y[j + 1], z[0][j], z[0][j + 1], yi) \
                    if len(y) > 1 else float(z[0][0])
                result.append(row_val)
                continue
            if len(y) == 1:
                col_val = Interpolation._lerp(x[i], x[i + 1], z[i][0], z[i + 1][0], xi)
                result.append(col_val)
                continue

            # Interpolate along y at the two bounding x rows
            z_low = Interpolation._lerp(y[j], y[j + 1], z[i][j], z[i][j + 1], yi)
            z_high = Interpolation._lerp(y[j], y[j + 1], z[i + 1][j], z[i + 1][j + 1], yi)
            # Then interpolate along x
            result.append(Interpolation._lerp(x[i], x[i + 1], z_low, z_high, xi))
        return result