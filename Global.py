import numpy as np
from porticos import matrices as m

#Para os métodos, ainda é preciso configurar manualmente se fara uso da get para v,t ou p
#e se irá usar a T2 ou T3

class Global:
    
    def __init__(self,Bars,number_degrees_of_motion = 0,number_of_nodes = 0):
        self.Me_g = Global.get_Me_global(self,Bars,number_degrees_of_motion,number_of_nodes)
        self.Ke_g = Global.get_Ke_global(self,Bars,number_degrees_of_motion,number_of_nodes)
    
    @classmethod

    #Este eu faço pouca ideia mas tenho uma pequena lógica
    def get_Ke_global(self,Bars,number_degrees_of_motion,number_of_nodes): #Bars is a list of Bar objects
        temp = np.zeros([number_degrees_of_motion*number_of_nodes,number_degrees_of_motion*number_of_nodes]) #Preallocating
        Ke_global = np.copy(temp)
        
        for n in range(len(Bars)):
            T = m.get_T2(Bars[n])
            T[T**2<10**(-8)] = 0 #Erro de aproximação
            
            Ke_p = np.matmul(np.matmul(np.matrix.transpose(T),m.get_Ke_v(Bars[n])),T)

            for i in range(2):
                for j in range(2):
                    
                    temp[2*(Bars[n].node1)-number_degrees_of_motion+i,2*(Bars[n].node1)-number_degrees_of_motion+j] = Ke_p[i,j]
                    temp[2*(Bars[n].node1)-number_degrees_of_motion+i,2*(Bars[n].node2)-number_degrees_of_motion+j] = Ke_p[i,j+number_degrees_of_motion]
                    temp[2*(Bars[n].node2)-number_degrees_of_motion+i,2*(Bars[n].node1)-number_degrees_of_motion+j] = Ke_p[i+number_degrees_of_motion,j]
                    temp[2*(Bars[n].node2)-number_degrees_of_motion+i,2*(Bars[n].node2)-number_degrees_of_motion+j] = Ke_p[i+number_degrees_of_motion,j+number_degrees_of_motion]
            
            Ke_global += temp
            Ke_global[Ke_global**2<10**(-8)] = 0 #Erro de aproximação

            temp = np.zeros([number_degrees_of_motion*number_of_nodes,number_degrees_of_motion*number_of_nodes]) #Resetting

           
        return Ke_global

    def get_Me_global(self,Bars,number_degrees_of_motion,number_of_nodes): #Bars is a list of Bar objects
        temp = np.zeros([number_degrees_of_motion*number_of_nodes,number_degrees_of_motion*number_of_nodes]) #Preallocating
        Me_global = np.copy(temp)
        
        for n in range(len(Bars)):
            T = m.get_T2(Bars[n])
            T[T**2<10**(-8)] = 0 #Erro de aproximação
            
            Me_p = np.matmul(np.matmul(np.matrix.transpose(T),m.get_Me_v(Bars[n])),T)

            for i in range(2):
                for j in range(2):
                    
                    temp[2*(Bars[n].node1)-number_degrees_of_motion+i,2*(Bars[n].node1)-number_degrees_of_motion+j] = Me_p[i,j]
                    temp[2*(Bars[n].node1)-number_degrees_of_motion+i,2*(Bars[n].node2)-number_degrees_of_motion+j] = Me_p[i,j+number_degrees_of_motion]
                    temp[2*(Bars[n].node2)-number_degrees_of_motion+i,2*(Bars[n].node1)-number_degrees_of_motion+j] = Me_p[i+number_degrees_of_motion,j]
                    temp[2*(Bars[n].node2)-number_degrees_of_motion+i,2*(Bars[n].node2)-number_degrees_of_motion+j] = Me_p[i+number_degrees_of_motion,j+number_degrees_of_motion]
            
            Me_global += temp
            Me_global[Me_global**2<10**(-8)] = 0 #Erro de aproximação

            temp = np.zeros([number_degrees_of_motion*number_of_nodes,number_degrees_of_motion*number_of_nodes]) #Resetting
        
        
        return Me_global