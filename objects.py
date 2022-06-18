import numpy as np
from porticos import matrices as m

class bar:
    def __init__(self, E=0, A=0, L=0, pho=0, I = 0, node1=0, node2=0,theta=0):
        self.E = E          #bar's elastic module
        self.A = A          #bar's section area
        self.L = L          #bar's size
        self.pho = pho      #bar's density
        self.I = I          #Inertia
        self.node1 = node1  #first bar's node
        self.node2 = node2
        self.theta = theta*np.pi/180  #bar's angle to the horizontal

    @classmethod

    def get_user_input(self):
        E = float(input("Indique o módulo elástico da barra: "))
        A = float(input("Indique a área da seção da barra: "))
        L = float(input("Indique o comprimeto da barra: "))
        pho = float(input("Indique a densidade da barra: "))
        I = float(input("Indique a constante de inércia da barra: "))
        node1 = int(input("Indique o primeiro nó relacionado a barra: "))
        node2 = int(input("Indique o segundo nó relacionado a barra: "))
        theta = float(input("Indique o ânglo da barra: "))

        return self(E, A, L, pho, node1, node2)

class Global:
    
    def __init__(self,number_degrees_of_motion,number_of_nodes):
        self.number_degrees_of_motion = number_degrees_of_motion
        self.number_of_nodes = number_of_nodes
        self.size = number_degrees_of_motion*number_of_nodes
        self.K_e_global = np.zeros(self.size)
    
    @classmethod

    def creat_K_e_global(self,bars): #bars is a list of bar objects
        zeros = np.zeros(self.size) #Preallocating

        for n in range(len(bars)):
            Ke_p = m.get_Ke_p(bars[n])

            for i in range(self.number_degrees_of_motion):
                zeros[2*(bars[n].node1)-1+i,]
            
