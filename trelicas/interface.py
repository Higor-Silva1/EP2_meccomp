import trelicas_static as ts
import numpy as np
from Bar import Bar
import copy

print("Esses são os tipos de problemas disponíveis atualmente:")
print("(1) Treliças em regime estático\n")

type = int(input("Qual o tipo do seu problema: \n"))

if type == 1:

    ###### Creating the Bars ######
    Bars = []
    K_e = []
    M_e = []

    n = int(input("Qual o número de Barras do problema?:"))
    for i in range(n):
        print("Quais as características da Barra", i+1, "?")
        obj = Bar.get_user_input()
        Bars.append(obj)

        K_e.append(ts.Ke_mod(Bars[i]))
        M_e.append(ts.Me_mod(Bars[i]))
    ###############################

    ##### Creating the Global Matrix #####
    n = float(input)

    
    