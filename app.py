def sum_int(a, b):
    res = a + b
    return res

def sum_int_mod(a, b, m):
    res = sum_int(a, b) % m
    return res

def sum_str(a, b):
    assert(type(a) == str)
    assert(type(b) == str)
    res = (a + b)
    return res

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

def sum_above(t, i, j):
    res = 0
    above = t[i - 1]
    if (j - 1) >= 0:
        res += above[j - 1]
    if j < len(above):
        res += above[j]
    return res

def pascal(n):
    t = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i + 1):
            row.append(sum_above(t, i, j))
        t.append(row)
    return t

def get_number_of_spaces(row):
    res = len(row) - 1
    for val in row:
        res += len(str(val))
    return res

def print_pascal(n):
    p = pascal(n)
    spaces = get_number_of_spaces(p[len(p) - 1])
    out = '\n'.join(' '.join(map(str, row)).center(spaces) for row in p)
    print(out)
