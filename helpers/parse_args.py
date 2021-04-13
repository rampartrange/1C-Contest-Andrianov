import argparse
from helpers.arguments_proccessor import process_args_ret_storage
from helpers.constants import input_file, output_file

def parse_args():
    parser = argparse.ArgumentParser(description='Allows you to provide input.csv and output.csv',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers()

    # input
    parser = subparsers.add_parser('argument_processor', help='processes arguments')
    parser.set_defaults(mode='process_arguments', func=process_args_ret_storage)
    parser.add_argument('-in', '--input-file', type=argparse.FileType('r'), help='Input file', default=input_file)
    parser.add_argument('-o', '--output-file', type=argparse.FileType('w'), help='Output file', default=output_file)
    parser.add_argument('--first-min', type=int, default=3, help='Minimal number of courses at 4th term')
    parser.add_argument('--second-min', type=int, default=1, help='Minimal number of courses at 6th term')

    arguments = parser.parse_args()

    return arguments
