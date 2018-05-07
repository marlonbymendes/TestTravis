def sum_int(a, b):
    return a + b

def sum_int_mod(a, b, m):
    return sum_int(a, b) % m

def sum_str(a, b):
    assert(type(a) == str)
    assert(type(b) == str)
    return (a + b)

def sum_histogram(a, b):
    print('start')
    keys = set(list(a.keys()) + list(b.keys()))
    res = dict()
    for key in keys:
        value = None
        print('key = {}'.format(key))
        if key in a.keys():
            value = a[key]
        if key in b.keys():
            if value == None:
                value = b[key]
            else:
                value += b[key]
        res[key] = value
    return res
