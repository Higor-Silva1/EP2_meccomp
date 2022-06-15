from cmath import cos
from math import sin
import numpy as np
import scipy as sp

def Ke_mod(bar,theta): #bar is a object with all the bar's properties
    ke = np.array(bar.E*bar.A/bar.L)*np.array([ [cos(theta)**2,cos(theta)*sin(theta),-cos(theta)**2,-cos(theta)*sin(theta)],
                                                [cos(theta)*sin(theta),sin(theta)**2,-cos(theta)*sin(theta),-sin(theta)**2],
                                                [-cos(theta)**2,-cos(theta)*sin(theta),cos(theta)**2,cos(theta)*sin(theta)]
                                                [-cos(theta)*sin(theta),-sin(theta)**2,cos(theta)*sin(theta),sin(theta)**2]])

def Me_mod(bar,theta):
    np.array(bar.pho*bar.A*bar.L/6)*np.array([ [2*cos(theta)**2,2*cos(theta)*sin(theta),cos(theta)**2,cos(theta)*sin(theta)],
                                                [2*cos(theta)*sin(theta),2*sin(theta)**2,cos(theta)*sin(theta),sin(theta)**2],
                                                [cos(theta)**2,cos(theta)*sin(theta),2*cos(theta)**2,2*cos(theta)*sin(theta)]
                                                [cos(theta)*sin(theta),sin(theta)**2,2*cos(theta)*sin(theta),2*sin(theta)**2]])

