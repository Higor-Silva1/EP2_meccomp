from Bar import Bar
from Global import Global
from porticos import matrices
import numpy as np
from porticos.dinamica import analise

# E = 4.22
# A = 1
# L = 1

# Bar1 = Bar(E,A,L,1,1,1,2,0)
# Bar2 = Bar(2.98,A,L,1,1,2,3,135)
# Bar3 = Bar(E,A,L,1,1,3,4,0)
# Bar4 = Bar(E,A,L,1,1,2,4,90)
# Bar5 = Bar(2.98,A,L,1,1,2,5,45)
# Bar6 = Bar(E,A,L,1,1,4,5,0)

# Bars = [Bar1,Bar2,Bar3,Bar4,Bar5,Bar6]
# G = Global(Bars,2,5)

# print(np.matrix.view(G.get_Ke_global(Bars,2,5))) #mudar isso aqui, para parametrizar

# print("\n \n")

# print(np.matrix.view(G.Ke_g_reduzida))



#Me_gloal precisa do "self: Global", mas Ke_global não???????
#print(np.matrix.view(G.get_Me_global(Bars,2,5)))
#Pedir ao usuário condições de contorno zero e subtatrair ou multiplicar por zero
#nas posições equivalentes (tipo, se c_1 = 1, 0*[Me[1:end,1],Me[1,1:end]]??

E = 100
A = 1
I = 1/12
L = 2
pho = 2

Bar1 = Bar(E,A,L,pho,I,1,2,0)

G = Global([Bar1],2,2)

resutltado = analise(G)

print(np.matrix.view(resutltado.modal_amr()[0]))
