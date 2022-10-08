import sys
import os
import pandas as pd
from itertools import *


def get_matrix_with_file_csv(file_csv) -> tuple:
    """Select columns from the file, convert to a matrix, get a list of currencies"""
    colm = file_csv.columns
    currency_list = [c for c in colm[1:]]
    currency_matrix = list()
    for el in file_csv.values:
        el_matrix = list(map(lambda el_list: float(el_list), el[1:]))
        currency_matrix.append(el_matrix)
    return currency_list, currency_matrix


def search_combination(object_list: list) -> list:
    """Get from combinations from the list of currencies returns a list of all possible combinations"""
    combination_list = list()
    combo = 2
    if len(object_list) > 3:
        while combo < len(object_list):
            for elem in permutations(object_list, combo):
                first_el = (elem[0],)
                element = elem + first_el
                combination_list.append(list(element))
            combo += 1
    else:
        for elem in permutations(object_list, len(object_list) - 1):
            first_el = (elem[0],)
            element = elem + first_el
            combination_list.append(list(element))
    return combination_list


def get_dictionary_with_currency_pairs(file_csv) -> dict:
    """Getting and returning a dictionary with currency pairs and value"""
    columns = list(file_csv)[1:]
    dict_currency = dict()
    n = 0
    for element in file_csv.values:
        for currency in element[1:]:
            if element[0] != columns[n]:
                dict_currency[element[0]+'/'+columns[n]] = currency
            if n < (len(columns)-1):
                n += 1
        n = 0
    return dict_currency


def get_result_with_combo(object_list: list, object_dict: dict) -> dict:
    """
    Function from the list of all possible combinations, select those that have a profit of more than 1%,
    return a dictionary with combinations
    """
    index_first_el = 0
    index_second_el = 1
    dict_result = dict()
    temp_res = 1
    lst_currency = []
    for el in object_list:
        while True:
            lst_currency.append(object_dict[el[index_first_el] + "/" + el[index_second_el]])
            if index_first_el < (len(el) - 1) and index_second_el < (len(el) - 1):
                index_first_el += 1
                index_second_el += 1
            else:
                for elem in lst_currency:
                    temp_res *= elem
                if ((temp_res-1)*100) > 1:
                    dict_result[" ".join(el)] = round(((temp_res-1)*100), 2)
                break
                
        index_first_el = 0
        index_second_el = 1
        temp_res = 1
        lst_currency = []
    return dict_result


def return_max_result(object_dict: dict) -> str:
    """The function takes a dictionary as input, looks for the maximum value and returns the key as a string"""
    if len(object_dict) != 0:
        max_result = max(object_dict.values())
        for key, value in object_dict.items():
            if value == max_result:
                return f'{key} conversion rate {value}'
    else:
        return 'No risk-free opportunities exist yielding over 1.00% profit'


if __name__ == '__main__':
    try:
        path = sys.argv[1]
        if os.path.exists(path):
            read_file_csv = pd.read_csv(path, delimiter=",")
            list_currency, matrix_currency = get_matrix_with_file_csv(read_file_csv)
            combo_list = search_combination(list_currency)
            currency_dict = get_dictionary_with_currency_pairs(read_file_csv)
            result_dict = get_result_with_combo(combo_list, currency_dict)
            print(return_max_result(result_dict))
        else:
            print(f'Not found file in path {path}')
    except IndexError:
        print('Not found path. Specify the file path')
