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

# E = 100
# A = 1
# I = 1/12
# L = 2
# pho = 2

# Bar1 = Bar(E,A,L,pho,I,1,2,0)

# G = Global([Bar1],2,2)

# resutltado = analise(G)

# print(np.matrix.view(resutltado.modal_amr()[0]))

##### Questão 15 #######

# E = 10; A1 = 1; A2 = 2; L=1

# Bar1 = Bar(E,A1,L,0,0,1,2,0)
# Bar2 = Bar(E,A2,L,0,0,2,3,90)

# Bars = [Bar1,Bar2]

# C = [0,0,1*np.cos(np.pi/4),-1*np.sin(np.pi/4),0,0]
# F = [0,0,0,0,0,0]

# G = Global(Bars,2,3,C,F)

##################################

######## Questão 16 ################

# E = 100; A = 1; I = 1/12; L = 1; q = 2; P = 10

# Bar1 = Bar(E,A,L,0,I,1,2,0)
# Bar2 = Bar(E,A,L,0,I,2,3,0)
# Bars = [Bar1,Bar2]

####O que colocar quando eu não tiver a condição de contorno no ponto??? Preciso rever isso no código
####C != de condição de contorno, ele é o vetor final já aplicado as condiçoes de contorno, a matriz reduzida deve usar algo booleano
####Será que é preciso (e até possível?) fazer uma C reduzida ou melhor já adicionar no código?


# C = [0,0,0,0,P,0] #Matriz C já reduzida
# Contorno = [0,0,1,1,1,0]
# F = 2/12*np.array([6,1,12,0,6,-1])

# G = Global(Bars,2,3,Contorno,C,F)


###################################

########### Questão 17 #############
#Esse ele não resolve pq o theta2 não é parte do C e sim do Y, isso eu não coloquei no código

# E1 = 16; A1 = 2; I1 = 1/2;  pho1 = 2; L1 = 4
# E2 = 10; A2 = 4; I2 = 1/10; pho2 = 1; L2 = 2

# Bar1 = Bar(E1,A1,L1,pho1,I1,1,2,0)
# Bar2 = Bar(E2,A2,L2,pho2,I2,2,3,0)
# Bars = [Bar1,Bar2]

# C = [0,0,1,0.1,0,0]
# F = [0,0,0,  0,0,0]

# G = Global(Bars,2,3,[0,0,1,1,0,0],C,F)


####################################
# resultado = analise(G)

# print(np.matrix.view(resultado.harmonica()))



