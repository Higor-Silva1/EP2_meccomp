import numpy as np
from porticos import matrices as m

class Global:
    
    def __init__(self,number_degrees_of_motion,number_of_nodes,size=0,Ke_global=[],Me_global=[]):
        self.number_degrees_of_motion = number_degrees_of_motion
        self.number_of_nodes = number_of_nodes
        self.size = number_degrees_of_motion*number_of_nodes
        self.Ke_global = np.zeros([10,10])
        self.Me_global = np.zeros([10,10])
    
    @classmethod

    #Este eu faço pouca ideia mas tenho uma pequena lógica
    def get_Ke_global(self,Bars,degrees,nodes): #Bars is a list of Bar objects
        temp = np.zeros([degrees*nodes,degrees*nodes]) #Preallocating
        Ke_global = np.copy(temp)
        print(np.matrix.view(Ke_global))
        print("antes \n")
        for n in range(len(Bars)):
            T = m.get_T(Bars[n])
            T[T**2<10**(-8)] = 0 #Erro de aproximação
            #print("n=",n,"/n")
            #print(np.matrix.view(T))
            #print("/n")
            #@ matriz multiply
            Ke_p = np.matmul(np.matmul(np.matrix.transpose(T),m.get_Ke_t(Bars[n])),T)
            #print(np.matrix.view(Ke_p))
            for i in range(2):
                for j in range(2):
                    #print(np.matrix.view(temp))
                    temp[2*(Bars[n].node1)-degrees+i,2*(Bars[n].node1)-degrees+j] = Ke_p[i,j]
                    temp[2*(Bars[n].node1)-degrees+i,2*(Bars[n].node2)-degrees+j] = Ke_p[i,j+degrees]
                    temp[2*(Bars[n].node2)-degrees+i,2*(Bars[n].node1)-degrees+j] = Ke_p[i+degrees,j]
                    temp[2*(Bars[n].node2)-degrees+i,2*(Bars[n].node2)-degrees+j] = Ke_p[i+degrees,j+degrees]
            
            
            #print(np.matrix.view(Ke_global))
            #print("depois \n")


            #print("n=",n,"temp: \n")
            #print(np.matrix.view(temp))
            #print("\n")

            
            Ke_global += temp
            Ke_global[Ke_global**2<10**(-8)] = 0 #Erro de aproximação
            #print("n=",n,"Ke_act: \n")
            #print(np.matrix.view(Ke_global))
            #print("\n")

            temp = np.zeros([degrees*nodes,degrees*nodes]) #Resetting
            
        return Ke_global