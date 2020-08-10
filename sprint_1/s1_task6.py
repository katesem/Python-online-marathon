def order(a):

    if a == sorted(a, reverse=False):
        s = 'ascending'
        return s
    elif a == sorted(a, reverse=True):
        s = 'descending'
        return s
    else:
        s = 'not sorted'
        return s
