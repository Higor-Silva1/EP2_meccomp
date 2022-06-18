from objects import bar
import numpy as np

def get_Ke_t(bar): #Matriz de rigidez da treliça
    Ke_t = (bar.E*bar.A/bar.L)*np.array[[ 1, 0, 0, -1, 0, 0], 
                                        [ 0, 0, 0,  0, 0, 0],
                                        [ 0, 0, 0,  0, 0, 0],
                                        [-1, 0, 0,  1, 0, 0],
                                        [ 0, 0, 0,  0, 0, 0],
                                        [ 0, 0, 0,  0, 0, 0]] 
    return Ke_t

def get_Ke_v(bar): #Matriz de rigidez da viga
    Ke_v = (bar.E*bar.I/(bar.L**3))*np.array[[0,       0,          0, 0,        0,          0]  
                                              [0,      12,    6*bar.L, 0,      -12,    6*bar.L]
                                              [0, 6*bar.L, 4*bar.L**2, 0, -6*bar.L, 2*bar.L**2]
                                              [0,       0,          0, 0,        0,          0]
                                              [0,     -12,   -6*bar.L, 0,       12,   -6*bar.L]
                                              [0, 6*bar.L, 2*bar.L**2, 0, -6*bar.L, 4*bar.L**2]]
    return Ke_v

def get_Ke_p(bar): #Matriz de rigidez do pórtico
    return get_Ke_t(bar) + get_Ke_v(bar) 

# A partir desse ponto eu não faço ideia se estou certo ou não. 
# Contudo, o que é a vida sem um pouco de aventura.

def get_Me_t(bar): #Matriz de massa da treliça
    Me_t = (bar.pho*bar.A*bar.L/6)*np.array[[2, 0, 0, 1, 0, 0], 
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [1, 0, 0, 2, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0]]
    return Me_t

def get_Me_v(bar): #Matriz de massa da viga
    Me_v = (bar.pho*bar.A*bar.L/420)*np.array[[0,         0,           0, 0,         0,           0]  
                                              [0,       156,    22*bar.L, 0,        54,   -13*bar.L]
                                              [0,  22*bar.L,  4*bar.L**2, 0,  13*bar.L, -3*bar.L**2]
                                              [0,         0,           0, 0,         0,           0]
                                              [0,        54,    13*bar.L, 0,       156,   -22*bar.L]
                                              [0, -13*bar.L, -3*bar.L**2, 0, -22*bar.L,  4*bar.L**2]]
    return Me_v

def get_Me_p(bar): #Matriz de massa do pórtico
    return get_Me_t(bar) + get_Me_v(bar)

def get_T(bar):
    T = [[ np.cos(bar.theta), np.sin(bar.theta), 0, 0,                 0,                 0]
         [-np.sin(bar.theta), np.cos(bar.theta), 0, 0,                 0,                 0]
         [                 0,                 0, 1, 0,                 0,                 0]
         [                 0,                 0, 0, np.cos(bar.theta), np.sin(bar.theta), 0]
         [                 0,                 0, 0,-np.sin(bar.theta), np.cos(bar.theta), 0]
         [                 0,                 0, 0, 0,                 0,                 1]]
         
    return T