from objects import Bar
import numpy as np

""""
def get_Ke_t(Bar): #Matriz de rigidez da treliça
    Ke_t = (Bar.E*Bar.A/Bar.L)*np.array[[ 1, 0, 0, -1, 0, 0], 
                                        [ 0, 0, 0,  0, 0, 0],
                                        [ 0, 0, 0,  0, 0, 0],
                                        [-1, 0, 0,  1, 0, 0],
                                        [ 0, 0, 0,  0, 0, 0],
                                        [ 0, 0, 0,  0, 0, 0]] 
    return Ke_t
"""

def get_Ke_t(Bar): #Matriz de rigidez da treliça
    Ke_t = (Bar.E*Bar.A/Bar.L)*np.array[[ 1, 0, -1,0], 
                                        [ 0, 0, 0, 0],
                                        [-1, 0, 1, 0],
                                        [ 0, 0, 0, 0]] 
    return Ke_t

def get_Ke_v(Bar): #Matriz de rigidez da viga
    Ke_v = (Bar.E*Bar.I/(Bar.L**3))*np.array[[0,       0,          0, 0,        0,          0]  
                                              [0,      12,    6*Bar.L, 0,      -12,    6*Bar.L]
                                              [0, 6*Bar.L, 4*Bar.L**2, 0, -6*Bar.L, 2*Bar.L**2]
                                              [0,       0,          0, 0,        0,          0]
                                              [0,     -12,   -6*Bar.L, 0,       12,   -6*Bar.L]
                                              [0, 6*Bar.L, 2*Bar.L**2, 0, -6*Bar.L, 4*Bar.L**2]]
    return Ke_v

def get_Ke_p(Bar): #Matriz de rigidez do pórtico
    return get_Ke_t(Bar) + get_Ke_v(Bar) 

# A partir desse ponto eu não faço ideia se estou certo ou não. 
# Contudo, o que é a vida sem um pouco de aventura.

def get_Me_t(Bar): #Matriz de massa da treliça
    Me_t = (Bar.pho*Bar.A*Bar.L/6)*np.array[[2, 0, 0, 1, 0, 0], 
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [1, 0, 0, 2, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0]]
    return Me_t

def get_Me_v(Bar): #Matriz de massa da viga
    Me_v = (Bar.pho*Bar.A*Bar.L/420)*np.array[[0,         0,           0, 0,         0,           0]  
                                              [0,       156,    22*Bar.L, 0,        54,   -13*Bar.L]
                                              [0,  22*Bar.L,  4*Bar.L**2, 0,  13*Bar.L, -3*Bar.L**2]
                                              [0,         0,           0, 0,         0,           0]
                                              [0,        54,    13*Bar.L, 0,       156,   -22*Bar.L]
                                              [0, -13*Bar.L, -3*Bar.L**2, 0, -22*Bar.L,  4*Bar.L**2]]
    return Me_v

def get_Me_p(Bar): #Matriz de massa do pórtico
    return get_Me_t(Bar) + get_Me_v(Bar)

""""
def get_T(Bar):
    T = [[ np.cos(Bar.theta), np.sin(Bar.theta), 0, 0,                 0,                 0]
         [-np.sin(Bar.theta), np.cos(Bar.theta), 0, 0,                 0,                 0]
         [                 0,                 0, 1, 0,                 0,                 0]
         [                 0,                 0, 0, np.cos(Bar.theta), np.sin(Bar.theta), 0]
         [                 0,                 0, 0,-np.sin(Bar.theta), np.cos(Bar.theta), 0]
         [                 0,                 0, 0, 0,                 0,                 1]]
         
    return T
"""

def get_T(Bar):
    T = [[ np.cos(Bar.theta), np.sin(Bar.theta), 0,                 0                ]
         [-np.sin(Bar.theta), np.cos(Bar.theta), 0,                 0                ]
         [                 0,                 0, np.cos(Bar.theta), np.sin(Bar.theta)]
         [                 0,                 0,-np.sin(Bar.theta), np.cos(Bar.theta)]]
         
    return T