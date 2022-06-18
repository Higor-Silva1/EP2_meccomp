import numpy as np

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