from Bar import Bar
from Global import Global
from porticos import matrices
import numpy as np

E = 4.22
A = 1
L = 1

Bar1 = Bar(E,A,L,0,0,1,2,0)
Bar2 = Bar(2.98,A,L,0,0,2,3,135)
Bar3 = Bar(E,A,L,0,0,3,4,0)
Bar4 = Bar(E,A,L,0,0,2,4,90)
Bar5 = Bar(2.98,A,L,0,0,2,5,45)
Bar6 = Bar(E,A,L,0,0,4,5,0)

Bars = [Bar1,Bar2,Bar3,Bar4,Bar5,Bar6]
G = Global(2,5)

#print(G.size)

#print(Bar1.node1)

#print(Bar2.theta)

print("Matriz Global: \n")
print(np.matrix.view(Global.get_Ke_global(Bars,2,5)))

#Pedir ao usuário condições de contorno zero e subtatrair ou multiplicar por zero
#nas posições equivalentes (tipo, se c_1 = 1, 0*[Me[1:end,1],Me[1,1:end]]??