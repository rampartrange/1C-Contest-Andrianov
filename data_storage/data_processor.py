from data_storage.data_storage import DataStorage
import pandas as pd
import numpy as np
from helpers.constants import low_level, high_level, start_level


def parse_table(data_storage):
    parsed_table = data_storage.get_data()

    parsed_table.rename(columns={'Номер': 'index',
                                 'Название': 'name',
                                 'Формат': 'format',
                                 'Уровень': 'level',
                                 'Зависимости': 'dependencies'},
                        inplace=True)
    parsed_table = parsed_table.drop(columns=['format'])

    parsed_table['dependencies'] = parse_dependencies(parsed_table['dependencies'].astype('str').to_numpy())
    parsed_table.set_index('index', inplace=True)
    return parsed_table


def parse_dependencies(dependencies):
    parsed_result = list()
    for idx, element in enumerate(dependencies):
        parse_line = list()
        if element == 'nan':
            element = '0'
        without_comma = element.split(',')
        for new_element in without_comma:
            final_element = new_element.split('/')
            final_element = list(map(int, final_element))
            parse_line.append(final_element)

        parsed_result.append(parse_line)

    return parsed_result


def make_up_courses(data_proc):
    # low_level_dependencies = data_proc.collect_dependencies(low_level)
    # high_level_dependencies = data_proc.collect_dependencies(high_level)
    data_proc.collect_dependencies()


class DataProcessor:

    def __init__(self,
                 data_storage,
                 second_lvl_courses,
                 low_level_courses,
                 high_level_courses):
        self.data_storage = data_storage
        self.parsed_table = parse_table(data_storage)
        self.priorities = dict({start_level: second_lvl_courses,
                                low_level: low_level_courses,
                                high_level: high_level_courses})
        print(self.parsed_table)

    def collect_dependencies(self):
        self.parsed_table['paths'] = 0
        print(self.parsed_table)
        for course_idx in self.parsed_table.index.values.tolist():
            courses = list()
            for dependencies in self.parsed_table.loc[course_idx]['dependencies']:
                print(dependencies)
        print(self.parsed_table)

    def dfs(self, idx):
        courses_list = list()
        table = self.parsed_table
        for dependencies in table.loc[idx]['dependencies']:
            if len(dependencies) > 1:
                optional_choice = list()
            for course_id in dependencies:
                if course_id != 0:
                    if len(dependencies) > 1:
                        optional_choice.append(course_id)
                    else:
                        courses_list.append(course_id)
            if (len(dependencies) > 1) and (len(optional_choice) > 0):
                courses_list.append(optional_choice)
        return courses_list
