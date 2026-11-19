class MetricsCalculator:
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the number of all four samples to 0
        """
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0


    def update(self, predicted_labels, true_labels):
        """
        Update the number of all four samples(true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, change the number of corresponding samples
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        (self.true_positives, self.false_positives, self.false_negatives, self.true_negatives) = (1, 1, 1, 1)
        """
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                self.true_positives += 1
            elif predicted == 1 and true == 0:
                self.false_positives += 1
            elif predicted == 0 and true == 1:
                self.false_negatives += 1
            else:
                self.true_negatives += 1


    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        tp = 0
        fp = 0
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                tp += 1
            elif predicted == 1 and true == 0:
                fp += 1
        denominator = tp + fp
        if denominator == 0:
            return 0.0
        return tp / denominator


    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        tp = 0
        fn = 0
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                tp += 1
            elif predicted == 0 and true == 1:
                fn += 1
        denominator = tp + fn
        if denominator == 0:
            return 0.0
        return tp / denominator


    def f1_score(self, predicted_labels, true_labels):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        tp = 0
        fp = 0
        fn = 0
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                tp += 1
            elif predicted == 1 and true == 0:
                fp += 1
            elif predicted == 0 and true == 1:
                fn += 1
        # 2PR/(P+R) simplifies to 2TP/(2TP+FP+FN), avoiding intermediate rounding
        denominator = 2 * tp + fp + fn
        if denominator == 0:
            return 0.0
        return (2 * tp) / denominator


    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>>mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        tp = 0
        tn = 0
        total = 0
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted not in (0, 1) or true not in (0, 1):
                continue
            total += 1
            if predicted == 1 and true == 1:
                tp += 1
            elif predicted == 0 and true == 0:
                tn += 1
        if total == 0:
            return 0.0
        return (tp + tn) / total