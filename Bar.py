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
                    
            
