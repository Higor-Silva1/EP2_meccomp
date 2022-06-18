import numpy as np

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
                    
            
