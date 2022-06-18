import numpy as np
from porticos import matrices as m

class Global:
    
    def __init__(self,number_degrees_of_motion,number_of_nodes,size=0,Ke_global=[],Me_global=[]):
        self.number_degrees_of_motion = number_degrees_of_motion
        self.number_of_nodes = number_of_nodes
        self.size = number_degrees_of_motion*number_of_nodes
        self.Ke_global = np.zeros([self.size,self.size])
        self.Me_global = np.zeros([self.size,self.size])
    
    @classmethod

    #Este eu faço pouca ideia mas tenho uma pequena lógica
    def get_Ke_global(self,Bars): #Bars is a list of Bar objects
        temp = np.zeros([self.size,self.size]) #Preallocating

        for n in range(len(Bars)):
            Ke_p = m.get_Ke_p(Bars[n])

            for i in range(self.number_degrees_of_motion):
                for j in range(self.number_degrees_of_motion):
                    temp[2*(Bars[n].node1)-1+i,2*(Bars[n].node1)-1+j] = Ke_p[i,j]
                    temp[2*(Bars[n].node1)-1+i,2*(Bars[n].node2)-1+j] = Ke_p[i,j+self.number_degrees_of_motion]
                    temp[2*(Bars[n].node2)-1+i,2*(Bars[n].node1)-1+j] = Ke_p[i+self.number_degrees_of_motion,j]
                    temp[2*(Bars[n].node2)-1+i,2*(Bars[n].node2)-1+j] = Ke_p[i+self.number_degrees_of_motion,j+self.number_degrees_of_motion]
            
            self.Ke_global += temp
            temp = np.zeros([self.size,self.size]) #Resetting

    #Este eu simplesmente não faço ideia alguma
    def get_Me_global(self,Bars): #Bars is a list of Bar objects
        temp = np.zeros([self.size,self.size]) #Preallocating

        for n in range(len(Bars)):
            Ke_p = m.get_Ke_p(Bars[n])

            for i in range(self.number_degrees_of_motion):
                for j in range(self.number_degrees_of_motion):
                    temp[2*(Bars[n].node1)-1+i,2*(Bars[n].node1)-1+j] = Ke_p[i,j]
                    temp[2*(Bars[n].node1)-1+i,2*(Bars[n].node2)-1+j] = Ke_p[i,j+self.number_degrees_of_motion]
                    temp[2*(Bars[n].node2)-1+i,2*(Bars[n].node1)-1+j] = Ke_p[i+self.number_degrees_of_motion,j]
                    temp[2*(Bars[n].node2)-1+i,2*(Bars[n].node2)-1+j] = Ke_p[i+self.number_degrees_of_motion,j+self.number_degrees_of_motion]
            
            self.Me_global += temp
            temp = np.zeros([self.size,self.size]) #Resetting