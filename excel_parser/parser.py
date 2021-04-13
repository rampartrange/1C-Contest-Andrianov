import pandas as pd


def read_input_cvt_to_table(filename):
    with open(filename, 'rb') as f:
        input_data = pd.read_csv(f)

    return input_data


def write_output(filename):
    with open(filename, 'wb') as f:
        output = 1