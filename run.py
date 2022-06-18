from objects import Bar
import numpy as np

E = 4.22*10**5
A = 1
L = 1

Bar1 = Bar(E,A,L,0,0,1,2,0)
Bar2 = Bar(E,A,L,0,0,2,3,135)
Bar3 = Bar(E,A,L,0,0,3,4,0)
Bar4 = Bar(E,A,L,0,0,2,4,90)
Bar5 = Bar(E,A,L,0,0,2,5,45)
Bar6 = Bar(E,A,L,0,0,4,5,0)

#np.matrix.view(matrices.get_Ke_v(Bar1))