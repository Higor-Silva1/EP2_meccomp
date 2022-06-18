import trelicas_static as ts
import numpy as np
from objects import bar
import copy

print("Esses são os tipos de problemas disponíveis atualmente:")
print("(1) Treliças em regime estático\n")

type = int(input("Qual o tipo do seu problema: \n"))

if type == 1:

    ###### Creating the bars ######
    bars = []
    K_e = []
    M_e = []

    n = int(input("Qual o número de barras do problema?:"))
    for i in range(n):
        print("Quais as características da barra", i+1, "?")
        obj = bar.get_user_input()
        bars.append(obj)

        K_e.append(ts.Ke_mod(bars[i]))
        M_e.append(ts.Me_mod(bars[i]))
    ###############################

    ##### Creating the Global Matrix #####
    n = float(input)

    
    