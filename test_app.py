import app
import pytest

def call_test(a, b, expected, function):
    res = function(a, b)
    assert res == expected

def test_sum_int():
    a = 7
    b = 13
    expected = 20
    call_test(a, b, expected, app.sum_int)

def test_sum_str_with_valid_a_and_b():
    a = 'a123'
    b = '321b'
    expected = 'a123321b'
    call_test(a, b, expected, app.sum_str)

def test_sum_str_with_invalid_a_valid_b():
    a = 51231
    b = '321b'
    try:
        app.sum_str(a, b)
        pytest.fail()
    except AssertionError:
        pass

def test_sum_str_with_invalid_b_valid_a():
    a = '321b'
    b = 51231
    try:
        app.sum_str(a, b)
        pytest.fail()
    except AssertionError:
        pass

def test_histogram():
    a = {'a': 3,
         'b': 2,
         'c': 1}

    b = {'b': 133,
         'c': -1,
         'd': 3}

    expected = {'a':3,
                'b':135,
                'c':0,
                'd':3,}

    call_test(a, b, expected, app.sum_histogram)
