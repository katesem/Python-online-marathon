def order(a):
    if a == sorted(a, reverse=False):
        return 'ascending'
    elif a == sorted(a, reverse=True):
        return 'descending'
    else:
        return 'not sorted'
