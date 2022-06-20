import numpy as np
from porticos import matrices as m

#Para os métodos, ainda é preciso configurar manualmente se fara uso da get para v,t ou p
#e se irá usar a T2 ou T3

class Global:
    
    def __init__(self,Bars,number_degrees_of_motion = 0,number_of_nodes = 0,Contorno = 0, C=0, F=0):
        #Mudei para colocar direto os C e o F para evitar o trablho de iniciar toda hora, o produto final
        #talvez mantenha o set_C e o set_F
        self.Ke_g = Global.get_Ke_global(self,Bars,number_degrees_of_motion,number_of_nodes)
        self.Me_g = Global.get_Me_global(self,Bars,number_degrees_of_motion,number_of_nodes)
        self.Contorno = np.array(Contorno) #Por enquanto não fiz um set_Contorno
        #self.C = m.set_C()
        self.C = np.transpose(np.array(C))
        self.Ke_g_reduzida = Global.get_Ke_global_reduzida(self)
        self.Me_g_reduzida = Global.get_Me_global_reduzida(self)
        #self.F = m.set_F()
        self.F = np.transpose(np.array(F))
        self.F_reduzida = Global.get_F_reduzida(self)
    
    
    #Este eu faço pouca ideia mas tenho uma pequena lógica
    def get_Ke_global(self,Bars,number_degrees_of_motion,number_of_nodes): #Bars is a list of Bar objects
        temp = np.zeros([number_degrees_of_motion*number_of_nodes,number_degrees_of_motion*number_of_nodes]) #Preallocating
        Ke_global = np.copy(temp)
        
        for n in range(len(Bars)):
            T = m.get_T2(Bars[n])
            T[np.isclose(T,0)] = 0 #Erro de aproximação
            
            Ke_p = np.matmul(np.matmul(np.matrix.transpose(T),m.get_Ke_v(Bars[n])),T)

            for i in range(2):
                for j in range(2):
                    
                    temp[2*(Bars[n].node1)-number_degrees_of_motion+i,2*(Bars[n].node1)-number_degrees_of_motion+j] = Ke_p[i,j]
                    temp[2*(Bars[n].node1)-number_degrees_of_motion+i,2*(Bars[n].node2)-number_degrees_of_motion+j] = Ke_p[i,j+number_degrees_of_motion]
                    temp[2*(Bars[n].node2)-number_degrees_of_motion+i,2*(Bars[n].node1)-number_degrees_of_motion+j] = Ke_p[i+number_degrees_of_motion,j]
                    temp[2*(Bars[n].node2)-number_degrees_of_motion+i,2*(Bars[n].node2)-number_degrees_of_motion+j] = Ke_p[i+number_degrees_of_motion,j+number_degrees_of_motion]
            
            Ke_global += temp
            Ke_global[np.isclose(Ke_global,0)] = 0 #Erro de aproximação

            temp = np.zeros([number_degrees_of_motion*number_of_nodes,number_degrees_of_motion*number_of_nodes]) #Resetting

           
        return Ke_global

    def get_Me_global(self,Bars,number_degrees_of_motion,number_of_nodes): #Bars is a list of Bar objects
        temp = np.zeros([number_degrees_of_motion*number_of_nodes,number_degrees_of_motion*number_of_nodes]) #Preallocating
        Me_global = np.copy(temp)
        
        #Iniciar a T fora para o emilio do mal nao relcamar de eficiente e custo
        for n in range(len(Bars)):
            T = m.get_T2(Bars[n])
            T[np.isclose(T,0)] = 0 #Erro de aproximação
            
            Me_p = np.matmul(np.matmul(np.matrix.transpose(T),m.get_Me_v(Bars[n])),T)

            for i in range(2):
                for j in range(2):
                    
                    temp[2*(Bars[n].node1)-number_degrees_of_motion+i,2*(Bars[n].node1)-number_degrees_of_motion+j] = Me_p[i,j]
                    temp[2*(Bars[n].node1)-number_degrees_of_motion+i,2*(Bars[n].node2)-number_degrees_of_motion+j] = Me_p[i,j+number_degrees_of_motion]
                    temp[2*(Bars[n].node2)-number_degrees_of_motion+i,2*(Bars[n].node1)-number_degrees_of_motion+j] = Me_p[i+number_degrees_of_motion,j]
                    temp[2*(Bars[n].node2)-number_degrees_of_motion+i,2*(Bars[n].node2)-number_degrees_of_motion+j] = Me_p[i+number_degrees_of_motion,j+number_degrees_of_motion]
            
            Me_global += temp
            Me_global[np.isclose(Me_global,0)] = 0
            #Me_global[Me_global**2<10**(-8)] = 0 #Erro de aproximação #Me is close

            temp = np.zeros([number_degrees_of_motion*number_of_nodes,number_degrees_of_motion*number_of_nodes]) #Resetting
        
        
        return Me_global


    def get_Ke_global_reduzida(self):
        Ke_global_reduzida = np.copy(self.Ke_g)

        index_zeros = np.where(self.Contorno==0)[0] #Find where are all the zeros in the contour conditions

        for i in index_zeros:

            Ke_global_reduzida[:,i] = 0
            Ke_global_reduzida[i,:] = 0

            Ke_global_reduzida[i,i] = 1
        
        return Ke_global_reduzida
    
    def get_Me_global_reduzida(self):
        Me_global_reduzida = np.copy(self.Me_g)

        index_zeros = np.where(self.Contorno==0)[0] #Find where are all the zeros in the contour conditions

        for i in index_zeros:

            Me_global_reduzida[:,i] = 0
            Me_global_reduzida[i,:] = 0

            Me_global_reduzida[i,i] = 1
        
        return Me_global_reduzida
    
    def get_F_reduzida(self):
        F_reduzida = np.copy(self.F)

        index_zeros = np.where(self.Contorno==0)[0] #Find where are all the zeros in the contour conditions

        for i in index_zeros:
            F_reduzida[i] = 0

        print(np.matrix.view(F_reduzida))    
        return F_reduzida