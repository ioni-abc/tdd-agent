import os

import openpyxl


class ExcelProcessor:
    """
    This is a class for processing excel files, including readring and writing excel data, as well as processing specific operations and saving as a new excel file.
    """

    def __init__(self):
        pass

    def read_excel(self, file_name):
        """
        Reading data from Excel files
        :param file_name:str, Excel file name to read
        :return:list of data, Data in Excel
        """
        workbook = openpyxl.load_workbook(file_name)
        try:
            sheet = workbook.active
            return [tuple(row) for row in sheet.iter_rows(values_only=True)]
        finally:
            workbook.close()


    def write_excel(self, data, file_name):
        """
        Write data to the specified Excel file
        :param data: list, Data to be written
        :param file_name: str, Excel file name to write to
        :return: 0 or 1, 1 represents successful writing, 0 represents failed writing
        >>> processor = ExcelProcessor()
        >>> new_data = [
        >>>     ('Name', 'Age', 'Country'),
        >>>     ('John', 25, 'USA'),
        >>>     ('Alice', 30, 'Canada'),
        >>>     ('Bob', 35, 'Australia'),
        >>>     ('Julia', 28, 'Germany')
        >>> ]
        >>> data = processor.write_excel(new_data, 'test_data.xlsx')
        """
        workbook = None
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            for row in data:
                sheet.append(list(row))
            workbook.save(file_name)
            return 1
        except Exception:
            return 0
        finally:
            if workbook is not None:
                workbook.close()


    def process_excel_data(self, N, save_file_name):
        """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        >>> processor = ExcelProcessor()
        >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
        """
        base, ext = os.path.splitext(save_file_name)
        output_file = base + '_processed' + (ext if ext else '.xlsx')

        try:
            rows = self.read_excel(save_file_name)
        except Exception:
            return 0, output_file

        def upper_if_str(value):
            return value.upper() if isinstance(value, str) else value

        new_rows = []
        for index, row in enumerate(rows):
            row = list(row)
            if N < len(row):
                source_value = row[N]
            else:
                source_value = None
            if index == 0:
                new_value = upper_if_str(source_value)
            else:
                new_value = upper_if_str(source_value)
            new_rows.append(tuple(row + [new_value]))

        success = self.write_excel(new_rows, output_file)
        return success, output_file