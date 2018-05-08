import app

def call_test(a, b, expected, function):
    res = function(a, b)
    assert res == expected

def test_sum_int():
    a = 7
    b = 13
    expected = 20
    call_test(a, b, expected, app.sum_int)

def test_sum_str():
    a = 'a123'
    b = '321b'
    expected = 'a123321b'
    call_test(a, b, expected, app.sum_str)
