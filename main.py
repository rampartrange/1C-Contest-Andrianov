from helpers.parse_args import parse_args
from helpers.constants import low_level, high_level, start_level
from data_storage.data_processor import DataProcessor, make_up_courses

if __name__ == '__main__':

    arguments = parse_args()
    storage = arguments.func(arguments)

    print(f"Please write indices of {start_level} level courses")
    priority_second_level = list(map(int, input().split()))
    print(f"Please write indices of {low_level} level courses")
    chosen_courses_low_level = list(map(int, input().split()))
    print(f"Please write indices of {high_level} level courses")
    chosen_courses_high_level = list(map(int, input().split()))

    data_proc = DataProcessor(storage,
                              priority_second_level,
                              chosen_courses_low_level,
                              chosen_courses_high_level)

    make_up_courses(data_proc)


