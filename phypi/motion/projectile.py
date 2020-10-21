################ Projectile Motion ####################

import math
import phypi.constant


def xdisplace(u: int, t: int, angle: int):
    '''
        [+] Calculate x displacement with initial velocity, time and throwing angle. 
        >> from phypi.motion import projectile
        >> print(projectile.xdisplace(10, 5, 30))

    '''
    return u*t*math.cos(angle)


def ydisplace(u: int, t: int, angle: int, g: int = phypi.constant.g):
    '''
        [+] Calculate y displacement with initial veocity, time, gravity and angle.
        >> from phypi.motion import projectile
        >> print(projectile.ydisplace(10, 5, 30))
            or
        >> print(projectile.ydisplace(10, 5, 30, 10))
    '''
    return (u*t*(math.sin(angle))) - (0.5*g*(t**2))


def ydisplace_x(u: int, x: int, angle: int, g: int = phypi.constant.g):
    '''
        [+] Calculate y displacement with initial veocity, time, gravity, angle and x displacement.
        >> from phypi.motion import projectile
        >> print(projectile.ydisplace_x(10, 20, 30, 10))

    '''
    return (x*math.tan(angle)) - (g/(2*(u**2)*((math.cos)**2)))*(x**2)

def max_height(u: int, angle: int, g: int = phypi.constant.g):
    '''
        [+] maximum height attained by the object. 
        >> from phypi.motion import projectile
        >> print(projectile.ydisplace_x(10, 30, 10))
    '''
    return ((u**2)*(math.sin(angle))**2)/(2*g)

def total_time(u: int, angle: int, g: int = phypi.constant.g):
    '''
        [+] Total time taken by the object to travel total distace
        >> from phypi.motion import projectile
        >> print(projectile.ydisplace_x(10, 30, 10))
    '''
    return (2*u*math.sin(angle))/g

def range(u: int, angle: int, g: int = phypi.constant.g):
    '''
        [+] The range of an object, given the initial launch angle and initial velocity 
        >> from phypi.motion import projectile
        >> print(projectile.ydisplace_x(10, 30, 10))
    '''
    return ((u**2)*(math.cos(angle)))/(2*g)

