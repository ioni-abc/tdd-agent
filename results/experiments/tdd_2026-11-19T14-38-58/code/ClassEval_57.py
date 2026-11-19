import numpy as np


class MetricsCalculator2:
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        """
        compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """
        def _reciprocal_rank(item):
            result, ground_truth_num = item
            if ground_truth_num <= 0:
                return 0.0
            for idx, value in enumerate(result):
                if value == 1:
                    return 1.0 / (idx + 1)
            return 0.0

        if isinstance(data, tuple):
            rr = _reciprocal_rank(data)
            return rr, [rr]

        if isinstance(data, list):
            if len(data) == 0:
                return 0.0, [0.0]
            rr_list = [_reciprocal_rank(item) for item in data]
            mean_rr = sum(rr_list) / len(rr_list)
            return mean_rr, rr_list

        raise TypeError("data must be a tuple or a list of tuples")

    @staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.41666666666666663, [0.41666666666666663]
        0.3333333333333333, [0.41666666666666663, 0.25]
        """
        def _average_precision(item):
            result, ground_truth_num = item
            if ground_truth_num <= 0:
                return 0.0
            hits = 0
            total = 0.0
            for idx, value in enumerate(result):
                if value == 1:
                    hits += 1
                    total += hits / (idx + 1)
            return total / ground_truth_num

        if isinstance(data, tuple):
            ap = _average_precision(data)
            return ap, [ap]

        if isinstance(data, list):
            if len(data) == 0:
                return 0.0, [0.0]
            ap_list = [_average_precision(item) for item in data]
            mean_ap = sum(ap_list) / len(ap_list)
            return mean_ap, ap_list

        raise TypeError("data must be a tuple or a list of tuples")