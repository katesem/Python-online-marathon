def double_string(l):
    return (len([j for i in l for j in l if j == i*2]))
