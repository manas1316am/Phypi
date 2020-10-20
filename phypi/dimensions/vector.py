'''
    1. Magnitude of the vector

'''

import math


def twodmagnitude(a: int, b: int):
    '''
        [+] twodmagnitude(a: int, b: int)
        >> from phypi.dimensions import vector
        >> print(vector.twodmagnitude(a,b))
    '''
    return math.sqrt(pow(a, 2) + pow(b, 2))


def threedmagnitude(a: int, b: int, c: int):
    '''
        [+] threedmagnitude(a: int, b: int ,c:int)
        >> from phypi.dimensions import vector
        >> print(vector.threedmagnitude(a,b,c))
    '''
    return math.sqrt(pow(a, 2) + pow(b, 2) + pow(c, 2))
