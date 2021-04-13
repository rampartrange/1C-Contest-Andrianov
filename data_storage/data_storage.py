from helpers.constants import input_file, output_file


class DataStorage:
    """
    Class for storaging excel_data
    """

    def __init__(self,
                 data,
                 input_filename=input_file,
                 output_filename=output_file,
                 first_min=3,
                 second_min=1):
        self.data = data
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.first_min = first_min
        self.second_min = second_min

    def __str__(self):
        return str(self.data)

    def get_input_filename(self):
        return self.input_filename

    def get_output_filename(self):
        return self.output_filename

    def get_data(self):
        return self.data

    def get_first_min(self):
        return self.first_min

    def get_second_min(self):
        return self.second_min
