from tkinter import Y
import numpy as np
from Bar import Bar
from Global import Global
import matplotlib.pyplot as plt

#numpy.linalg.eig() para obter os autovelores e autovetores em análise modal
#Lembrar que os autovalores serão w^2 e não w em si

#Criar uma classe chamada analise para guardar os resultados?
class analise():
    def __init__(self,Global_Matrix): #Se preciso, testar se Global_Matrix is type global e avisar se não for
        self.Global_Matrix = Global_Matrix

    def modal(self):
        print("Realizando Análise Modal sem Amortecimento... \n \n")
        K_estrela = np.linalg.inv(self.Global_Matrix.Me_g_reduzida)@self.Global_Matrix.Ke_g_reduzida
        #Pelo visto não é a matriz global que se utiliza, e sim a matriz reduzida aaaaa
        [auto_valores, auto_vetores] = np.linalg.eig(K_estrela)
        
        #Não tenho certeza se auto_vetores = modos_de_vibrar rever aula
        ########## Consertar modos_de_vibrar ########### 
        modos_de_vibrar = auto_vetores
        modos_de_vibrar[np.isclose(modos_de_vibrar,0)] = 0
        omega = np.sqrt(auto_valores)
        omega_hertz = omega/(2*np.pi)

        print("As frequências de ressonância são: \n")
        for i in range(len(omega)):
            print("w",i+1,"=",omega[i],"\n")
        
        print("Os modos de vibrar são: \n")
        for q in range(len(omega)):
            print("Modo",q+1,"=",np.matrix.view(modos_de_vibrar[q]),"\n")
        return omega, modos_de_vibrar #Não se devo colocar pos o usuário talvez queira mais de uma análise

    def harmonica(self):
        print("Realizando Análise Harmônica sem Amortecimento... \n \n")
        
        print("Qual a frequência dos esforços aplicados: \n")
        w = float(input())
        Y = np.linalg.inv(self.Global_Matrix.Ke_g_reduzida-(w)**2*self.Global_Matrix.Me_g_reduzida)@(self.Global_Matrix.F+self.Global_Matrix.C)
        Y = Y.transpose()
        print("Digite 1 para Y; 2 para as reações e 3 para análise na frequência")
        modo = int(input())
        
        if modo == 1: 
            return Y
        
        if modo == 2:
            reactions = (self.Global_Matrix.Ke_g - (w**2)*self.Global_Matrix.Me_g)@Y

            return reactions

        if modo == 3:
            print("Escolha em quantas partes iguais o w será dividido: \n")
            h = int(input("h precisa ser maior que 1: "))
            Y = np.zeros([len(self.Global_Matrix.Ke_g_reduzida), h])
            print("Qual a frequência final (assumindo incial == 0): \n")
            w_f = float(input())
            
            w_vec = np.arange(0,w_f,w_f/h)

            for i in range(h):
                
                # A matriz Ke_g é singular por definição
                #Y[:,i] = np.linalg.inv(self.Global_Matrix.Ke_g-(w_f*i/(h-1))**2*self.Global_Matrix.Me_g)@(self.Global_Matrix.F+self.Global_Matrix.C) #(w_f/h)*i passo atual

                Y[:,i] = np.linalg.inv(self.Global_Matrix.Ke_g_reduzida-(w_f*i/(h-1))**2*self.Global_Matrix.Me_g_reduzida)@(self.Global_Matrix.F+self.Global_Matrix.C) #(w_f/h)*i passo atual
            
            #print("\n Y = ",np.matrix.view(Y))

            print("Para qual condição de contorno deseja obter a resposta em frequência?: \n")
            print("Digite o número inteiro equivalente a posição no vetor Y ou 0 para sair")
            cc_desejado = int(input())
            while cc_desejado != 0:
                plt.plot(w_vec,np.abs(Y[cc_desejado-1,:]))
                plt.show()
                print("Digite o número inteiro equivalente a posição no vetor Y ou 0 para sair \n")
                cc_desejado = int(input())
            return Y


