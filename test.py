import pytest
from trading import *


def test_return_max_result():
    dict_object_1 = {
        'EUR CNY EUR': 4.0, 'USD CNY USD': 2.0, 'USD THB USD': 30.0,
        'CNY EUR CNY': 4.0, 'CNY USD CNY': 2.0, 'THB USD THB': 30.0
    }
    dict_object_2 = {}

    res_func_1 = return_max_result(dict_object_1)
    res_func_2 = return_max_result(dict_object_2)
    
    res = max(dict_object_1)
    
    assert res_func_1 == f'{res} conversion rate {dict_object_1[res]}'
    assert type(res_func_1) == str
    assert type(res_func_1) is not None
    assert res_func_2 is None
    assert type(res_func_2) is not str
    