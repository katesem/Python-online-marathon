import random
import copy

def randomWord(l):
    if not l:
        yield None
    while True:
        for i in range(len(l)):
            r = copy.deepcopy(random.sample(l,len(l)))
            for j in range(len(l)):
                yield r[j]
    
