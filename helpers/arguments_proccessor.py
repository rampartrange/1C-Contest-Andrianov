import pandas as pd
from excel_parser.parser import read_input_cvt_to_table
from data_storage.data_storage import DataStorage


def process_args_ret_storage(args):
    input_data = read_input_cvt_to_table(args.input_file.name)
    storage = DataStorage(input_data,
                          args.input_file.name,
                          args.output_file.name,
                          args.first_min,
                          args.second_min)

    return storage

