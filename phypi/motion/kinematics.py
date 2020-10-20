'''
    1. velocity: v = u + at
    2. displacement:  s = u*t + 12*a*t^2
    3. velcity: v^2 = u^2 + 2*a*s
'''


def velocitywithtime(u: int, a: int, t: int):
    '''
        [+] Calculating velocity with the help of speed, acceleration and time
        >> from phypi.motion import kinematics
        >> print(kinematics.velocitywithtime(2,3,4))
    '''
    return u + a*t


def displacementwithtime(u: int, a: int, t: int):
    '''
        [+] calculating displacement with the help of initial speed, acceleration and time
        >> from phypi.motion import kinematics
        >> print(kinematics.displacementwithtime(2,3,4))
    '''
    return u*t + 12*a*t**2


def velocitywithouttime(u: int, a: int, s: int):
    '''
        [+] Calculating veocity with initial speed and acceleration and displacement, but without time
        >> from phypi.motion import kinematics
        >> print(kinematics.velocitywithouttime(2,3,4))
    '''
    return u**2 + 2*a*s
