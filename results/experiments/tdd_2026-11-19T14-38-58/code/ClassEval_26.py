import csv
import os


class CSVProcessor:
    """
    This is a class for processing CSV files, including readring and writing CSV data, as well as processing specific operations and saving as a new CSV file.
    """


    def __init__(self):
        pass

    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :param file_name: str, name of the csv file
        :return title, data: (list, list), first row is title, the rest is data
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        """
        with open(file_name, 'r', newline='') as f:
            rows = list(csv.reader(f))
        if not rows:
            return [], []
        title = rows[0]
        data = rows[1:]
        return title, data

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
        1
        """
        try:
            with open(file_name, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
            return 1
        except (OSError, csv.Error, TypeError, ValueError):
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the N th column(from 0)
        :param save_file_name, the name of file that needs to be processed.
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        >>> csvProcessor.process_csv_data(0, 'read_test.csv')
        1
        >>> csvProcessor.read_csv('read_test_process.csv')
        (['a', 'b', 'c', 'd'], [['HELLO']])
        """
        try:
            title, data = self.read_csv(save_file_name)
            new_data = [title]
            for row in data:
                new_data.append([row[N].upper()])
            root, ext = os.path.splitext(save_file_name)
            new_file_name = root + '_process' + ext
            return self.write_csv(new_data, new_file_name)
        except (OSError, csv.Error, IndexError, TypeError, ValueError):
            return 0