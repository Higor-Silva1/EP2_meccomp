import numpy as np
from objects import bar, Global

#numpy.linalg.eig() para obter os autovelores e autovetores em análise modal
#Lembrar que os autovalores serão w^2 e não w em si

def analize(mode):
    print("Qual o tipo de análise deve ser realizada?\n")
    print("Digite 1 para Análise Modal sem Amortecimento\n")
    print("Digite 2 para Análise Harmônica sem Amortecimento\n")
    print("Digite 3 para Análise Modal com Amortecimento\n")
    print("Digite 4 para Análise Harmônica com Amortecimento\n")
    mode = int(input()) #Mudar para validade input do EP1

    if mode == 1:


