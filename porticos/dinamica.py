import numpy as np
from Bar import Bar
from Global import Global

#numpy.linalg.eig() para obter os autovelores e autovetores em análise modal
#Lembrar que os autovalores serão w^2 e não w em si

def analize(Global_Matrix): #Se preciso, testar se Global_Matrix is type global e avisar se não for
    print("Qual o tipo de análise deve ser realizada?\n")
    print("Digite 1 para Análise Modal sem Amortecimento\n")
    print("Digite 2 para Análise Harmônica sem Amortecimento\n")
    print("Digite 3 para Análise Modal com Amortecimento\n")
    print("Digite 4 para Análise Harmônica com Amortecimento\n")
    mode = int(input()) #Mudar para validade input do EP1 caso necessário

    #if mode == 0: por favor, insira um modo de análise (pedir input novamente)

    #Adicionar simplificações nos modos possíveis
    if mode == 1:
        print("Realizando Análise Modal sem Amortecimento \n \n")
        #Pelo visto não é a matriz global que se utiliza, e sim a matriz reduzida aaaaa
        [auto_valores, auto_vetores] = np.linalg.eig(np.linalg.inv(Global_Matrix.Me_g_reduzida)@Global_Matrix.Ke_g_reduzida)
        
        #Não tenho certeza se auto_vetores = modos_de_vibrar rever aula
        ########## Consertar modos_de_vibrar ########### 
        modos_de_vibrar = auto_vetores
        modos_de_vibrar[np.isclose(modos_de_vibrar,0)] = 0
        omega = np.sqrt(auto_valores)
        omega_hertz = omega/(2*np.pi)

        print("As frequências de ressonância são: \n")
        for i in range(len(omega)):
            print("w",i+1,"=",omega[i],"\n")
        
        print("Os modos de vibrar são: \n")
        for q in range(len(omega)):
            print("Modo",q+1,"=",np.matrix.view(modos_de_vibrar[q]),"\n")
    
    if mode == 2:
        print("Realizando Análise Harmônica sem Amortecimento \n \n")
        print("Escolha o tamnho do passo da frequência: \n")
        h = float(input())
        print("Escolha o a frequência final (assumindo incial == 0): \n")
        w_f = float(input())

        #for i in range((w_f))


