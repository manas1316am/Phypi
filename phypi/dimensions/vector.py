'''
    1. 2-D Magnitude of the vector => twodmagnitude(a,b)
    2. 3-D Magnitude OF the vector => threedmagnitude(a,b,c)

    3. 2-D dot product => twoddotproduct(a1, b1, a2, b2)
    4. 3-D dot product => threeddotproduct(a1, b1, a2, b2, a3, b3)

    5.

'''

import math

########## 1 ##################
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


########## 2 ##################

def twoddotproduct(a1: int, b1: int, a2: int, b2: int):
    '''
        [+] twoddotproduct(a1: int, b1: int, a2: int, b2: int)
        >> from phypi.dimensions import vector
        >> print(vector.twoddotproduct(a1, b1, a2, b2))
    '''
    return a1*b1 + a2*b2 

def threeddotproduct(a1: int, b1: int, a2: int, b2: int, a3: int, b3: int):
    '''
        [+] threeddotproduct(a1: int, b1: int, a2: int, b2: int)
        >> from phypi.dimensions import vector
        >> print(vector.threeddotproduct(a1, b1, a2, b2, a3, b3))
    '''
    return a1*b1 + a2*b2 + a3*b3

########## 3 ##################

def twodcrossproduct(a1: int, b1: int, a2: int, b2: int):
    '''
        [+] twodcrossproduct(a1: int, b1: int, a2: int, b2: int)
        >> from phypi.dimensions import vector
        >> print(vector.twodcrossproduct(a1, b1, a2, b2))
    '''
    return a1*b2 - a2*b1

def threedcrossproduct(a1: int, b1: int, a2: int, b2: int, a3: int, b3: int):
    '''
        [+] threedcrossproduct(a1: int, b1: int, a2: int, b2: int, a3: int, b3: int)
        >> from phypi.dimensions import vector
        >> print(vector.threedcrossproduct(a1, b1, a2, b2, a3, b3))
    '''
    return ((a2*b3) - (a3*b2)) + ((a1*b3) - (a3*b1)) + ((a1*b2) - (a2*b1))