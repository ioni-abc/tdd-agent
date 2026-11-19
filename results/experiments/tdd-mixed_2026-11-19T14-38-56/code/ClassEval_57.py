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
        if isinstance(data, tuple):
            items = [data]
        else:
            items = list(data)

        reciprocal_ranks = []
        for actual, _ground_truth in items:
            rr = 0.0
            for rank, hit in enumerate(actual, start=1):
                if hit == 1:
                    rr = 1.0 / rank
                    break
            reciprocal_ranks.append(rr)

        if not reciprocal_ranks:
            return 0.0, []

        mean_rr = sum(reciprocal_ranks) / len(reciprocal_ranks)
        return mean_rr, reciprocal_ranks


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
        if isinstance(data, tuple):
            items = [data]
        else:
            items = list(data)

        average_precisions = []
        for actual, ground_truth in items:
            hits_so_far = 0
            precision_sum = 0.0
            for rank, hit in enumerate(actual, start=1):
                if hit == 1:
                    hits_so_far += 1
                    precision_sum += hits_so_far / rank
            if ground_truth:
                ap = precision_sum / ground_truth
            else:
                ap = 0.0
            average_precisions.append(ap)

        if not average_precisions:
            return 0.0, []

        mean_ap = sum(average_precisions) / len(average_precisions)
        return mean_ap, average_precisions