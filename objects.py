import numpy as np
from porticos import matrices as m

class Bar:
    def __init__(self, E=0, A=0, L=0, pho=0, I = 0, node1=0, node2=0,theta=0):
        self.E = E          #Bar's elastic module
        self.A = A          #Bar's section area
        self.L = L          #Bar's size
        self.pho = pho      #Bar's density
        self.I = I          #Inertia
        self.node1 = node1  #first Bar's node
        self.node2 = node2
        self.theta = theta*np.pi/180  #Bar's angle to the horizontal

    @classmethod

    def get_user_input(self):
        E = float(input("Indique o módulo elástico da Barra: "))
        A = float(input("Indique a área da seção da Barra: "))
        L = float(input("Indique o comprimeto da Barra: "))
        pho = float(input("Indique a densidade da Barra: "))
        I = float(input("Indique a constante de inércia da Barra: "))
        node1 = int(input("Indique o primeiro nó relacionado a Barra: "))
        node2 = int(input("Indique o segundo nó relacionado a Barra: "))
        theta = float(input("Indique o ânglo da Barra: "))

        return self(E, A, L, pho, node1, node2)

class Global:
    
    def __init__(self,number_degrees_of_motion,number_of_nodes):
        self.number_degrees_of_motion = number_degrees_of_motion
        self.number_of_nodes = number_of_nodes
        self.size = number_degrees_of_motion*number_of_nodes
        self.Ke_global = np.zeros(self.size)
        self.Me_global = np.zeros(self.size)
    
    @classmethod

    #Este eu faço pouca ideia mas tenho uma pequena lógica
    def creat_Ke_global(self,Bars): #Bars is a list of Bar objects
        temp = np.zeros(self.size) #Preallocating

        for n in range(len(Bars)):
            Ke_p = m.get_Ke_p(Bars[n])

            for i in range(self.number_degrees_of_motion):
                for j in range(self.number_degrees_of_motion):
                    temp[2*(Bars[n].node1)-1+i,2*(Bars[n].node1)-1+j] = Ke_p[i,j]
                    temp[2*(Bars[n].node1)-1+i,2*(Bars[n].node2)-1+j] = Ke_p[i,j+self.number_degrees_of_motion]
                    temp[2*(Bars[n].node2)-1+i,2*(Bars[n].node1)-1+j] = Ke_p[i+self.number_degrees_of_motion,j]
                    temp[2*(Bars[n].node2)-1+i,2*(Bars[n].node2)-1+j] = Ke_p[i+self.number_degrees_of_motion,j+self.number_degrees_of_motion]
            
            self.Ke_global += temp
            temp = np.zeros(self.size) #Resetting

    #Este eu simplesmente não faço ideia
    def creat_Me_global(self,Bars): #Bars is a list of Bar objects
        temp = np.zeros(self.size) #Preallocating

        for n in range(len(Bars)):
            Ke_p = m.get_Ke_p(Bars[n])

            for i in range(self.number_degrees_of_motion):
                for j in range(self.number_degrees_of_motion):
                    temp[2*(Bars[n].node1)-1+i,2*(Bars[n].node1)-1+j] = Ke_p[i,j]
                    temp[2*(Bars[n].node1)-1+i,2*(Bars[n].node2)-1+j] = Ke_p[i,j+self.number_degrees_of_motion]
                    temp[2*(Bars[n].node2)-1+i,2*(Bars[n].node1)-1+j] = Ke_p[i+self.number_degrees_of_motion,j]
                    temp[2*(Bars[n].node2)-1+i,2*(Bars[n].node2)-1+j] = Ke_p[i+self.number_degrees_of_motion,j+self.number_degrees_of_motion]
            
            self.Me_global += temp
            temp = np.zeros(self.size) #Resetting
                    
            
