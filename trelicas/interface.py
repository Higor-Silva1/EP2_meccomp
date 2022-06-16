import trelicas_static as ts
import numpy as np
from objects import bar
import copy

print("(1) Treliças em regime estático")
type = int(input("Qual o tipo do seu problema: \n"))

if type == 1:
    bars = []
    n = int(input("Qual o número de barras do problema?:"))
    for i in range(n):
        #bars = np.zeros(n) #Prealocate array
        print("Quais as características da barra", i+1, "?")
        obj = bar.get_user_input()
        bars.append(obj)

print(bars[0].A,"\n",bars[1].A)