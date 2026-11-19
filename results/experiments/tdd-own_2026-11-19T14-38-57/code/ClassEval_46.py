import bisect


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
        points = sorted(zip(x, y))
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        n = len(xs)
        result = []
        for xi in x_interp:
            if n == 1:
                result.append(float(ys[0]))
                continue
            i = bisect.bisect_right(xs, xi) - 1
            i = max(0, min(i, n - 2))
            x0, x1 = xs[i], xs[i + 1]
            y0, y1 = ys[i], ys[i + 1]
            t = (xi - x0) / (x1 - x0)
            result.append(y0 + t * (y1 - y0))
        return result

    @staticmethod
    def _locate(axis, v):
        """
        Find the bracketing indices and interpolation fraction of v on a sorted axis.
        """
        n = len(axis)
        if n == 1:
            return 0, 0, 0.0
        i = bisect.bisect_right(axis, v) - 1
        i = max(0, min(i, n - 2))
        t = (v - axis[i]) / (axis[i + 1] - axis[i])
        return i, i + 1, t

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
        x_order = sorted(range(len(x)), key=lambda k: x[k])
        y_order = sorted(range(len(y)), key=lambda k: y[k])
        xs = [x[k] for k in x_order]
        ys = [y[k] for k in y_order]
        grid = [[z[yi][xi] for xi in x_order] for yi in y_order]

        result = []
        for xv, yv in zip(x_interp, y_interp):
            ix0, ix1, tx = Interpolation._locate(xs, xv)
            iy0, iy1, ty = Interpolation._locate(ys, yv)
            z00 = grid[iy0][ix0]
            z01 = grid[iy0][ix1]
            z10 = grid[iy1][ix0]
            z11 = grid[iy1][ix1]
            bottom = (1 - tx) * z00 + tx * z01
            top = (1 - tx) * z10 + tx * z11
            result.append(float((1 - ty) * bottom + ty * top))
        return result