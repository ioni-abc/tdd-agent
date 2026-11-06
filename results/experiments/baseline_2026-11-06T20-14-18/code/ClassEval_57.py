import numpy as np


class MetricsCalculator2:
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def _normalize(data):
        if isinstance(data, tuple):
            return [data]
        return list(data)

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
        items = MetricsCalculator2._normalize(data)
        rr_list = []
        for result, _gt in items:
            rr = 0.0
            for rank, hit in enumerate(result, start=1):
                if hit == 1:
                    rr = 1.0 / rank
                    break
            rr_list.append(rr)
        if len(rr_list) == 0:
            return 0.0, []
        return sum(rr_list) / len(rr_list), rr_list

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
        items = MetricsCalculator2._normalize(data)
        ap_list = []
        for result, gt_num in items:
            hits = 0
            precision_sum = 0.0
            for rank, hit in enumerate(result, start=1):
                if hit == 1:
                    hits += 1
                    precision_sum += hits / rank
            ap = precision_sum / gt_num if gt_num else 0.0
            ap_list.append(ap)
        if len(ap_list) == 0:
            return 0.0, []
        return sum(ap_list) / len(ap_list), ap_list