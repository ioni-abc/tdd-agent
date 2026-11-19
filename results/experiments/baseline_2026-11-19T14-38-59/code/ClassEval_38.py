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
        try:
            wb = openpyxl.load_workbook(file_name, data_only=True)
            ws = wb.active
            data = [tuple(row) for row in ws.iter_rows(values_only=True)]
            wb.close()
            return data
        except Exception:
            return []

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
        try:
            wb = openpyxl.Workbook()
            ws = wb.active
            for row in data:
                ws.append(list(row))
            wb.save(file_name)
            wb.close()
            return 1
        except Exception:
            return 0

    def process_excel_data(self, N, save_file_name):
        """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        >>> processor = ExcelProcessor()
        >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
        """
        output_file = f"processed_{save_file_name}"
        data = self.read_excel(save_file_name)
        if not data or not isinstance(N, int) or N < 1:
            return 0, output_file

        idx = N - 1
        processed = []
        for row in data:
            row_list = list(row)
            if idx < len(row_list) and isinstance(row_list[idx], str):
                row_list[idx] = row_list[idx].upper()
            processed.append(tuple(row_list))

        success = self.write_excel(processed, output_file)
        return success, output_file