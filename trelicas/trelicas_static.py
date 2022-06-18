from cmath import cos
from math import sin
import numpy as np
import scipy as sp

def Ke_mod(bar): #bar is a object with all the bar's properties
    ke = np.array(bar.E*bar.A/bar.L)*np.array([ [cos(bar.theta)**2,cos(bar.theta)*sin(bar.theta),-cos(bar.theta)**2,-cos(bar.theta)*sin(bar.theta)],
                                                [cos(bar.theta)*sin(bar.theta),sin(bar.theta)**2,-cos(bar.theta)*sin(bar.theta),-sin(bar.theta)**2],
                                                [-cos(bar.theta)**2,-cos(bar.theta)*sin(bar.theta),cos(bar.theta)**2,cos(bar.theta)*sin(bar.theta)]
                                                [-cos(bar.theta)*sin(bar.theta),-sin(bar.theta)**2,cos(bar.theta)*sin(bar.theta),sin(bar.theta)**2]])

def Me_mod(bar):
    np.array(bar.pho*bar.A*bar.L/6)*np.array([ [2*cos(bar.theta)**2,2*cos(bar.theta)*sin(bar.theta),cos(bar.theta)**2,cos(bar.theta)*sin(bar.theta)],
                                                [2*cos(bar.theta)*sin(bar.theta),2*sin(bar.theta)**2,cos(bar.theta)*sin(bar.theta),sin(bar.theta)**2],
                                                [cos(bar.theta)**2,cos(bar.theta)*sin(bar.theta),2*cos(bar.theta)**2,2*cos(bar.theta)*sin(bar.theta)]
                                                [cos(bar.theta)*sin(bar.theta),sin(bar.theta)**2,2*cos(bar.theta)*sin(bar.theta),2*sin(bar.theta)**2]])

