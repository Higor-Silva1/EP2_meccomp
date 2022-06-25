import Bar
import numpy as np

def get_Ke_t(Bar): #Matriz de rigidez da treliça
    Ke_t = (Bar.E*Bar.A/Bar.L)*np.array([[ 1, 0, -1,0], 
                                         [ 0, 0, 0, 0],
                                         [-1, 0, 1, 0],
                                         [ 0, 0, 0, 0]]) 
    return Ke_t

def get_Ke_v(Bar): #Matriz de rigidez da viga
    Ke_v = (Bar.E*Bar.I/(Bar.L**3))*np.array([[     12,    6*Bar.L,      -12,    6*Bar.L],
                                              [6*Bar.L, 4*Bar.L**2, -6*Bar.L, 2*Bar.L**2],
                                              [    -12,   -6*Bar.L,       12,   -6*Bar.L],
                                              [6*Bar.L, 2*Bar.L**2, -6*Bar.L, 4*Bar.L**2]])
    return Ke_v

def get_Ke_p(Bar): #Matriz de rigidez do pórtico
    Ke_p = (Bar.E*Bar.A/Bar.L)*np.array([[ 1, 0, 0, -1, 0, 0], 
                                         [ 0, 0, 0,  0, 0, 0],
                                         [ 0, 0, 0,  0, 0, 0],
                                         [-1, 0, 0,  1, 0, 0],
                                         [ 0, 0, 0,  0, 0, 0],
                                         [ 0, 0, 0,  0, 0, 0]]) + (Bar.E*Bar.I/(Bar.L**3))*np.array([
                                              [0,       0,          0, 0,        0,          0],  
                                              [0,      12,    6*Bar.L, 0,      -12,    6*Bar.L],
                                              [0, 6*Bar.L, 4*Bar.L**2, 0, -6*Bar.L, 2*Bar.L**2],
                                              [0,       0,          0, 0,        0,          0],
                                              [0,     -12,   -6*Bar.L, 0,       12,   -6*Bar.L],
                                              [0, 6*Bar.L, 2*Bar.L**2, 0, -6*Bar.L, 4*Bar.L**2]])
    return Ke_p 

# A partir desse ponto eu não faço ideia se estou certo ou não. 
# Contudo, o que é a vida sem um pouco de aventura.

def get_Me_t(Bar): #Matriz de massa da treliça
    Me_t = (Bar.pho*Bar.A*Bar.L/6)*np.array([[2, 0, 1, 0], 
                                             [0, 0, 0, 0],
                                             [1, 0, 2, 0],
                                             [0, 0, 0, 0]])
    return Me_t

def get_Me_v(Bar): #Matriz de massa da viga
    Me_v = (Bar.pho*Bar.A*Bar.L/420)*np.array([[      156,    22*Bar.L,        54,   -13*Bar.L],
                                               [ 22*Bar.L,  4*Bar.L**2,  13*Bar.L, -3*Bar.L**2],
                                               [       54,    13*Bar.L,       156,   -22*Bar.L],
                                               [-13*Bar.L, -3*Bar.L**2, -22*Bar.L,  4*Bar.L**2]])
    return Me_v

def get_Me_p(Bar): #Matriz de massa do pórtico
    Me_p = (Bar.pho*Bar.A*Bar.L/6)*np.array([[2, 0, 0, 1, 0, 0], 
                                             [0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0],
                                             [1, 0, 0, 2, 0, 0],
                                             [0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0]]) + (Bar.pho*Bar.A*Bar.L/420)*np.array([
                                               [0,         0,           0, 0,         0,           0],  
                                               [0,       156,    22*Bar.L, 0,        54,   -13*Bar.L],
                                               [0,  22*Bar.L,  4*Bar.L**2, 0,  13*Bar.L, -3*Bar.L**2],
                                               [0,         0,           0, 0,         0,           0],
                                               [0,        54,    13*Bar.L, 0,       156,   -22*Bar.L],
                                               [0, -13*Bar.L, -3*Bar.L**2, 0, -22*Bar.L,  4*Bar.L**2]])
    return Me_p


def get_T3(Bar):
    T = np.array([[ np.cos(Bar.theta), np.sin(Bar.theta), 0, 0,                 0,                 0],
                  [-np.sin(Bar.theta), np.cos(Bar.theta), 0, 0,                 0,                 0],
                  [                 0,                 0, 1, 0,                 0,                 0],
                  [                 0,                 0, 0, np.cos(Bar.theta), np.sin(Bar.theta), 0],
                  [                 0,                 0, 0,-np.sin(Bar.theta), np.cos(Bar.theta), 0],
                  [                 0,                 0, 0, 0,                 0,                 1]])
         
    return T

def get_T2(Bar):
    T = np.array([[ np.cos(Bar.theta), np.sin(Bar.theta), 0,                 0        ],
          [-np.sin(Bar.theta), np.cos(Bar.theta), 0,                 0                ],
          [                 0,                 0, np.cos(Bar.theta), np.sin(Bar.theta)],
          [                 0,                 0,-np.sin(Bar.theta), np.cos(Bar.theta)]])
         
    return T


def set_C():
    print("Qual o vetor de condições de contorno do sistema? \n")
    print("Indique o vetor com os elementos separados por espaço, lembrando da ordem: u_1 v_1 phi_1 u_2 ...\n")
    temp = input()
    temp = temp.split()
    C = []
    for i in range(len(temp)):
        C.append(float(temp[i]))
        
    C = np.array(C)
    return C.transpose()

def set_F():
    print("Qual o vetor de esforços distribuidos aplicadas ao sistema? \n")
    print("Indique o vetor com os elementos separados por espaço, lembrando da ordem: u_1 v_1 phi_1 u_2 ...\n")
    temp = input()
    temp = temp.split()
    F = []
    for i in range(len(temp)):
        F.append(float(temp[i]))
        
    F = np.array(F)
    return F.transpose()

def set_Cm():
    pass
